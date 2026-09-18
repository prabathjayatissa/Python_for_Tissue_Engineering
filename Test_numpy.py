"""
==============================================================
NUMPY MASTERCLASS - 2
For MSc Tissue Engineering Students (FHTW)

Author: Dr Prabath Jayathissa
Run section by section.

==============================================================
"""

"""
NumPy Exercises for Tissue Engineering Master's Students
=========================================================
A single-file, self-contained set of exercises applying NumPy to
real tissue engineering problems. Each exercise is preceded by a
short theory section explaining the biological/physical context
and the mathematical model used.

Run:  python tissue_engineering_numpy.py
Deps: numpy, matplotlib, scipy
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless-safe; remove if you want interactive plots
import matplotlib.pyplot as plt
from scipy import ndimage


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------
def banner(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def theory(text: str) -> None:
    """Print a wrapped theory block."""
    print("\n--- THEORY ---")
    for line in text.strip().split("\n"):
        print(line.strip())
    print("-------------")


# ===========================================================================
# Exercise 1: Cell Seeding Density Calculations
# ===========================================================================
def exercise_1():
    banner("Exercise 1: Cell Seeding Density")

    theory("""
    When seeding cells onto a 3D scaffold, the number of cells required
    depends on the available surface area and the desired seeding density
    (typically expressed in cells/cm^2). For a cylindrical scaffold, the
    total surface area includes the top and bottom circular faces plus the
    lateral (side) surface.

    Formulas:
        A_top + A_bottom = 2 * pi * r^2
        A_lateral        = 2 * pi * r * h
        A_total          = 2 * pi * r^2 + 2 * pi * r * h

    The number of cells needed:
        N_cells = seeding_density * A_total

    The volume of cell suspension required:
        V = N_cells / concentration
    """)

    r = 0.5  # cm (radius of scaffold cylinder)
    h = 0.2  # cm (height)

    surface_area = 2 * np.pi * r**2 + 2 * np.pi * r * h
    print(f"Surface area: {surface_area:.3f} cm^2")

    seeding_density = 10_000  # cells/cm^2
    cells_needed = seeding_density * surface_area
    print(f"Cells needed: {cells_needed:.0f}")

    conc = 2e6  # cells/mL
    volume_uL = (cells_needed / conc) * 1000
    print(f"Volume needed: {volume_uL:.2f} uL")


# ===========================================================================
# Exercise 2: Cell Growth Curve (Exponential Model)
# ===========================================================================
def exercise_2():
    banner("Exercise 2: Exponential Cell Growth")

    theory("""
    In the exponential (log) phase of growth, cell proliferation follows
    first-order kinetics:

        N(t) = N0 * exp(mu * t)

    where:
        N(t)  = cell number at time t
        N0    = initial cell number
        mu    = specific growth rate (1/time)

    The doubling time (time required for the population to double) is:

        t_d = ln(2) / mu

    The population doubling level (PDL) quantifies how many times the
    population has doubled:

        PDL = log2(N / N0)
    """)

    t = np.arange(0, 14.5, 0.5)
    N0 = 5_000
    mu = 0.35  # 1/day

    N = N0 * np.exp(mu * t)

    doubling_time = np.log(2) / mu
    print(f"Doubling time: {doubling_time:.2f} days")

    idx = np.argmax(N > 1e6)
    print(f"Exceeds 1M cells on day {t[idx]}")

    PDL = np.log2(N[-1] / N0)
    print(f"PDL at day 14: {PDL:.2f}")

    plt.figure()
    plt.plot(t, N / 1000, marker="o")
    plt.xlabel("Time (days)")
    plt.ylabel("Cells (x1000)")
    plt.title("Exponential Cell Growth")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ex2_growth_curve.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 3: Mechanical Properties of Tissue Scaffolds
# ===========================================================================
def exercise_3():
    banner("Exercise 3: Scaffold Mechanical Properties")

    theory("""
    In the linear elastic (Hookean) regime, stress and strain are related by:

        sigma = E * epsilon

    where:
        sigma   = applied stress (kPa)
        epsilon = strain (dimensionless)
        E       = Young's modulus (kPa), the slope of the stress-strain curve

    Experimentally, E is estimated by fitting a straight line to the
    linear portion of the stress-strain curve (typically 5-15% strain for
    soft tissue scaffolds).

    For n samples, the standard error of the mean is:
        SE = std / sqrt(n)

    The 95% confidence interval:
        CI = mean +/- 1.96 * SE
    """)

    rng = np.random.default_rng(0)
    strain = np.linspace(0, 0.3, 30)
    stress = np.array([
        strain * 120 + rng.normal(0, 0.5, 30),
        strain * 115 + rng.normal(0, 0.5, 30),
        strain * 128 + rng.normal(0, 0.5, 30),
        strain * 110 + rng.normal(0, 0.5, 30),
        strain * 125 + rng.normal(0, 0.5, 30),
    ])

    mask = (strain >= 0.05) & (strain <= 0.15)
    moduli = np.array([
        np.polyfit(strain[mask], s[mask], 1)[0] for s in stress
    ])
    print(f"Moduli (kPa): {moduli.round(1)}")
    print(f"Mean +/- SD: {moduli.mean():.1f} +/- {moduli.std(ddof=1):.1f} kPa")

    stiffest = np.argmax(moduli)
    compliant = np.argmin(moduli)
    print(f"Stiffest: sample {stiffest}, most compliant: sample {compliant}")

    n = len(moduli)
    se = moduli.std(ddof=1) / np.sqrt(n)
    ci = (moduli.mean() - 1.96 * se, moduli.mean() + 1.96 * se)
    print(f"95% CI: ({ci[0]:.1f}, {ci[1]:.1f}) kPa")

    plt.figure()
    for i, s in enumerate(stress):
        plt.plot(strain, s, label=f"Sample {i} (E={moduli[i]:.0f} kPa)")
    plt.xlabel("Strain")
    plt.ylabel("Stress (kPa)")
    plt.title("Scaffold Stress-Strain Curves")
    plt.legend(fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ex3_stress_strain.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 4: Diffusion of Nutrients in a Hydrogel
# ===========================================================================
def exercise_4():
    banner("Exercise 4: 1D Oxygen Diffusion in Hydrogel")

    theory("""
    Nutrient (e.g., oxygen) transport in avascular tissue constructs is
    governed by Fick's second law. In 1D:

        dC/dt = D * d^2C/dx^2

    where:
        C = concentration (mol/m^3)
        D = diffusion coefficient (m^2/s)
        x = spatial coordinate (m)
        t = time (s)

    Using an explicit finite-difference scheme on a uniform grid
    (spacing dx, time step dt):

        C[i, n+1] = C[i, n] + (D*dt/dx^2) * (C[i+1,n] - 2C[i,n] + C[i-1,n])

    Stability requires:
        dt <= 0.5 * dx^2 / D

    Boundary conditions here are fixed concentration (Dirichlet):
        C(0, t) = C(L, t) = 0.2 mol/m^3

    Initial condition:
        C(x, 0) = 0 everywhere inside the domain.
    """)

    L = 2e-3           # m
    D = 2e-9           # m^2/s
    nx = 51
    dx = L / (nx - 1)
    dt = 0.4 * dx**2 / D   # stability: dt <= 0.5 dx^2 / D

    C = np.zeros(nx)
    C[0] = C[-1] = 0.2   # mol/m^3 boundary

    t_end = 1800
    nt = int(t_end / dt)
    snapshot_every = max(1, nt // 6)
    C_history = []

    steady_state_time = None
    for n in range(nt):
        C_new = C.copy()
        C_new[1:-1] = C[1:-1] + D * dt / dx**2 * (C[2:] - 2 * C[1:-1] + C[:-2])
        if n % snapshot_every == 0:
            C_history.append(C_new.copy())
        if n > 10 and np.max(np.abs(C_new - C)) / 0.2 < 1e-3:
            steady_state_time = n * dt
            break
        C = C_new

    if steady_state_time is not None:
        print(f"Steady state at t = {steady_state_time:.1f} s")
    else:
        print("Steady state not reached within simulation window.")

    x_mm = np.linspace(0, L * 1000, nx)
    plt.figure()
    for i, Ch in enumerate(C_history):
        plt.plot(x_mm, Ch, label=f"t={i * snapshot_every * dt:.0f}s")
    plt.xlabel("Position (mm)")
    plt.ylabel("[O2] (mol/m^3)")
    plt.title("Oxygen Diffusion in Hydrogel")
    plt.legend(fontsize=8)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ex4_diffusion.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 5: Image-Based Cell Counting
# ===========================================================================
def exercise_5():
    banner("Exercise 5: Fluorescence Image Cell Counting")

    theory("""
    Fluorescently labelled cells appear as bright spots on a dark
    background. A simple automated counting pipeline is:

        1. Threshold the image at (mean + k * std) of the background to
           create a binary mask of "cell" pixels.
        2. Label connected components (each component = one cell).
        3. Count components and measure per-cell statistics.
        4. Convert to a density (cells / area) using the known field of view.

    Each synthetic "cell" here is modelled as a 2D Gaussian blob:
        I(x, y) = exp( -((x - cx)^2 + (y - cy)^2) / (2 * sigma^2) )
    with additive Gaussian noise simulating camera/background signal.
    """)

    rng = np.random.default_rng(42)
    img = np.zeros((200, 200))
    centers = rng.integers(20, 180, size=(60, 2))
    y, x = np.ogrid[:200, :200]
    for (cy, cx) in centers:
        img += np.exp(-((y - cy) ** 2 + (x - cx) ** 2) / (2 * 3 ** 2))
    img += rng.normal(0, 0.05, img.shape)

    threshold = img.mean() + 3 * img.std()
    mask = img > threshold

    labels, n_cells = ndimage.label(mask)
    print(f"Detected cells: {n_cells}")

    if n_cells > 0:
        avg_intensity = ndimage.mean(img, labels, range(1, n_cells + 1)).mean()
        print(f"Mean intensity/cell: {avg_intensity:.2f}")

    density = n_cells / (1.0 * 1.0)
    print(f"Density: {density:.0f} cells/mm^2")

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Raw image")
    plt.axis("off")
    plt.subplot(1, 2, 2)
    plt.imshow(mask, cmap="gray")
    plt.title(f"Thresholded ({n_cells} cells)")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("ex5_cells.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 6: 3D Scaffold Porosity Analysis
# ===========================================================================
def exercise_6():
    banner("Exercise 6: 3D Scaffold Porosity & Degradation")

    theory("""
    Porosity is the fraction of void volume within a scaffold:

        porosity = 1 - (V_material / V_total)

    For a binary voxel grid (1 = material, 0 = pore), this simplifies to
    the mean of the "pore" voxels:
        porosity = 1 - mean(grid)

    Specific surface area (SSA) approximates the pore-material interface.
    On a voxel grid, it is the total number of voxel faces shared between
    material and pore voxels, normalized by total volume. Faces are counted
    by taking the absolute finite difference along each axis.

    Degradation is modelled as a stochastic surface erosion process: at
    each iteration, surface material voxels are removed with probability p.
    Porosity increases monotonically as material is lost.
    """)

    rng = np.random.default_rng(1)
    scaffold = (rng.random((50, 50, 50)) > 0.7).astype(int)

    porosity = 1 - scaffold.mean()
    print(f"Porosity: {porosity:.3f}")

    padded = np.pad(scaffold, 1, constant_values=0)
    faces = 0
    for axis in range(3):
        faces += np.abs(np.diff(padded, axis=axis)).sum()
    ssa = faces / scaffold.size
    print(f"Specific surface area: {ssa:.4f} per voxel")

    s = scaffold.copy()
    porosities = [1 - s.mean()]
    for _ in range(20):
        erode_mask = (rng.random(s.shape) < 0.1) & (s == 1)
        s[erode_mask] = 0
        porosities.append(1 - s.mean())

    plt.figure()
    plt.plot(porosities, marker="o")
    plt.xlabel("Iteration")
    plt.ylabel("Porosity")
    plt.title("Scaffold Degradation")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ex6_porosity.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 7: Gene Expression Analysis (qPCR)
# ===========================================================================
def exercise_7():
    banner("Exercise 7: qPCR Relative Gene Expression")

    theory("""
    Quantitative PCR measures the cycle threshold (Ct) at which a
    fluorescent signal crosses a fixed baseline. Lower Ct = more starting
    template = higher expression.

    The comparative Ct (2^-dCt) method:
        dCt = Ct_target - Ct_housekeeping
        relative expression = 2^(-dCt)

    Assumptions:
        - Amplification efficiency = 2 (perfect doubling per cycle).
        - Housekeeping gene (e.g., GAPDH) is stably expressed across
          samples and serves as an internal control.

    Technical replicates (e.g., triplicate wells) are averaged first;
    biological replicates (donors) are then used to compute mean +/- SD.
    """)

    genes = ["COL1A1", "SOX9", "RUNX2"]
    Ct = np.array([
        [[22.1, 22.3, 22.0], [23.0, 23.2, 22.9], [22.5, 22.6, 22.4], [22.8, 22.7, 22.9]],
        [[26.5, 26.7, 26.4], [27.0, 27.2, 26.9], [26.8, 26.9, 26.7], [27.1, 27.0, 27.2]],
        [[28.0, 28.2, 27.9], [28.5, 28.6, 28.4], [28.1, 28.0, 28.2], [28.3, 28.4, 28.5]],
    ])

    Ct_mean = Ct.mean(axis=2)
    dCt = Ct_mean - 20.0
    rel_expr = 2 ** (-dCt)

    for i, g in enumerate(genes):
        print(f"{g}: {rel_expr[i].mean():.2e} +/- {rel_expr[i].std(ddof=1):.2e}")

    most = genes[int(np.argmax(rel_expr.mean(axis=1)))]
    print(f"Most expressed: {most}")

    plt.figure()
    means = rel_expr.mean(axis=1)
    errs = rel_expr.std(axis=1, ddof=1)
    plt.bar(genes, means, yerr=errs, capsize=6)
    plt.ylabel("Relative expression (2^-dCt)")
    plt.title("qPCR Gene Expression")
    plt.grid(True, axis="y")
    plt.tight_layout()
    plt.savefig("ex7_qpcr.png", dpi=120)
    plt.close()


# ===========================================================================
# Exercise 8: Bone Remodeling Simulation
# ===========================================================================
def exercise_8():
    banner("Exercise 8: Bone Remodeling Simulation")

    theory("""
    Bone is a living tissue that continuously adapts its density in
    response to mechanical loading (Wolff's law). A common continuum
    model (Huiskes-style) uses strain energy density U as the mechanical
    stimulus:

        d(rho)/dt = B * (U / rho - U_ref)

    where:
        rho    = bone apparent density (g/cm^3)
        B      = remodeling rate constant
        U      = strain energy density (Mechanical stimulus)
        U_ref  = homeostatic setpoint

    Interpretation:
        - If U/rho > U_ref  ->  bone apposition (density increases)
        - If U/rho < U_ref  ->  bone resorption (density decreases)

    Density is clamped to a physiological range:
        0.1 <= rho <= 1.8 g/cm^3
    corresponding to trabecular and cortical bone limits.
    """)

    N = 100
    rho = np.ones((N, N))
    x, y = np.meshgrid(np.linspace(0, 1, N), np.linspace(0, 1, N))
    U = 0.5 * np.sin(np.pi * x) * np.cos(np.pi * y) + 0.6

    B, dt, U_ref = 0.02, 0.1, 0.5
    for _ in range(500):
        drho = B * (U / rho - U_ref) * dt
        rho = np.clip(rho + drho, 0.1, 1.8)

    apposition = int((rho > 1).sum())
    resorption = int((rho < 1).sum())
    print(f"Apposition (rho>1): {apposition} voxels")
    print(f"Resorption (rho<1): {resorption} voxels")

    plt.figure()
    im = plt.imshow(rho, cmap="bone")
    plt.colorbar(im, label="rho (g/cm^3)")
    plt.title("Bone Density Distribution")
    plt.tight_layout()
    plt.savefig("ex8_bone.png", dpi=120)
    plt.close()


# ===========================================================================
# Main
# ===========================================================================
def main():
    print("NumPy Exercises for Tissue Engineering Master's Students")
    print("Note: figures are saved as PNG files in the current directory.")

    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()

    print("\nAll exercises completed. Figures saved as ex*.png")


if __name__ == "__main__":
    main()
