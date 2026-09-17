# A simple story about organizing information in tables

# Pandas is a Python library for working with information.
# A library is a box of ready-to-use tools.
#
# In this lesson, we will imagine that Pandas is a magic table maker.
# It helps us organize information about toys, fruits, and children.


# ============================================================
# THEORY 1: What is information?
# ============================================================
# Information is something we know.
#
# Examples:
# - A toy is red.
# - A banana is yellow.
# - Sara has 5 apples.
#
# Computers like information to be neat and organized.
# Tables help us organize information.


# ============================================================
# THEORY 2: What is a table?
# ============================================================
# A table has:
#
# 1. Columns: vertical lists with names.
# 2. Rows: horizontal lines containing one record.
#
# Imagine a classroom table:
#
#   Name     Age     Favorite Color
#   Sara      5          Red
#   Omar      5          Blue
#
# A row tells us about one child.
# A column tells us one kind of information.


# Pandas must be installed before running this file.
# Usually, we install it with:
# pip install pandas

import pandas as pd


# ============================================================
# THEORY 3: What is pandas?
# ============================================================
# Pandas is a Python library for organizing and studying tables.
#
# We write "pd" as a short name for pandas.
# This is like giving a long word a small nickname.

print("Welcome to Pandas!")
print("Pandas helps us organize information in tables.\n")


# ============================================================
# THEORY 4: What is a Series?
# ============================================================
# A Series is one column of information.
#
# Imagine one basket containing only apples:
# 2, 5, 3, 4
#
# A Pandas Series is like one neat basket or one vertical list.

apples = pd.Series([2, 5, 3, 4])

print("One Series of apples:")
print(apples)
print()


# A Series can have labels.
# Labels are names that help us understand each value.

apples_by_child = pd.Series(
    [2, 5, 3],
    index=["Sara", "Omar", "Lina"]
)

print("Apples belonging to each child:")
print(apples_by_child)
print()


# We can ask for one value by using its label.
print("How many apples does Sara have?")
print(apples_by_child["Sara"])
print()


# ============================================================
# THEORY 5: What is a DataFrame?
# ============================================================
# A DataFrame is a complete table.
#
# Imagine a table with columns for:
# - a child's name
# - the child's age
# - the child's favorite color
#
# Each row describes one child.
#
# A DataFrame is one of the most important things in Pandas.

children = pd.DataFrame({
    "Name": ["Sara", "Omar", "Lina"],
    "Age": [5, 5, 4],
    "Favorite_Color": ["Red", "Blue", "Green"]
})

print("Our children's table:")
print(children)
print()


# ============================================================
# THEORY 6: What is a column?
# ============================================================
# A column is one vertical part of a table.
#
# We can choose one column by writing its name.

print("Only the names:")
print(children["Name"])
print()

print("Only the ages:")
print(children["Age"])
print()


# We can also create a new column.
# Here, we add each child's favorite snack.

children["Favorite_Snack"] = ["Apple", "Banana", "Cookie"]

print("Table after adding a snack column:")
print(children)
print()


# ============================================================
# THEORY 7: What is a row?
# ============================================================
# A row contains information about one thing.
#
# In this table, one row contains information about one child.
#
# The first row is called row 0 by Python.

print("The first row:")
print(children.iloc[0])
print()

print("The second row:")
print(children.iloc[1])
print()


# iloc means: find something by its position.
# Position counting starts at 0:
# - first item: position 0
# - second item: position 1
# - third item: position 2


# ============================================================
# THEORY 8: Looking at the beginning and end
# ============================================================
# head() shows the first rows.
# It is like looking at the first toys in a toy box.
#
# tail() shows the last rows.
# It is like looking at the last toys in a toy box.

print("The first two rows:")
print(children.head(2))
print()

print("The last two rows:")
print(children.tail(2))
print()


# ============================================================
# THEORY 9: How big is the table?
# ============================================================
# shape tells us how many rows and columns we have.
#
# It gives us:
# (number of rows, number of columns)

print("The shape of the table is:")
print(children.shape)
print()

print("The table has", children.shape[0], "rows.")
print("The table has", children.shape[1], "columns.")
print()


# ============================================================
# THEORY 10: Choosing rows with a condition
# ============================================================
# A condition is a question with an answer of True or False.
#
# Example question:
# Is the child 5 years old?
#
# Pandas can find only the rows that answer True.

five_year_olds = children[children["Age"] == 5]

print("Children who are 5 years old:")
print(five_year_olds)
print()


# Another condition:
# Find children whose favorite color is red.

red_lovers = children[children["Favorite_Color"] == "Red"]

print("Children who like red:")
print(red_lovers)
print()


# ============================================================
# THEORY 11: Bigger, smaller, and equal
# ============================================================
# We can use comparison signs:
#
# == means equal to
# >  means greater than
# <  means less than
# >= means greater than or equal to
# <= means less than or equal to

older_children = children[children["Age"] > 4]

print("Children older than 4:")
print(older_children)
print()


younger_children = children[children["Age"] < 5]

print("Children younger than 5:")
print(younger_children)
print()


# ============================================================
# THEORY 12: Simple calculations
# ============================================================
# Pandas can do simple math for a column.
#
# sum() adds everything together.
# mean() finds the average.
# min() finds the smallest value.
# max() finds the largest value.

ages = children["Age"]

print("All ages added together:")
print(ages.sum())
print()

print("The average age is:")
print(ages.mean())
print()

print("The youngest age is:")
print(ages.min())
print()

print("The oldest age is:")
print(ages.max())
print()


# ============================================================
# THEORY 13: Sorting information
# ============================================================
# Sorting means putting things in order.
#
# We can sort children from youngest to oldest.

sorted_children = children.sort_values("Age")

print("Children sorted from youngest to oldest:")
print(sorted_children)
print()


# We can sort from oldest to youngest.
# ascending=False means use the biggest value first.

reverse_sorted_children = children.sort_values("Age", ascending=False)

print("Children sorted from oldest to youngest:")
print(reverse_sorted_children)
print()


# ============================================================
# THEORY 14: Counting groups
# ============================================================
# value_counts() counts how often each value appears.
#
# It can answer questions like:
# How many children like each color?

color_counts = children["Favorite_Color"].value_counts()

print("How many children like each color?")
print(color_counts)
print()


# ============================================================
# THEORY 15: Missing information
# ============================================================
# Sometimes we do not know something.
#
# Pandas represents missing information with NaN.
# NaN means "Not a Number" or missing value.

pets = pd.DataFrame({
    "Name": ["Sara", "Omar", "Lina"],
    "Pet": ["Cat", None, "Fish"]
})

print("A table with one missing pet:")
print(pets)
print()

print("Which values are missing?")
print(pets.isna())
print()

# fillna() can put a replacement in an empty place.
filled_pets = pets.fillna("No pet yet")

print("The table after filling the missing value:")
print(filled_pets)
print()


# ============================================================
# THEORY 16: Adding and changing information
# ============================================================
# A table can grow and change.
#
# We can add a new child as a new row.
# concat() joins tables together.

new_child = pd.DataFrame({
    "Name": ["Mia"],
    "Age": [5],
    "Favorite_Color": ["Yellow"],
    "Favorite_Snack": ["Pear"]
})

children_with_mia = pd.concat([children, new_child], ignore_index=True)

print("Table after adding Mia:")
print(children_with_mia)
print()


# We can change one value.
children_with_mia.loc[0, "Favorite_Color"] = "Purple"

print("Table after changing Sara's color:")
print(children_with_mia)
print()


# ============================================================
# THEORY 17: Making a new column from old columns
# ============================================================
# We can use existing columns to make a new column.
#
# Here, we make a column called Age_Next_Year.

children_with_mia["Age_Next_Year"] = children_with_mia["Age"] + 1

print("Table with ages for next year:")
print(children_with_mia)
print()


# ============================================================
# THEORY 18: Reading a small CSV file
# ============================================================
# CSV means Comma-Separated Values.
#
# A CSV file is like a simple table saved as a text file.
#
# Pandas can read a CSV file with read_csv().
#
# This example creates a tiny CSV file first.

csv_text = "Name,Animal,Sound\nMilo,Cat,Meow\nBob