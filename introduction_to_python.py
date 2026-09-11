"""
MSTE WS26 | Introduction to Python
Fundamentals for Beginners and Data-Driven Applications

Dr. Prabath Jayathissa
MBBS, MSc(BI), MSc(CS), MD(Health Informatics)
UAS Technikum Wien
2026

Converted from the original Marp lecture slides into a runnable Python file.

Run:
    python introduction_to_python.py

This script demonstrates the main Python concepts from the lecture.
"""

# =============================================================================
# 1. INSTALLATION & SETUP
# =============================================================================
#
# Windows:
#   1. Install Python 3.10+ from https://www.python.org/
#   2. Check "Add Python to PATH"
#   3. Verify:
#          python --version
#          pip --version
#
# Recommended IDEs:
#   - VS Code + Python/Jupyter extensions
#   - PyCharm
#
# Jupyter:
#   jupyter notebook


# =============================================================================
# 2. PYTHON REPL & SCRIPTS
# =============================================================================

def demo_repl():
    """Basic examples that can also be tried in the Python REPL."""
    print("2 + 2 =", 2 + 2)
    print("Hello")


# =============================================================================
# 3. VARIABLES & DATA TYPES
# =============================================================================

def demo_variables():
    name = "Dr. Jayathissa"
    institution = "Technikum Wien"

    age = 42
    height = 1.75
    pi = 3.14159

    is_professor = True
    is_weekend = False

    print(f"Name: {name}, Age: {age}")
    print("Name: " + name + ", Age: " + str(age))
    print(f"Institution: {institution}")
    print(f"Height: {height} m")
    print(f"Professor: {is_professor}")
    print(f"Weekend: {is_weekend}")

    print("\nData types:")
    for value in [age, height, name, is_professor]:
        print(f"{value!r} -> {type(value).__name__}")


# Common Python data types:
# int      -> 42
# float    -> 3.14
# str      -> "text"
# bool     -> True / False
# list     -> [1, 2, 3]
# tuple    -> (1, 2, 3)
# dict     -> {"key": "value"}
# set      -> {1, 2, 3}


# =============================================================================
# 4. ARITHMETIC OPERATIONS
# =============================================================================

def demo_arithmetic():
    a = 10
    b = 3

    print("\nArithmetic:")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Integer division:", a // b)
    print("Modulo:", a % b)
    print("Exponentiation:", a ** b)

    x = 5
    x += 3
    print("x += 3:", x)
    x -= 2
    print("x -= 2:", x)
    x *= 2
    print("x *= 2:", x)
    x /= 3
    print("x /= 3:", x)


# =============================================================================
# 5. STRING OPERATIONS
# =============================================================================

def demo_strings():
    text = "Python Programming"

    print("\nString operations:")
    print("Length:", len(text))
    print("First character:", text[0])
    print("Last character:", text[-1])
    print("First six:", text[0:6])
    print("From index 7:", text[7:])
    print("Every second character:", text[::2])
    print("Lowercase:", text.lower())
    print("Uppercase:", text.upper())

    words = text.split()
    joined = "-".join(words)

    print("Words:", words)
    print("Joined:", joined)


# =============================================================================
# 6. LISTS
# =============================================================================

def demo_lists():
    genes = ["COL1A1", "VEGF", "MMP2", "IL-6"]

    print("\nOriginal genes:", genes)
    print("First gene:", genes[0])
    print("Last gene:", genes[-1])

    genes[0] = "Collagen"
    genes.append("TNF-alpha")
    genes.insert(1, "FGF2")
    genes.remove("IL-6")

    popped = genes.pop()

    print("After modifications:", genes)
    print("Popped item:", popped)
    print("Number of genes:", len(genes))
    print("VEGF present:", "VEGF" in genes)


def demo_list_methods():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]

    print("\nList methods:")
    print("Original:", numbers)
    print("Sorted copy:", sorted(numbers))

    numbers.sort()
    numbers.reverse()

    print("After sort + reverse:", numbers)
    print("Count of 1:", numbers.count(1))
    print("Index of 4:", numbers.index(4))


# =============================================================================
# 7. DICTIONARIES
# =============================================================================

def demo_dictionaries():
    patient = {
        "id": "P001",
        "name": "Anna Müller",
        "age": 35,
        "tissue_type": "skin",
        "recovery_days": 14,
    }

    print("\nPatient dictionary:")
    print("Name:", patient["name"])
    print("Age:", patient.get("age"))
    print("Email:", patient.get("email", "N/A"))

    patient["age"] = 36
    patient["status"] = "healing"

    del patient["recovery_days"]
    removed = patient.pop("status")

    print("Removed status:", removed)

    print("\nIterating through patient:")
    for key, value in patient.items():
        print(f"{key}: {value}")

    print("Keys:", list(patient.keys()))
    print("Values:", list(patient.values()))


# =============================================================================
# 8. CONDITIONAL STATEMENTS
# =============================================================================

def demo_conditionals():
    age = 45
    cell_count = 2_500_000

    print("\nConditionals:")

    if age >= 18:
        print("Adult")

    if cell_count > 3_000_000:
        print("Excellent cell viability")
    else:
        print("Low cell count")

    if cell_count < 500_000:
        print("Critical: Cell viability issue")
    elif cell_count < 1_000_000:
        print("Warning: Low cell count")
    else:
        print("Cell count acceptable")


def demo_comparison_operators():
    a, b = 10, 5

    print("\nComparison operators:")
    print("a == b:", a == b)
    print("a != b:", a != b)
    print("a > b:", a > b)
    print("a < b:", a < b)
    print("a >= 10:", a >= 10)
    print("a <= 10:", a <= 10)


def demo_logical_operators():
    age = 30
    has_degree = True
    experience_years = 5

    print("\nLogical operators:")

    if age > 25 and has_degree:
        print("Eligible for senior position")

    if experience_years < 2 or age < 25:
        print("Entry-level candidate")

    if not has_degree:
        print("Degree required")


# =============================================================================
# 9. LOOPS
# =============================================================================

def demo_for_loops():
    genes = ["COL1A1", "VEGF", "MMP2"]

    print("\nFor loop:")
    for gene in genes:
        print(f"Gene: {gene}")

    print("\nFor loop with index:")
    for i, gene in enumerate(genes):
        print(f"{i + 1}. {gene}")

    print("\nRange:")
    for day in range(1, 6):
        print(f"Day {day}: Culture growing")

    patient = {"name": "Anna", "age": 35}

    print("\nDictionary loop:")
    for key, value in patient.items():
        print(f"{key}: {value}")


def demo_while_loops():
    print("\nWhile loop:")
    count = 0

    while count < 5:
        print(f"Culture day {count + 1}")
        count += 1

    print("\nWhile loop with break and continue:")
    day = 0

    while day < 10:
        day += 1

        if day == 3:
            continue

        if day == 8:
            break

        print(f"Day {day}: Monitoring")


def demo_loop_control():
    print("\nbreak:")
    for i in range(10):
        if i == 5:
            break
        print(i)

    print("\ncontinue:")
    for i in range(5):
        if i == 2:
            continue
        print(i)


# =============================================================================
# 10. FUNCTIONS
# =============================================================================

def greet(name):
    return f"Hello, {name}!"


def calculate_cell_count(initial_count, doubling_time, hours):
    """Calculate cell count using a simple exponential doubling model."""
    doublings = hours / doubling_time
    final_count = initial_count * (2 ** doublings)
    return final_count


def create_experiment(name, duration=14, replicates=3):
    return f"{name}: {duration} days, {replicates} replicates"


def divide(a, b):
    return a / b


def get_patient_info():
    return "Anna", 35, "skin"


def print_status(status):
    print(f"Status: {status}")


def demo_functions():
    print("\nFunctions:")

    message = greet("Dr. Jayathissa")
    print(message)

    cells = calculate_cell_count(1_000_000, 24, 48)
    print(f"After 48 hours: {cells:,.0f} cells")

    print(create_experiment("Cell culture"))
    print(create_experiment("Scaffold test", 21, 5))

    print("Division:", divide(10, 2))

    name, age, tissue = get_patient_info()
    print(f"Patient: {name}, age {age}, tissue {tissue}")

    result = print_status("Growing")
    print("Return value:", result)


# =============================================================================
# 11. WORKING WITH LIBRARIES
# =============================================================================

def demo_standard_library():
    import math
    from datetime import datetime

    print("\nStandard library:")
    print("sqrt(16):", math.sqrt(16))
    print("pi:", math.pi)
    print("sin(pi/2):", math.sin(math.pi / 2))
    print("Current date/time:", datetime.now())


def demo_optional_data_science_libraries():
    """
    Demonstrates NumPy, pandas and matplotlib imports.

    These packages are optional for this basic script.

    Install with:
        pip install numpy pandas matplotlib
    """
    try:
        import numpy as np

        arr = np.array([1, 2, 3, 4, 5])
        print("\nNumPy:")
        print("Array:", arr)
        print("Mean:", np.mean(arr))
        print("Standard deviation:", np.std(arr))
    except ImportError:
        print("\nNumPy is not installed.")
        print("Install it with: pip install numpy")

    try:
        import pandas as pd

        data = pd.DataFrame(
            {
                "gene": ["COL1A1", "VEGF", "MMP2"],
                "expression": [10.2, 7.5, 4.8],
            }
        )
        print("\nPandas DataFrame:")
        print(data)
    except ImportError:
        print("\npandas is not installed.")
        print("Install it with: pip install pandas")


# =============================================================================
# 12. BEST PRACTICES / PEP 8
# =============================================================================

def calculate_viability(live_cells, total_cells):
    """Calculate percentage cell viability."""
    if total_cells == 0:
        raise ValueError("Total cell count cannot be zero.")
    return (live_cells / total_cells) * 100


def demo_pep8():
    patient_age = 35
    cell_count = 2_500_000

    viability = calculate_viability(2_000_000, cell_count)

    print("\nPEP 8 example:")
    print(f"Patient age: {patient_age}")
    print(f"Cell count: {cell_count:,}")
    print(f"Viability: {viability:.1f}%")


# =============================================================================
# 13. COMMENTS AND DOCUMENTATION
# =============================================================================

def logistic_growth(t, K, r):
    """
    Calculate cell count at time t using a logistic growth model.

    Parameters
    ----------
    t : float
        Time in hours.
    K : float
        Maximum cell count (carrying capacity).
    r : float
        Growth-rate parameter.

    Returns
    -------
    float
        Cell count at time t.
    """
    import math

    return K / (1 + math.exp(-r * t))


def demo_documentation():
    print("\nLogistic growth example:")

    for t in [0, 2, 4, 6, 8]:
        cells = logistic_growth(t, K=1_000_000, r=0.5)
        print(f"t={t:>2} h -> {cells:,.0f} cells")


# =============================================================================
# 14. COMMON MISTAKES & DEBUGGING
# =============================================================================

def demo_indexing():
    genes = ["COL1A1", "VEGF", "MMP2"]

    print("\n0-based indexing:")
    print("First gene:", genes[0])
    print("Third gene:", genes[2])

    # The following would raise IndexError:
    # print(genes[3])


def add_to_list(item, items=None):
    """
    Correct approach for a mutable default argument.

    Avoid:
        def add_to_list(item, items=[]):
            ...
    """
    if items is None:
        items = []

    items.append(item)
    return items


def demo_mutable_defaults():
    print("\nMutable default argument:")
    list1 = add_to_list(1)
    list2 = add_to_list(2)

    print("list1:", list1)
    print("list2:", list2)


def demo_type_conversion():
    age = "35"

    # Wrong:
    # new_age = age + 1
    #
    # Correct:
    age = int(age)
    new_age = age + 1

    print("\nType conversion:")
    print("Next year:", new_age)


def process_data():
    x = 10
    return x


def demo_scope():
    result = process_data()

    print("\nVariable scope:")
    print("Returned result:", result)

    # x is local to process_data() and is not available here.
    # print(x)  # Would raise NameError.


# =============================================================================
# 15. ERROR HANDLING
# =============================================================================

def demo_error_handling():
    print("\nError handling:")

    try:
        count = int("not a number")
    except ValueError:
        print("Invalid number format")

    try:
        data = [1, 2, 3]
        print(data[10])
    except IndexError:
        print("Index out of range")
    except TypeError:
        print("Type error occurred")

    try:
        with open("nonexistent.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as exc:
        print(f"File not found: {exc}")
    finally:
        print("Cleanup code runs regardless")


# =============================================================================
# 16. INPUT / OUTPUT
# =============================================================================

def demo_input():
    """
    Uncomment the input examples when running interactively.

    They are kept in a function so the main lecture demonstration does not
    pause waiting for keyboard input.
    """
    # name = input("Enter your name: ")
    # print(f"Hello, {name}!")

    # age_str = input("Enter your age: ")
    # age = int(age_str)
    # print(f"Next year you'll be {age + 1}")

    print("\nInput examples are commented out.")
    print("Uncomment them when interactive input is desired.")


def demo_file_operations():
    filename = "experiment_demo.txt"

    # Write to a file.
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Day 1: Initial measurement\n")
        file.write("Day 2: Cell culture growing\n")

    # Read the file.
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print("\nFile content:")
    print(content)

    # Read line by line.
    print("Line by line:")
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

    # Remove demonstration file after use.
    from pathlib import Path

    Path(filename).unlink(missing_ok=True)


# =============================================================================
# 17. BEGINNER PROJECT EXAMPLE: CELL VIABILITY CALCULATOR
# =============================================================================

def cell_viability_calculator():
    """
    A small example combining variables, functions, conditionals and output.
    """
    live_cells = 2_000_000
    total_cells = 2_500_000

    viability = calculate_viability(live_cells, total_cells)

    print("\nCell Viability Calculator")
    print("-" * 30)
    print(f"Live cells : {live_cells:,}")
    print(f"Total cells: {total_cells:,}")
    print(f"Viability  : {viability:.1f}%")

    if viability >= 90:
        print("Assessment: Excellent")
    elif viability >= 70:
        print("Assessment: Acceptable")
    else:
        print("Assessment: Low viability")


# =============================================================================
# 18. SUMMARY
# =============================================================================
#
# Key concepts:
#
#   Variables       -> age = 30
#   Data types      -> int, float, str, list, dict
#   Operations      -> +, -, *, /, %, **
#   Strings         -> slicing, formatting
#   Lists           -> indexing, methods
#   Dictionaries    -> key-value pairs
#   Conditionals    -> if, elif, else
#   Loops           -> for, while, break, continue
#   Functions       -> def, parameters, return
#   Libraries       -> import
#   Error handling  -> try, except, finally
#   File I/O        -> open, read, write


# =============================================================================
# 19. NEXT STEPS
# =============================================================================
#
# 1. Practice simple Python scripts.
# 2. Learn NumPy for numerical and array operations.
# 3. Learn pandas for data manipulation and analysis.
# 4. Learn Matplotlib / Seaborn for visualization.
# 5. Study statistics and data science.
# 6. Apply Python to tissue-engineering and biomedical problems.
#
# Beginner projects:
#   - Calculator
#   - Guessing game
#   - To-do list
#   - Text analysis
#   - Data statistics
#   - Cell viability calculator


# =============================================================================
# 20. RESOURCES
# =============================================================================
#
# Official Python:
#   https://www.python.org/
#   https://docs.python.org/3/
#   https://www.python.org/dev/peps/pep-0008/
#
# Data science:
#   https://numpy.org/
#   https://pandas.pydata.org/
#   https://matplotlib.org/
#   https://seaborn.pydata.org/
#
# Practice:
#   https://leetcode.com/
#   https://www.hackerrank.com/
#   https://www.codewars.com/
#
# Learning:
#   https://realpython.com/
#   https://www.codecademy.com/
#   https://www.udemy.com/
#   https://www.coursera.org/
#
# Books:
#   Python Crash Course — Eric Matthes
#   Automate the Boring Stuff with Python — Al Sweigart
#   Learning Python — Mark Lutz


# =============================================================================
# MAIN PROGRAM
# =============================================================================

def main():
    """Run the lecture demonstrations."""

    print("=" * 70)
    print("MSTE WS26 | INTRODUCTION TO PYTHON")
    print("Fundamentals for Beginners and Data-Driven Applications")
    print("Dr. Prabath Jayathissa | UAS Technikum Wien | 2026")
    print("=" * 70)

    demo_repl()
    demo_variables()
    demo_arithmetic()
    demo_strings()
    demo_lists()
    demo_list_methods()
    demo_dictionaries()
    demo_conditionals()
    demo_comparison_operators()
    demo_logical_operators()
    demo_for_loops()
    demo_while_loops()
    demo_loop_control()
    demo_functions()
    demo_standard_library()
    demo_optional_data_science_libraries()
    demo_pep8()
    demo_documentation()
    demo_indexing()
    demo_mutable_defaults()
    demo_type_conversion()
    demo_scope()
    demo_error_handling()
    demo_input()
    demo_file_operations()
    cell_viability_calculator()

    print("\n" + "=" * 70)
    print("END OF INTRODUCTION TO PYTHON")
    print("Python is learned by doing! 🐍")
    print("=" * 70)


if __name__ == "__main__":
    main()
