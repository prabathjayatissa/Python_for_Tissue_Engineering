"""
Pandas Exercises for Tissue Engineering Master's Students
==========================================================
A single-file, self-contained set of exercises applying pandas to
real tissue engineering data workflows: cell culture records, qPCR,
mechanical testing, flow cytometry, scaffold fabrication, and clinical
patient metadata. Each exercise is preceded by a short theory section.

Run:  python tissue_engineering_pandas.py
Deps: pandas, numpy, matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def banner(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def theory(text: str) -> None:
    print("\n--- THEORY ---")
    for line in text.strip().split("\n"):
        print(line.strip())
    print("-------------")


def preview(df: pd.DataFrame, name: str, n: int = 5) -> None:
    print(f"\n{name} (shape={df.shape}):")
    print(df.head(n).to_string(index=False))


# ===========================================================================
# Exercise 1: Cell Culture Time Series
# ===========================================================================
def exercise_1():
    banner("Exercise 1: Cell Culture Time Series")

    theory("""
    Cell culture experiments generate longitudinal data: each flask or
    well is measured repeatedly over days. Pandas DataFrames are ideal
    for this long-format data because you can:
        - group by sample / condition,
        - compute per-group statistics,
        - pivot to wide format for plotting growth curves.

    A common derived metric is the population doubling time:
        t_d = ln(2) / mu   where mu = (ln(N2) - ln(N1)) / (t2 - t1)

    Typical workflow:
        groupby  ->  apply  ->  agg  ->  merge back
    """)

    rng = np.random.default_rng(0)
    days = np.arange(0, 15)
    data = []
    for sample in ["MSC-A", "MSC-B", "MSC-C"]:
        N0 = rng.integers(4000, 6000)
        mu = rng.uniform(0.28, 0.42)
        for d in days:
            N = N0 * np.exp(mu * d) * rng.normal(1, 0.05)
            data.append({"sample": sample, "day": int(d),
                         "cells": int(N), "mu": mu})
    df = pd.DataFrame(data)
    preview(df, "Long-format culture data")

    # 1. Pivot to wide format
    wide = df.pivot(index="day", columns="sample", values="cells")
    print("\nWide format:\n", wide.head().to_string())

    # 2. Per-sample summary
    summary = df.groupby("sample").agg(
        initial_cells=("cells", "first"),
        final_cells=("cells", "last"),
        max_cells=("cells", "max"),
        mean_mu=("mu", "mean"),
    )
    summary["fold_expansion"] = summary["final_cells"] / summary["initial_cells"]
    summary["doubling_time_days"] = np.log(2) / summary["mean_mu"]
    print("\nPer-sample summary:\n", summary.round(2).to_string())

    # 3. Plot growth curves
    plt.figure()
    for s in wide.columns:
        plt.plot(wide.index, wide[s] / 1000, marker="o", label=s)
    plt.xlabel("Day")
    plt.ylabel("Cells (x1000)")
    plt.title("Cell Growth Curves")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("pandas_ex1_growth.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 2: qPCR Batch Analysis
# ===========================================================================
def exercise_2():
    banner("Exercise 2: qPCR Batch Analysis")

    theory("""
    qPCR data is naturally tabular:
        rows = wells (gene x donor x replicate)
        columns = Ct value and metadata

    The 2^-dCt method:
        dCt = Ct_target - Ct_housekeeping
        relative expression = 2^(-dCt)

    In pandas:
        - pivot so housekeeping and target genes are aligned per donor,
        - compute dCt row-wise (broadcasting columns),
        - group by gene x condition to summarize.
    """)

    rng = np.random.default_rng(1)
    genes = ["COL1A1", "SOX9", "RUNX2", "GAPDH"]
    conditions = ["static", "perfused"]
    donors = ["D1", "D2", "D3", "D4"]
    rows = []
    for cond in conditions:
        for d in donors:
            for g in genes:
                base = {"GAPDH": 20, "COL1A1": 22, "SOX9": 27, "RUNX2": 28}[g]
                if cond == "perfused" and g in ("COL1A1", "SOX9"):
                    base -= 1.5  # perfusion upregulates matrix genes
                for rep in range(3):
                    rows.append({
                        "condition": cond, "donor": d, "gene": g,
                        "replicate": rep,
                        "Ct": base + rng.normal(0, 0.15),
                    })
    df = pd.DataFrame(rows)
    preview(df, "qPCR raw data")

    # 1. Average technical replicates
    tech = (df.groupby(["condition", "donor", "gene"])["Ct"]
              .mean().reset_index())
    preview(tech, "Technical replicate means")

    # 2. Pivot so we have housekeeping as a column
    wide = tech.pivot_table(index=["condition", "donor"],
                            columns="gene", values="Ct").reset_index()
    hk = "GAPDH"
    for g in ["COL1A1", "SOX9", "RUNX2"]:
        wide[f"dCt_{g}"] = wide[g] - wide[hk]
        wide[f"rel_{g}"] = 2 ** (-wide[f"dCt_{g}"])

    # 3. Summary per condition
    summary = (wide.groupby("condition")[["rel_COL1A1", "rel_SOX9", "rel_RUNX2"]]
                    .agg(["mean", "std"]))
    print("\nExpression summary (mean +/- SD across donors):")
    print(summary.round(3).to_string())

    # 4. Plot
    genes_plot = ["rel_COL1A1", "rel_SOX9", "rel_RUNX2"]
    means = wide.groupby("condition")[genes_plot].mean()
    errs = wide.groupby("condition")[genes_plot].std()
    ax = means.plot(kind="bar", yerr=errs, capsize=4, figsize=(7, 4))
    ax.set_ylabel("Relative expression (2^-dCt)")
    ax.set_title("qPCR: static vs perfused")
    plt.tight_layout()
    plt.savefig("pandas_ex2_qpcr.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 3: Mechanical Testing of Scaffolds
# ===========================================================================
def exercise_3():
    banner("Exercise 3: Mechanical Testing of Scaffolds")

    theory("""
    A mechanical test rig produces one row per (sample, strain step).
    For each sample we want:
        - Young's modulus E (slope of stress-strain in linear region),
        - yield stress (max stress),
        - toughness (area under the stress-strain curve).

    In pandas:
        - groupby("sample_id").apply(func) to fit each curve,
        - trapezoid integration via np.trapz on each group,
        - merge results back into a tidy summary table.

    Formulas:
        E       = d(sigma)/d(epsilon)   in the linear region
        sigma_y = max(sigma)
        toughness = integral(sigma d(epsilon))
    """)

    rng = np.random.default_rng(2)
    data = []
    formulations = {"A": 100, "B": 130, "C": 160}
    for sample_id, (form, E_base) in enumerate(
        [(f, e) for f, e in formulations.items() for _ in range(4)],
        start=1,
    ):
        strain = np.linspace(0, 0.3, 30)
        stress = E_base * strain + rng.normal(0, 1.0, strain.size)
        for s, sig in zip(strain, stress):
            data.append({"sample_id": sample_id, "formulation": form,
                         "strain": s, "stress": sig})
    df = pd.DataFrame(data)
    preview(df, "Mechanical test data")

    def fit_sample(g):
        linear = g[(g["strain"] >= 0.05) & (g["strain"] <= 0.15)]
        E = np.polyfit(linear["strain"], linear["stress"], 1)[0]
        yield_stress = g["stress"].max()
        toughness = np.trapz(g["stress"], g["strain"])
        return pd.Series({"E_kPa": E,
                          "yield_kPa": yield_stress,
                          "toughness_kPa": toughness})

    per_sample = df.groupby(["sample_id", "formulation"]).apply(
        fit_sample, include_groups=False).reset_index()
    preview(per_sample, "Per-sample properties")

    summary = per_sample.groupby("formulation")[["E_kPa", "yield_kPa",
                                                 "toughness_kPa"]].agg(["mean", "std"])
    print("\nFormulation summary:\n", summary.round(2).to_string())

    per_sample.boxplot(column="E_kPa", by="formulation")
    plt.title("Young's modulus by formulation")
    plt.suptitle("")
    plt.ylabel("E (kPa)")
    plt.tight_layout()
    plt.savefig("pandas_ex3_mech.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 4: Flow Cytometry Immunophenotyping
# ===========================================================================
def exercise_4():
    banner("Exercise 4: Flow Cytometry Immunophenotyping")

    theory("""
    Flow cytometry reports the percentage of cells positive for each
    surface marker (e.g., CD73, CD90, CD105 for MSCs; CD34, CD45 as
    negative markers). Results are typically stored as:
        donor x marker x % positive

    In pandas:
        - pivot donors x markers into a matrix,
        - filter with .query() or boolean masks,
        - use .apply() to compute a gating rule per donor,
        - use .sort_values() to rank samples.

    A typical MSC identity rule (ISCT criteria):
        CD73+ > 95%, CD90+ > 95%, CD105+ > 95%,
        CD34+ < 2%, CD45+ < 2%.
    """)

    rng = np.random.default_rng(3)
    donors = [f"D{i}" for i in range(1, 9)]
    markers = ["CD73", "CD90", "CD105", "CD34", "CD45"]
    rows = []
    for d in donors:
        for m in markers:
            if m in ("CD73", "CD90", "CD105"):
                pct = rng.normal(96, 3)
            else:
                pct = rng.normal(1.5, 0.8)
            rows.append({"donor": d, "marker": m,
                         "pct_positive": np.clip(pct, 0, 100)})
    df = pd.DataFrame(rows)
    preview(df, "Flow cytometry results")

    wide = df.pivot(index="donor", columns="marker",
                    values="pct_positive").round(2)
    print("\nWide matrix:\n", wide.to_string())

    def is_msc(row):
        return (row["CD73"] > 95 and row["CD90"] > 95 and row["CD105"] > 95
                and row["CD34"] < 2 and row["CD45"] < 2)

    wide["passes_ISCT"] = wide.apply(is_msc, axis=1)
    print("\nPassing ISCT criteria:\n", wide["passes_ISCT"].to_string())

    fails = wide.query("passes_ISCT == False")
    print(f"\n{len(fails)} donor(s) failed the criteria.")
    print(f"Overall pass rate: {wide['passes_ISCT'].mean() * 100:.1f}%")


# ===========================================================================
# Exercise 5: Scaffold Fabrication Batch Log
# ===========================================================================
def exercise_5():
    banner("Exercise 5: Scaffold Fabrication Batch Log")

    theory("""
    Scaffold fabrication logs record batch-level process parameters
    (polymer concentration, porogen fraction, crosslinker time) and
    resulting quality metrics (porosity, pore size, modulus). These are
    classic tidy-data operations:

        - .merge() to combine fabrication and QC tables,
        - .assign() to derive new columns,
        - .groupby().agg() for batch statistics,
        - .corr() to inspect relationships between parameters and quality.

    A Pearson correlation matrix across process and outcome columns
    helps identify which parameters most influence scaffold quality.
    """)

    rng = np.random.default_rng(4)
    fab = pd.DataFrame({
        "batch_id": np.arange(1, 21),
        "polymer_pct": rng.uniform(8, 16, 20).round(2),
        "porogen_pct": rng.uniform(40, 80, 20).round(2),
        "crosslink_min": rng.integers(5, 30, 20),
    })
    # QC depends on fabrication parameters
    qc = pd.DataFrame({
        "batch_id": fab["batch_id"],
        "porosity": (0.3 + 0.005 * fab["porogen_pct"]
                     - 0.008 * fab["polymer_pct"]
                     + rng.normal(0, 0.02, 20)).round(3),
        "pore_size_um": (50 + 0.6 * fab["porogen_pct"]
                         - 1.5 * fab["polymer_pct"]
                         + rng.normal(0, 3, 20)).round(1),
        "modulus_kPa": (30 + 4 * fab["polymer_pct"]
                        + 0.5 * fab["crosslink_min"]
                        - 0.3 * fab["porogen_pct"]
                        + rng.normal(0, 5, 20)).round(1),
    })

    merged = fab.merge(qc, on="batch_id")
    preview(merged, "Fabrication + QC")

    # Derived columns
    merged = merged.assign(
        stiffness_class=pd.cut(merged["modulus_kPa"],
                               bins=[0, 60, 90, 200],
                               labels=["soft", "medium", "stiff"]),
        high_porosity=merged["porosity"] > 0.7,
    )
    print("\nWith derived columns:\n",
          merged[["batch_id", "modulus_kPa", "stiffness_class",
                  "high_porosity"]].to_string(index=False))

    # Correlation matrix
    corr = merged[["polymer_pct", "porogen_pct", "crosslink_min",
                   "porosity", "pore_size_um", "modulus_kPa"]].corr()
    print("\nCorrelation matrix:\n", corr.round(2).to_string())

    # Batch QC summary by stiffness class
    print("\nQC by stiffness class:")
    print(merged.groupby("stiffness_class", observed=True)[
        ["porosity", "pore_size_um", "modulus_kPa"]].mean().round(2).to_string())


# ===========================================================================
# Exercise 6: Patient / Donor Registry & Join Operations
# ===========================================================================
def exercise_6():
    banner("Exercise 6: Patient / Donor Registry & Joins")

    theory("""
    Clinical translation studies combine:
        - a donor registry (age, sex, BMI, diagnosis),
        - sample-level assay results (one row per donor x assay).

    Pandas supports SQL-style joins:
        pd.merge(left, right, on=..., how='inner'|'left'|'outer')

    Missing data is common (skipped assays). Handle with:
        - .isna().sum()        -> count missing per column
        - .fillna(value)       -> impute a constant
        - .dropna(subset=[...])-> drop only where critical
        - .interpolate()       -> for ordered/time data

    Group-wise imputation (e.g., median per diagnosis) is a common
    clinical-preprocessing step.
    """)

    rng = np.random.default_rng(5)
    donors = pd.DataFrame({
        "donor_id": [f"D{i:03d}" for i in range(1, 21)],
        "age": rng.integers(25, 75, 20),
        "sex": rng.choice(["M", "F"], 20),
        "bmi": rng.normal(26, 4, 20).round(1),
        "diagnosis": rng.choice(["OA", "RA", "Healthy"], 20,
                                p=[0.4, 0.3, 0.3]),
    })

    assays = pd.DataFrame({
        "donor_id": [f"D{i:03d}" for i in range(1, 18)],  # some missing
        "ALP_activity": rng.normal(50, 12, 17).round(1),
        "GAG_content": rng.normal(80, 20, 17).round(1),
    })
    # Introduce missing values in assay results
    mask = rng.random(assays.shape[0]) < 0.15
    assays.loc[mask, "GAG_content"] = np.nan

    merged = donors.merge(assays, on="donor_id", how="left")
    preview(merged, "Merged donor + assays")

    print("\nMissing values per column:\n", merged.isna().sum().to_string())

    # Group-wise imputation by diagnosis
    merged["GAG_content_imputed"] = merged.groupby("diagnosis")["GAG_content"].transform(
        lambda s: s.fillna(s.median()))
    print("\nAfter imputation (GAG_content_imputed):")
    print(merged[["donor_id", "diagnosis", "GAG_content",
                  "GAG_content_imputed"]].head(8).to_string(index=False))

    # Summary per diagnosis
    summary = merged.groupby("diagnosis").agg(
        n=("donor_id", "count"),
        mean_age=("age", "mean"),
        mean_BMI=("bmi", "mean"),
        mean_ALP=("ALP_activity", "mean"),
        mean_GAG=("GAG_content_imputed", "mean"),
    ).round(2)
    print("\nSummary per diagnosis:\n", summary.to_string())


# ===========================================================================
# Exercise 7: Bioreactor Sensor Time Series & Resampling
# ===========================================================================
def exercise_7():
    banner("Exercise 7: Bioreactor Sensors & Resampling")

    theory("""
    Bioreactors log sensor data (pH, DO, temperature, glucose) at high
    frequency (seconds to minutes). To analyze:
        - set a DatetimeIndex,
        - resample to a lower frequency ('1H') and aggregate,
        - interpolate gaps with .interpolate(method='time'),
        - use .rolling(window).mean() to smooth noise.

    Key pandas tools:
        pd.to_datetime(...)
        df.set_index('timestamp')
        df.resample('1H').mean()
        df.rolling('15min').mean()
    """)

    rng = np.random.default_rng(6)
    ts = pd.date_range("2025-01-01 00:00", periods=24 * 60,
                       freq="1min")  # one day, per-minute
    t_hours = np.arange(len(ts)) / 60.0
    df = pd.DataFrame({
        "timestamp": ts,
        "pH": 7.2 + 0.05 * np.sin(t_hours / 3) + rng.normal(0, 0.02, len(ts)),
        "DO_pct": 60 + 10 * np.sin(t_hours / 4) + rng.normal(0, 1.5, len(ts)),
        "temp_C": 37 + 0.3 * np.sin(t_hours / 6) + rng.normal(0, 0.1, len(ts)),
        "glucose_mM": 25 * np.exp(-t_hours / 20) + rng.normal(0, 0.3, len(ts)),
    }).set_index("timestamp")

    preview(df.reset_index(), "Raw bioreactor log")

    hourly = df.resample("1H").agg(["mean", "std"])
    print("\nHourly resampled (first 5 rows):")
    print(hourly.head().round(3).to_string())

    smoothed = df[["pH", "DO_pct", "glucose_mM"]].rolling("15min").mean()
    print("\nSmoothed (15-min rolling mean) tail:")
    print(smoothed.tail(3).round(3).to_string())

    # Report time when glucose drops below 5 mM
    below = df[df["glucose_mM"] < 5]
    if not below.empty:
        print(f"\nGlucose < 5 mM first at: {below.index[0]}")
    else:
        print("\nGlucose never dropped below 5 mM.")

    # Plot
    fig, axs = plt.subplots(3, 1, figsize=(8, 6), sharex=True)
    axs[0].plot(df.index, df["pH"], alpha=0.4, label="raw")
    axs[0].plot(smoothed.index, smoothed["pH"], label="15-min mean")
    axs[0].set_ylabel("pH"); axs[0].legend(fontsize=8); axs[0].grid(True)
    axs[1].plot(df.index, df["DO_pct"], alpha=0.4)
    axs[1].plot(smoothed.index, smoothed["DO_pct"])
    axs[1].set_ylabel("DO (%)"); axs[1].grid(True)
    axs[2].plot(df.index, df["glucose_mM"], alpha=0.4)
    axs[2].plot(smoothed.index, smoothed["glucose_mM"])
    axs[2].set_ylabel("Glucose (mM)"); axs[2].grid(True)
    plt.tight_layout()
    plt.savefig("pandas_ex7_bioreactor.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 8: Histology Scoring (Wide <-> Long, Pivot Tables)
# ===========================================================================
def exercise_8():
    banner("Exercise 8: Histology Scoring & Pivot Tables")

    theory("""
    Histology scoring is often recorded in wide format: one row per
    sample, columns for each scoring category (e.g., ICRS, O'Driscoll,
    or modified Mankin for cartilage). Two-way reshaping is essential:

        wide -> long:  df.melt(id_vars=..., var_name=..., value_name=...)
        long -> wide:  df.pivot_table(index=..., columns=..., values=...)

    Pivot tables with aggfunc allow summarizing multi-level group data
    (e.g., mean score per treatment x category). Ordinal scores are
    often non-parametric, so median and IQR are preferred over mean/SD.
    """)

    rng = np.random.default_rng(7)
    treatments = ["Control", "TGF-b", "BMP-2", "TGF-b+BMP-2"]
    samples_per_group = 5
    categories = ["Surface", "Matrix", "Cell_distribution", "Integration"]

    rows = []
    for t in treatments:
        for s in range(samples_per_group):
            base = {"Control": 1.5, "TGF-b": 2.2, "BMP-2": 2.4,
                    "TGF-b+BMP-2": 2.8}[t]
            scores = {
                c: int(np.clip(np.round(rng.normal(base, 0.6)), 0, 3))
                for c in categories
            }
            scores.update({"treatment": t, "sample_id": f"{t}_{s}"})
            rows.append(scores)
    wide = pd.DataFrame(rows)
    preview(wide, "Histology scores (wide)")

    long = wide.melt(id_vars=["treatment", "sample_id"],
                     var_name="category", value_name="score")
    preview(long, "Histology scores (long)")

    pivot = long.pivot_table(index="treatment", columns="category",
                             values="score", aggfunc="mean").round(2)
    print("\nMean score per treatment x category:\n", pivot.to_string())

    ordinal = long.groupby(["treatment", "category"])["score"].agg(
        median="median",
        q1=lambda s: s.quantile(0.25),
        q3=lambda s: s.quantile(0.75),
        n="count")
    print("\nMedian [Q1, Q3] per group:\n", ordinal.to_string())

    pivot.plot(kind="bar", figsize=(8, 4), ylim=(0, 3.2))
    plt.ylabel("Mean score (0-3)")
    plt.title("Histology scoring by treatment")
    plt.grid(True, axis="y")
    plt.tight_layout()
    plt.savefig("pandas_ex8_histology.png", dpi=120)
    plt.close()


# ===========================================================================
# Main
# ===========================================================================
def main():
    print("Pandas Exercises for Tissue Engineering Master's Students")
    print("Note: figures are saved as PNG files in the current directory.")

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()

    print("\nAll exercises completed. Figures saved as pandas_ex*.png")


if __name__ == "__main__":
    main()
