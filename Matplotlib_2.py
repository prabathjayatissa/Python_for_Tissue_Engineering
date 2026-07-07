"""
Matplotlib Masterclass 02
Advanced Scientific Visualization for Tissue Engineering MSc Students

Topics:
- Biomaterial comparison plots
- Cell viability experiments
- Dose-response curves
- Differentiation markers
- Mechanical testing visualization
- 3D scaffold pore analysis
- Microscopy image quantification
- Publication-style figures

Requirements:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt


# =====================================================
# 1. Biomaterial comparison: Bar charts
# =====================================================

materials = [
    "Collagen",
    "GelMA",
    "PLGA",
    "PCL"
]

cell_viability = [
    92,
    96,
    85,
    78
]

plt.figure(figsize=(7,5))

plt.bar(
    materials,
    cell_viability
)

plt.ylabel("Cell viability (%)")
plt.xlabel("Biomaterial")

plt.title(
    "Comparison of scaffold biocompatibility"
)

plt.ylim(0,100)

plt.grid(
    axis="y"
)

plt.tight_layout()
plt.show()



# =====================================================
# 2. Dose-response curve
# Example: Growth factor concentration effect
# =====================================================

concentration = np.array(
    [0, 1, 5, 10, 25, 50, 100]
)

growth_response = np.array(
    [20, 30, 48, 65, 80, 88, 91]
)


plt.figure(figsize=(7,5))

plt.plot(
    concentration,
    growth_response,
    marker="o",
    linewidth=2
)

plt.xlabel(
    "Growth factor concentration (ng/mL)"
)

plt.ylabel(
    "Cell proliferation (%)"
)

plt.title(
    "Dose-response relationship"
)

plt.grid(True)

plt.tight_layout()

plt.show()



# =====================================================
# 3. Osteogenic differentiation assay
# =====================================================

days = np.array(
    [0,7,14,21,28]
)

alp_activity = np.array(
    [10,25,50,80,120]
)

calcium_deposition = np.array(
    [5,20,45,90,150]
)


plt.figure(figsize=(8,5))


plt.plot(
    days,
    alp_activity,
    marker="o",
    label="ALP activity"
)


plt.plot(
    days,
    calcium_deposition,
    marker="s",
    label="Calcium deposition"
)


plt.xlabel(
    "Differentiation time (days)"
)

plt.ylabel(
    "Relative signal"
)

plt.title(
    "Stem cell osteogenic differentiation"
)

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()



# =====================================================
# 4. Mechanical testing: Stress-strain curve
# =====================================================

strain = np.linspace(
    0,
    50,
    100
)


stress = (
    0.8 * strain
    +
    0.02 * strain**2
)


plt.figure(figsize=(7,5))


plt.plot(
    strain,
    stress,
    linewidth=2
)


plt.xlabel(
    "Strain (%)"
)

plt.ylabel(
    "Stress (kPa)"
)

plt.title(
    "Hydrogel mechanical characterization"
)

plt.grid(True)

plt.tight_layout()

plt.show()



# =====================================================
# 5. Scaffold pore size analysis
# =====================================================

pore_sizes = np.random.normal(
    150,
    30,
    300
)


plt.figure(figsize=(7,5))


plt.hist(
    pore_sizes,
    bins=30
)


plt.xlabel(
    "Pore diameter (µm)"
)

plt.ylabel(
    "Number of pores"
)


plt.title(
    "3D scaffold pore size distribution"
)


plt.tight_layout()

plt.show()



# =====================================================
# 6. Microscopy quantification scatter plot
# =====================================================

cell_number = np.array(
    [50,80,120,160,200,250]
)

fluorescence = np.array(
    [10,18,30,42,55,70]
)


plt.figure(figsize=(7,5))


plt.scatter(
    cell_number,
    fluorescence,
    s=120
)


plt.xlabel(
    "Number of cells per image"
)

plt.ylabel(
    "Fluorescence intensity"
)

plt.title(
    "Microscopy image quantification"
)


plt.grid(True)

plt.tight_layout()

plt.show()



# =====================================================
# 7. Multi-panel figure like a journal article
# =====================================================


fig, axes = plt.subplots(
    2,
    2,
    figsize=(10,8)
)


# Panel A
axes[0,0].bar(
    materials,
    cell_viability
)

axes[0,0].set_title(
    "Viability"
)


# Panel B
axes[0,1].plot(
    concentration,
    growth_response,
    marker="o"
)

axes[0,1].set_title(
    "Dose response"
)


# Panel C
axes[1,0].plot(
    strain,
    stress
)

axes[1,0].set_title(
    "Mechanical testing"
)


# Panel D
axes[1,1].hist(
    pore_sizes,
    bins=20
)

axes[1,1].set_title(
    "Pore distribution"
)


fig.suptitle(
    "Tissue Engineering Experimental Summary Figure",
    fontsize=15
)


plt.tight_layout()

plt.show()



# =====================================================
# 8. Exporting scientific figures
# =====================================================


plt.figure(figsize=(6,4))


plt.plot(
    days,
    calcium_deposition,
    marker="o"
)


plt.xlabel(
    "Days"
)

plt.ylabel(
    "Calcium deposition"
)

plt.title(
    "Differentiation result"
)


plt.savefig(
    "differentiation_assay_result.png",
    dpi=300,
    bbox_inches="tight"
)


plt.close()



print(
"""
Advanced Matplotlib tissue engineering lesson completed.

Students practiced:

✓ biomaterial comparison
✓ biological assay visualization
✓ dose-response analysis
✓ differentiation kinetics
✓ mechanical testing plots
✓ scaffold morphology statistics
✓ microscopy quantification
✓ journal-style figure layouts
✓ high-resolution export

Suggested next topics:
- pandas for reading Excel/CSV laboratory data
- scipy for statistical testing
- image processing with OpenCV
- machine learning visualization
"""
)