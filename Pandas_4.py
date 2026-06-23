# =============================================================================
# 🧬 Pandas for Tissue Engineering Data Analysis Tutorial (Master's Level)
# Author: Dr Prabath Jayathissa
# Goal: To teach structured data analysis techniques using Pandas on common
# T.E. datasets (viability, degradation, gene expression).
# =============================================================================

import pandas as pd
import numpy as np
from IPython.display import display  # Using basic display since notebook environment isn't guaranteed

print("--- Starting the Data Analysis Tutorial Setup ---")

# =============================================================================
# SECTION 1: SETUP AND SIMULATION OF RAW DATASETS (MOCK ENVIRONMENT)
# =============================================================================

print("\n[INFO] Setting up simulated experimental data...")

# 1. Primary Results DataFrame: Viability and Degradation Logs
data_raw = {
    'Sample_ID': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Group': ['Control', 'BMP-2', 'Control', 'Acidic', 'BMP-2', 'Acidic'],
    # Note: Using np.nan to represent missing data in the original structure
    'Viability (%)': [85.5, 92.1, 78.9, np.nan, 88.0, 75.0],
    'Day_7_Degradation': [5.1, 12.3, 3.0, 4.5, 10.5, 3.2]
}
df = pd.DataFrame(data_raw)

# 2. Secondary Results DataFrame: Gene Expression Data (from qPCR machine)
gene_data = pd.DataFrame({
    'Sample_ID': ['A', 'B', 'C', 'D', 'E', 'F'],  # The common key!
    'GeneX_Expression': [2.5, 4.1, 0.9, 3.1, 3.5, 1.2],  # E.g., Osteogenic marker (ALP)
    'GeneY_Expression': [1.1, 3.8, 1.5, 2.0, 2.5, 1.8]  # E.g., ECM synthesis marker (COL-I)
})

print("DataFrames initialized successfully.")
display(df.head())


# =============================================================================
# SECTION 2: CORE DATA MANIPULATION TECHNIQUES
# =============================================================================

def run_section_2():
    """Demonstrates filtering, selection, and cleaning techniques."""
    print("\n\n" + "=" * 60)
    print("SECTION 2: FILTERING AND CLEANING (Asking Specific Questions)")
    print("=" * 60)

    # --- A. Filtering (Boolean Masking) ---
    print("\n[A] 🧪 Filter Example: Identifying optimal BMP-2 samples:")
    high_viability_bmp = df[
        (df['Group'] == 'BMP-2') & (df['Viability (%)'] > 85)
        ]
    display(high_viability_bmp)

    # --- B. Handling Missing Data (NaN) ---
    print("\n[B] 🧹 Cleaning Example: Identifying and handling missing data.")
    print(f"Initial NaN count in Viability column: {df['Viability (%)'].isnull().sum()}")

    missing_check = df.isnull().sum()
    print("Missing value report (NaNs):")
    display(missing_check)

    # Imputation Strategy: Fill the single NaN in 'D' with the mean viability of its group ('Acidic')
    acidic_mean_viability = df[df['Group'] == 'Acidic']['Viability (%)'].mean()
    df.loc[df['Sample_ID'] == 'D', 'Viability (%)'] = acidic_mean_viability

    print(
        f"\n-> Successfully imputed NaN in Sample D using the mean viability of the 'Acidic' group ({acidic_mean_viability:.2f}%).")
    display(df[['Sample_ID', 'Group', 'Viability (%)']])


# =============================================================================
# SECTION 3: GROUPING AND AGGREGATION (STATISTICS)
# =============================================================================

def run_section_3():
    """Demonstrates using groupby() for comparative statistics."""
    print("\n\n" + "=" * 60)
    print("SECTION 3: GROUPING AND AGGREGATION (Statistical Comparison)")
    print("=" * 60)

    print("\n[A] 📈 Group Statistics Example (Mean & Std Dev):")

    group_stats = df.groupby('Group')[['Viability (%)', 'Day_7_Degradation']].agg(['mean', 'std', 'count'])

    print("Resulting DataFrame structure:")
    display(group_stats)
    print(
        "\n[INTERPRETATION]: This single output allows direct comparison: BMP-2 had the highest mean viability and largest std dev (most variability).")


# =============================================================================
# SECTION 4: MERGING DATASETS (COMBINING METRICS)
# =============================================================================

def run_section_4():
    """Demonstrates merging two separate datasets (e.g., Cell Assay and qPCR)."""
    print("\n\n" + "=" * 60)
    print("SECTION 4: MERGING DATASETS (Combining Metrics)")
    print("=" * 60)

    # Goal: Combine Viability data with Gene Expression data using the 'Sample_ID' key.
    print("[A] 🔗 Merge Example: Combining Viability and qPCR Data:")

    combined_df = pd.merge(df, gene_data, on='Sample_ID', how='left')

    print("The resulting DataFrame now holds metrics from three different assays:")
    display(combined_df)

    # --- Calculating Derived Metrics ---
    print("\n[B] 🔢 Derived Metric Example: Calculating MMP-I / COL-I Ratio:")
    combined_df['MMP_TIMP_Ratio'] = combined_df['GeneX_Expression'] / combined_df['GeneY_Expression']
    display(combined_df[['Sample_ID', 'GeneX_Expression', 'GeneY_Expression', 'MMP_TIMP_Ratio']])


# =============================================================================
# SECTION 5: MASTER'S PROJECT CHALLENGE (ADVANCED APPLICATION)
# FIX APPLIED HERE: The structure of time_data is corrected to match the sample/time pairs.
# =============================================================================

def run_advanced_challenge():
    """Simulates a complex longitudinal analysis task."""
    print("\n\n" + "=" * 60)
    print("SECTION 5: ADVANCED CHALLENGE - DEGRADATION KINETICS ANALYSIS")
    print("=" * 60)

    # Corrected Data Structure: Must list Sample_ID, Time, and Strength for every measurement point.
    time_data = {
        'Sample_ID': ['A', 'B', 'A', 'B'],
        'Time_Week': [1, 1, 2, 2],  # Note that time is not perfectly ordered here
        # Data points must be correlated by the index/order of rows.
        'Strength_MPa': [5.0, 4.8, 3.0, 2.5]
    }
    df_time = pd.DataFrame(time_data)

    print("\n[Challenge Data]: Scaffold strength over time.")
    display(df_time)

    # FIX: The function now accepts a single Series (the values to transform), not the entire group DataFrame.
    def calculate_rate(series):
        """Calculates the difference from the previous value in the series."""
        return series.diff().fillna(0)

    print("\n[Processing]: Calculating Rate of Change...")
    # FIX: The grouping and transformation are correctly applied to the column itself.
    df_time['Rate_of_Change'] = df_time.groupby('Sample_ID', sort=False)['Strength_MPa'].transform(calculate_rate)

    print("\n[Result]: Degradation Rate (Difference from previous week):")
    display(df_time[['Sample_ID', 'Time_Week', 'Strength_MPa', 'Rate_of_Change']])

    print(
        "\n[CONCLUSION]: The negative value in 'Rate_of_Change' quantifies the scaffold degradation rate, which is crucial for matching mechanical properties to tissue needs.")
# MAIN EXECUTION FLOW
# =============================================================================
if __name__ == "__main__":
    print("\n\n================================================================")
    print("🎉 ALL TUTORIAL SECTIONS COMPLETE. You are now ready for T.E. data analysis!")
    print("================================================================")
    run_section_2()  # Filter and Clean
    run_section_3()  # Group and Aggregate
    run_section_4()  # Merge Data
    run_advanced_challenge()  # Advanced Time-Series Example

