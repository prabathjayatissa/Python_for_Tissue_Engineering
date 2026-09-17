
# A simple theory lesson with many examples in one file

# Before running this script, install NumPy with:
# pip install numpy

import numpy as np

print("Welcome to NumPy!")
print("We will learn NumPy using boxes, toys, and numbers.\n")


# ============================================================
# THEORY 1: What is NumPy?
# ============================================================
# NumPy means Numerical Python.
#
# Numerical means working with numbers.
#
# NumPy is a Python library. A library is a box of ready-made
# tools that other people have created for us.
#
# NumPy helps Python work with many numbers quickly and easily.
#
# Imagine having one toy:
#     5
#
# That is easy to count.
#
# Now imagine having hundreds or thousands of toys.
# NumPy helps us organize and work with them.


# ============================================================
# THEORY 2: What is an array?
# ============================================================
# The most important NumPy object is called an ARRAY.
#
# An array is like a row of boxes.
# Each box can hold a number.
#
# Example:
#
#     [2, 4, 6, 8]
#
# This is an array with four boxes.
#
# In this example:
# - the first box holds 2
# - the second box holds 4
# - the third box holds 6
# - the fourth box holds 8

numbers = np.array([2, 4, 6, 8])

print("Our first array:")
print(numbers)


# ============================================================
# THEORY 3: Making an array
# ============================================================
# np.array() changes a normal Python list into a NumPy array.
#
# A list is like a simple line of toys.
# NumPy turns that line into a special number tool.

python_list = [1, 2, 3, 4, 5]
number_array = np.array(python_list)

print("Python list:", python_list)
print("NumPy array:", number_array)


# ============================================================
# THEORY 4: Counting items with size
# ============================================================
# The size tells us how many boxes are in an array.
#
# Our array has five numbers, so its size is 5.

print("Number of items:", number_array.size)


# ============================================================
# THEORY 5: Position and index
# ============================================================
# Each box has a position number called an INDEX.
#
# Important: Python starts counting at 0.
#
# For this array:
#
#     [10, 20, 30, 40]
#
# The positions are:
#      0   1   2   3
#
# So number 10 is at position 0.
# Number 30 is at position 2.

colors = np.array(["red", "blue", "green", "yellow"])

print("Colors:", colors)
print("First color:", colors[0])
print("Third color:", colors[2])


# ============================================================
# THEORY 6: Changing an item
# ============================================================
# We can put a new value into one box.
#
# Here we change the first color from red to pink.

colors[0] = "pink"
print("Colors after changing the first item:", colors)


# ============================================================
# THEORY 7: Adding numbers
# ============================================================
# NumPy can do arithmetic with arrays.
#
# Think of every box getting one extra toy.
#
# If we add 1 to this array:
#     [1, 2, 3]
#
# NumPy gives us:
#     [2, 3, 4]

small_numbers = np.array([1, 2, 3])
print("Original numbers:", small_numbers)
print("Add 1:", small_numbers + 1)


# ============================================================
# THEORY 8: Subtraction, multiplication, and division
# ============================================================
# NumPy performs the same operation on every box.

print("Subtract 1:", small_numbers - 1)
print("Multiply by 2:", small_numbers * 2)
print("Divide by 2:", small_numbers / 2)


# ============================================================
# THEORY 9: Adding two arrays
# ============================================================
# If two arrays have the same number of boxes,
# NumPy can add matching boxes together.
#
# First array:  [1, 2, 3]
# Second array: [4, 5, 6]
# Result:       [5, 7, 9]

apples = np.array([1, 2, 3])
bananas = np.array([4, 5, 6])
fruit_total = apples + bananas

print("Apples:", apples)
print("Bananas:", bananas)
print("Fruit totals:", fruit_total)


# ============================================================
# THEORY 10: Comparing numbers
# ============================================================
# NumPy can ask questions about every box.
#
# The answer is True or False.
#
# For example, numbers greater than 3:
#     [1, 4, 2, 5]
#     [False, True, False, True]

ages = np.array([2, 5, 3, 6])
print("Ages:", ages)
print("Is each age greater than 3?", ages > 3)
print("Is each age equal to 5?", ages == 5)


# ============================================================
# THEORY 11: Selecting items with a condition
# ============================================================
# A condition can help us choose only some items.
#
# This is like saying:
# "Please show me only the numbers bigger than 3."

big_ages = ages[ages > 3]
print("Ages bigger than 3:", big_ages)


# ============================================================
# THEORY 12: Sum
# ============================================================
# The sum adds all the numbers together.
#
# Example:
#     2 + 3 + 4 = 9

pieces = np.array([2, 3, 4])
print("Pieces:", pieces)
print("Total pieces:", np.sum(pieces))


# ============================================================
# THEORY 13: Mean or average
# ============================================================
# The mean is another word for average.
#
# To find the average, we:
# 1. Add all the numbers.
# 2. Divide by how many numbers there are.
#
# For [2, 4, 6]:
#     (2 + 4 + 6) / 3 = 4

scores = np.array([2, 4, 6])
print("Scores:", scores)
print("Average score:", np.mean(scores))


# ============================================================
# THEORY 14: Smallest and largest numbers
# ============================================================
# np.min() finds the smallest number.
# np.max() finds the largest number.

heights = np.array([10, 7, 12, 9])
print("Heights:", heights)
print("Smallest height:", np.min(heights))
print("Largest height:", np.max(heights))


# ============================================================
# THEORY 15: Sorting numbers
# ============================================================
# Sorting puts numbers in order, from small to big.

messy_numbers = np.array([5, 2, 8, 1, 4])
ordered_numbers = np.sort(messy_numbers)

print("Messy numbers:", messy_numbers)
print("Ordered numbers:", ordered_numbers)


# ============================================================
# THEORY 16: A two-dimensional array
# ============================================================
# An array can have rows and columns.
#
# Imagine a small table or a chocolate bar.
#
#     1  2  3
#     4  5  6
#
# This has:
# - 2 rows
# - 3 columns
#
# It is called a two-dimensional array.

table = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Two-dimensional array:")
print(table)


# ============================================================
# THEORY 17: Rows and columns
# ============================================================
# A row goes from left to right.
# A column goes from top to bottom.
#
# table[0] means the first row.
# table[:, 0] means the first column.

print("First row:", table[0])
print("Second row:", table[1])
print("First column:", table[:, 0])


# ============================================================
# THEORY 18: Getting one item from a table
# ============================================================
# To find one item, we use two positions:
# table[row, column]
#
# The number 5 is in:
# - row 1
# - column 1
#
# Remember that counting starts at 0.

print("Number in row 2, column 2:", table[1, 1])


# ============================================================
# THEORY 19: Shape
# ============================================================
# Shape tells us how many rows and columns an array has.
#
# The table has 2 rows and 3 columns.
# Its shape is (2, 3).

print("Table shape:", table.shape)


# ============================================================
# THEORY 20: Reshape
# ============================================================
# Reshape changes the arrangement of numbers.
#
# We still have the same numbers, but we place them
# into a different number of rows and columns.
#
# Six numbers can become:
# - 2 rows and 3 columns
# - 3 rows and 2 columns

six_numbers = np.array([1, 2, 3, 4, 5, 6])
new_table = six_numbers.reshape(3, 2)

print("Six numbers:", six_numbers)
print("Reshaped into 3 rows and 2 columns:")
print(new_table)


# ============================================================
# THEORY 21: Zeros and ones
# ============================================================
# NumPy can quickly make arrays filled with zeros or ones.
#
# np.zeros(4) makes four zeros.
# np.ones(3) makes three ones.

print("Four zeros:", np.zeros(4))
print("Three ones:", np.ones(3))


# ============================================================
# THEORY 22: A range of numbers
# ============================================================
# np.arange() makes a line of counting numbers.
#
# np.arange(5) gives numbers starting at 0 and stopping before 5.
# Result: [0, 1, 2, 3, 4]

counting_numbers = np.arange(5)
print("Counting numbers:", counting_numbers)


# ============================================================
# THEORY 23: Random numbers
# ============================================================
# Computers can make random-looking numbers.
#
# These numbers are useful for games, experiments, and practice.
#
# The numbers below can be different each time the script runs.

random_numbers = np.random.randint(1, 11, size=5)
print("Five random numbers from 1 to 10:", random_numbers)


# ============================================================
# THEORY 24: Data type
# ============================================================
# A data type tells us what kind of thing is inside an array.
#
# Examples:
# - int means whole numbers, such as 1 or 5
# - float means numbers with a decimal, such as 2.5
# - str means text, such as "red"

whole_numbers = np.array([1, 2, 3])
decimal_numbers = np.array([1.5, 2.5, 3.5])

print("Whole-number type:", whole_numbers.dtype)
print("Decimal-number type:", decimal_numbers.dtype)


# ============================================================
# THEORY 25: Copying an array
# ============================================================
# A copy is a separate array with the same values.
#
# Changing the copy does not change the original array.

original = np.array([1, 2, 3])
copy_of_original = original.copy()
copy_of_original[0] = 99

print("Original array:", original)
print("Changed copy:", copy_of_original)


# ============================================================
# THEORY 26: Joining arrays
# ============================================================
# Joining means putting arrays together.
#
# It is like joining two lines of toys.

first_line = np.array([1, 2])
second_line = np.array([3, 4])
joined_line = np.concatenate((first_line, second_line))

print("First line:", first_line)
print("Second line:", second_line)
print("Joined line:", joined_line)


# ============================================================
# THEORY 27: Splitting an array
# ============================================================
# Splitting means cutting one line into smaller lines.

long_line = np.array([1, 2, 3, 4])
small_lines = np.array_split(long_line, 2)

print("Long line:", long_line)
print("Two smaller lines:", small_lines)


# ============================================================
# THEORY 28: NumPy and a simple real-life example
# ============================================================
# Imagine that three children have three toys each.
# Each row belongs to one child.
# Each column shows one toy count.

children_toys = np.array([
    [2, 1, 3],
    [4, 2, 1],
    [1, 3, 2]
])

print("Toys owned by three children:")
print(children_toys)
print("Total toys for each child:", np.sum(children_toys, axis=1))
print("Total toys of each type:", np.sum(children_toys, axis=0))


# ============================================================
# THEORY 29: What does axis mean?
# ============================================================
# An axis tells NumPy which direction to work in.
#
# axis=1 works across each row.
# It gives one answer for each child.
#
# axis=0 works down each column.
# It gives one answer for each toy type.


# ============================================================
# THEORY 30: Why is NumPy useful?
# ============================================================
# NumPy is useful because it can:
# - store many numbers
# - perform calculations quickly
# - work with tables of numbers
# - find sums and averages
# - find the smallest and largest values
# - compare many values at once
# - help with science, pictures, games, and data
#
# Scientists, teachers, engineers, and programmers use NumPy
# when they need to work with lots of numbers.


# ============================================================
# FINAL CHILD-FRIENDLY SUMMARY
# ============================================================
# NumPy is like a smart box organizer for numbers.
#
# An array is a row or table of boxes.
# Each box holds a number.
# NumPy lets us count, add, compare, sort, and study the boxes.

print("\nHere is our NumPy lesson summary:")
print("1. NumPy is a Python tool for working with numbers.")
print("2. An array is a group of number boxes.")
print("3. An index tells us where an item is.")
print("4. Shape tells us the rows and columns.")
print("5. NumPy can calculate with many numbers at once.")
print("6. NumPy helps us understand data.")
print("\nGreat job! You learned the basic ideas of NumPy!")