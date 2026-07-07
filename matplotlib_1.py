"""
Matplotlib Masterclass for Tissue Engineering MSc Students (FHTW)

Learning objectives:
- Create publication-quality scientific figures
- Visualize biological experiments
- Plot growth curves
- Compare biomaterials
- Display experimental variability
- Create heatmaps and histograms
- Prepare figures for reports and publications

Requirements:
    pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------
# 1. Basic scientific plotting: Cell proliferation curve
# -------------------------------------------------------

days = np.array([0, 1, 3, 5, 7, 10, 14])

# Example: normalized metabolic activity from tissue scaffold experiment
cells_scaffold_A = np.array([1.0, 1.3, 2.0, 3.5, 5.2, 7.8, 10.5])
cells_scaffold_B = np.array([1.0, 1.2, 1.8, 2.8, 3.9, 5.0, 6.2])


plt.figure(figsize=(8, 5))

plt.plot(
    days,
    cells_scaffold_A,
    marker="o",
    linewidth=2,
    label="Collagen scaffold"
)

plt.plot(
    days,
    cells_scaffold_B,
    marker="s",
    linewidth=2,
    label="PLGA scaffold"
)

plt.xlabel("Culture time (days)")
plt.ylabel("Normalized cell activity")
plt.title("Cell proliferation on biomaterial scaffolds")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# -------------------------------------------------------
# 2. Experimental uncertainty: Error bars
# -------------------------------------------------------

time = np.array([1, 3, 5, 7, 14])

mean_viability = np.array([95, 93, 91, 88, 85])
std_viability = np.array([3, 4, 5, 4, 6])


plt.figure(figsize=(7, 5))

plt.errorbar(
    time,
    mean_viability,
    yerr=std_viability,
    marker="o",
    capsize=5,
    linewidth=2
)

plt.xlabel("Culture duration (days)")
plt.ylabel("Cell viability (%)")

plt.title("Viability assay with biological variation")

plt.grid(True)

plt.tight_layout()
plt.show()



# -------------------------------------------------------
# 3. Scatter plot: Material properties vs cell response
# -------------------------------------------------------

porosity = np.array([40, 50, 60, 70, 80, 90])

cell_attachment = np.array([35, 45, 55, 70, 82, 90])


plt.figure(figsize=(7, 5))

plt.scatter(
    porosity,
    cell_attachment,
    s=120
)

plt.xlabel("Scaffold porosity (%)")
plt.ylabel("Cell attachment (%)")

plt.title("Relationship between scaffold design and cell response")

plt.grid(True)

plt.tight_layout()
plt.show()



# -------------------------------------------------------
# 4. Histogram: Cell size distribution
# -------------------------------------------------------

cell_sizes = np.random.normal(
    loc=18,
    scale=3,
    size=500
)

plt.figure(figsize=(7, 5))

plt.hist(
    cell_sizes,
    bins=25
)

plt.xlabel("Cell diameter (µm)")
plt.ylabel("Frequency")

plt.title("Distribution of measured cell sizes")

plt.tight_layout()
plt.show()



# -------------------------------------------------------
# 5. Heatmap: Gene expression experiment
# -------------------------------------------------------

genes = [
    "COL1A1",
    "RUNX2",
    "SOX9",
    "ALPL",
    "VEGF"
]

samples = [
    "Day 1",
    "Day 7",
    "Day 14",
    "Day 21"
]


expression = np.array([
    [1.2, 2.4, 4.0, 5.5],
    [0.8, 1.5, 3.2, 4.8],
    [2.0, 3.5, 5.0, 6.2],
    [1.0, 2.2, 3.8, 5.0],
    [3.0, 4.5, 6.0, 7.2]
])


plt.figure(figsize=(8, 5))

plt.imshow(
    expression,
    aspect="auto"
)

plt.colorbar(
    label="Relative expression"
)

plt.xticks(
    range(len(samples)),
    samples
)

plt.yticks(
    range(len(genes)),
    genes
)

plt.title("Gene expression during tissue maturation")

plt.tight_layout()
plt.show()



# -------------------------------------------------------
# 6. Scientific figure panels using subplots
# -------------------------------------------------------

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 4)
)


# Panel A
axes[0].plot(days, cells_scaffold_A)
axes[0].set_title("Growth curve")
axes[0].set_xlabel("Days")
axes[0].set_ylabel("Activity")


# Panel B
axes[1].scatter(
    porosity,
    cell_attachment
)
axes[1].set_title("Material-cell interaction")
axes[1].set_xlabel("Porosity")
axes[1].set_ylabel("Attachment")


# Panel C
axes[2].hist(cell_sizes, bins=20)
axes[2].set_title("Cell distribution")
axes[2].set_xlabel("Diameter")


plt.suptitle(
    "Tissue Engineering Experimental Data Visualization",
    fontsize=14
)

plt.tight_layout()

plt.show()



# -------------------------------------------------------
# 7. Saving publication-quality figures
# -------------------------------------------------------

plt.figure(figsize=(6,4))

plt.plot(
    days,
    cells_scaffold_A,
    marker="o"
)

plt.xlabel("Days")
plt.ylabel("Cell activity")

plt.title(
    "Example publication figure"
)

plt.savefig(
    "tissue_engineering_matplotlib_example.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print(
    """
Matplotlib masterclass completed.

Students learned:
✓ line plots
✓ scatter plots
✓ error visualization
✓ distributions
✓ heatmaps
✓ multi-panel scientific figures
✓ publication-quality export

Recommended next steps:
- add pandas for experimental datasets
- add scipy for statistics
- add seaborn for advanced visualization
- integrate plots into Jupyter notebooks
"""
)