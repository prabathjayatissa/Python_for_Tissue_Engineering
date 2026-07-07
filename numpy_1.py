"""
==============================================================
NUMPY MASTERCLASS
For MSc Tissue Engineering Students (FHTW)

Author: Dr Prabath Jayathissa
Run section by section.

==============================================================
"""

import numpy as np
import time

np.set_printoptions(precision=3, suppress=True)

print("="*70)
print("NUMPY MASTERCLASS FOR TISSUE ENGINEERING")
print("="*70)

##########################################################################
# 1. WHAT IS NUMPY?
##########################################################################

print("\nSECTION 1 - Creating Arrays")

cells = np.array([100,120,135,160,180])

print("Cell counts")
print(cells)

print("dtype =", cells.dtype)
print("shape =", cells.shape)
print("size =", cells.size)

##########################################################################
# 2. ARRAY CREATION
##########################################################################

print("\nSECTION 2 - Array Creation")

zeros = np.zeros((3,4))
ones = np.ones((2,5))
identity = np.eye(4)
sequence = np.arange(0,10)
linspace = np.linspace(0,1,11)

print("Zeros")
print(zeros)

print("Identity")
print(identity)

print("Linspace")
print(linspace)

##########################################################################
# 3. DIMENSIONS
##########################################################################

print("\nSECTION 3 - Dimensions")

scaffold = np.array([
    [80,85,90],
    [88,93,98],
    [100,104,108]
])

print(scaffold)

print("Rows:", scaffold.shape[0])
print("Columns:", scaffold.shape[1])

##########################################################################
# 4. INDEXING
##########################################################################

print("\nSECTION 4 - Indexing")

print(scaffold[0,0])
print(scaffold[2,1])

##########################################################################
# 5. SLICING
##########################################################################

print("\nSECTION 5 - Slicing")

print(scaffold[:2])

print(scaffold[:,1])

##########################################################################
# 6. RESHAPING
##########################################################################

print("\nSECTION 6 - Reshape")

data = np.arange(24)

cube = data.reshape((2,3,4))

print(cube)

##########################################################################
# 7. VECTOR OPERATIONS
##########################################################################

print("\nSECTION 7 - Vector Operations")

day1 = np.array([120,140,160])
day2 = np.array([150,175,210])

growth = day2-day1

print(growth)

##########################################################################
# 8. ELEMENTWISE MATH
##########################################################################

print("\nSECTION 8")

strain = np.array([0.01,0.02,0.03])

stress = np.array([12,25,37])

modulus = stress/strain

print(modulus)

##########################################################################
# 9. BROADCASTING
##########################################################################

print("\nSECTION 9 - Broadcasting")

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matrix+10)

##########################################################################
# 10. BOOLEAN MASKING
##########################################################################

print("\nSECTION 10")

viability = np.array([95,91,87,72,99,63])

healthy = viability>90

print(healthy)

print(viability[healthy])

##########################################################################
# 11. WHERE
##########################################################################

print("\nSECTION 11")

classification = np.where(
    viability>90,
    "Healthy",
    "Needs Review"
)

print(classification)

##########################################################################
# 12. STATISTICS
##########################################################################

print("\nSECTION 12")

measurements = np.array([
    101,
    98,
    110,
    103,
    107,
    95,
    100
])

print("Mean",np.mean(measurements))
print("Median",np.median(measurements))
print("Std",np.std(measurements))
print("Variance",np.var(measurements))
print("Min",np.min(measurements))
print("Max",np.max(measurements))

##########################################################################
# 13. RANDOM NUMBERS
##########################################################################

print("\nSECTION 13")

np.random.seed(42)

cells = np.random.normal(
    loc=100,
    scale=8,
    size=20
)

print(cells)

##########################################################################
# 14. HISTOGRAM DATA
##########################################################################

print("\nSECTION 14")

hist,bins = np.histogram(cells,bins=5)

print(hist)
print(bins)

##########################################################################
# 15. MATRIX OPERATIONS
##########################################################################

print("\nSECTION 15")

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A+B)

print(A*B)

print(A@B)

##########################################################################
# 16. LINEAR ALGEBRA
##########################################################################

print("\nSECTION 16")

print(np.linalg.det(A))

print(np.linalg.inv(A))

print(np.linalg.eig(A))

##########################################################################
# 17. SOLVING SYSTEMS
##########################################################################

print("\nSECTION 17")

A = np.array([
    [3,2],
    [1,2]
])

b = np.array([18,10])

x = np.linalg.solve(A,b)

print(x)

##########################################################################
# 18. BIOMECHANICS
##########################################################################

print("\nSECTION 18")

force = np.array([5,10,15,20])

area = 2.5

stress = force/area

print(stress)

##########################################################################
# 19. STRAIN ENERGY
##########################################################################

print("\nSECTION 19")

strain = np.linspace(0,0.1,10)

stress = 500*strain

energy = np.trapz(stress,strain)

print(energy)

##########################################################################
# 20. DIFFUSION
##########################################################################

print("\nSECTION 20")

x = np.linspace(0,10,100)

oxygen = np.exp(-0.35*x)

print(oxygen[:10])

##########################################################################
# 21. IMAGE PROCESSING
##########################################################################

print("\nSECTION 21")

image = np.random.randint(
    0,
    255,
    (8,8)
)

print(image)

binary = image>120

print(binary.astype(int))

##########################################################################
# 22. 3D MRI VOLUME
##########################################################################

print("\nSECTION 22")

volume = np.random.rand(30,30,30)

print(volume.shape)

##########################################################################
# 23. PCA PREPARATION
##########################################################################

print("\nSECTION 23")

data = np.random.rand(50,5)

centered = data-np.mean(data,axis=0)

cov = np.cov(centered.T)

print(cov)

##########################################################################
# 24. EIGENVALUES
##########################################################################

print("\nSECTION 24")

values,vectors=np.linalg.eig(cov)

print(values)

##########################################################################
# 25. PERFORMANCE
##########################################################################

print("\nSECTION 25")

N=2_000_000

a=np.random.rand(N)
b=np.random.rand(N)

t=time.time()
c=a+b
numpy_time=time.time()-t

print("NumPy time:",numpy_time)

##########################################################################
# 26. LOOP COMPARISON
##########################################################################

print("\nSECTION 26")

listA=list(a)
listB=list(b)

t=time.time()

result=[]

for i in range(N):
    result.append(listA[i]+listB[i])

python_time=time.time()-t

print("Python time:",python_time)

print("Speedup =",python_time/numpy_time)

##########################################################################
# 27. EXAMPLE:
# CELL PROLIFERATION
##########################################################################

print("\nSECTION 27")

days=np.arange(1,8)

counts=np.array([
    100,
    132,
    165,
    220,
    295,
    385,
    480
])

growth=np.diff(counts)

print(days)
print(counts)
print(growth)

##########################################################################
# 28. EXAMPLE:
# POROSITY
##########################################################################

print("\nSECTION 28")

pores=np.random.normal(
    150,
    18,
    1000
)

print(np.mean(pores))
print(np.std(pores))

##########################################################################
# 29. EXAMPLE:
# YOUNG'S MODULUS
##########################################################################

print("\nSECTION 29")

stress=np.linspace(0,40,20)
strain=stress/600

E=np.polyfit(strain,stress,1)

print("Young's modulus")
print(E[0])

##########################################################################
# 30. ADVANCED BROADCASTING
##########################################################################

print("\nSECTION 30")

cells=np.random.randint(
    80,
    120,
    (6,5)
)

factors=np.array([
    1.0,
    1.05,
    1.10,
    0.98,
    1.12
])

adjusted=cells*factors

print(adjusted)

##########################################################################
# 31. NAN HANDLING
##########################################################################

print("\nSECTION 31")

data=np.array([
    10,
    11,
    np.nan,
    13,
    14
])

print(np.nanmean(data))
print(np.nanstd(data))

##########################################################################
# 32. SAVE DATA
##########################################################################

print("\nSECTION 32")

np.save("cells.npy",cells)

loaded=np.load("cells.npy")

print(loaded)

##########################################################################
# 33. CSV
##########################################################################

print("\nSECTION 33")

np.savetxt(
    "cell_counts.csv",
    cells,
    delimiter=",",
    fmt="%.2f"
)

##########################################################################
# 34. EXERCISES
##########################################################################

print("\nSECTION 34 - Exercises")

print("""
Exercise 1
----------
Create a 10x10 identity matrix.

Exercise 2
----------
Generate 1000 normally distributed scaffold pore sizes.

Exercise 3
----------
Compute mean, std, median.

Exercise 4
----------
Threshold MRI pixels >150.

Exercise 5
----------
Compute stress from force and area.

Exercise 6
----------
Compute Young's modulus.

Exercise 7
----------
Normalize gene expression matrix.

Exercise 8
----------
Simulate oxygen diffusion.

Exercise 9
----------
Create random 3D scaffold.

Exercise 10
-----------
Compute covariance matrix and eigenvalues.
""")

##########################################################################
# 35. SUMMARY
##########################################################################

print("\nSUMMARY")

topics=[
"Arrays",
"Indexing",
"Slicing",
"Broadcasting",
"Statistics",
"Random numbers",
"Linear Algebra",
"Mechanical Testing",
"Image Processing",
"Diffusion",
"PCA Preparation",
"Performance",
"Saving Files"
]

for i,t in enumerate(topics,1):
    print(f"{i:02d}. {t}")

print("\nCongratulations!")
print("You have completed the NumPy Masterclass for Tissue Engineering.")