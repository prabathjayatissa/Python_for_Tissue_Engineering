# Matplotlib is a Python library for making charts and pictures.
# A library is a box of ready-to-use tools.
#
# In this lesson, we imagine that Matplotlib is a magic drawing box.
# We give it numbers, and it draws a picture for us.

import matplotlib.pyplot as plt


# ============================================================
# THEORY 1: What is Matplotlib?
# ============================================================
# Matplotlib helps Python draw:
# - lines
# - dots
# - bars
# - circles
# - pictures made from numbers
#
# A chart is a picture that helps us understand information.
#
# Example:
# If we count toys every day, a chart can show which day had
# the most toys.

print("Welcome to Matplotlib!")
print("Matplotlib helps Python draw charts and pictures.\n")


# ============================================================
# THEORY 2: What is pyplot?
# ============================================================
# pyplot is a part of Matplotlib.
#
# We give pyplot the short name plt.
#
# This is like giving a long word a short nickname.
# It is easier to write plt than matplotlib.pyplot.


# ============================================================
# THEORY 3: What are x and y values?
# ============================================================
# A chart often uses two directions:
#
# x-axis: goes from left to right.
# y-axis: goes from bottom to top.
#
# Imagine a treasure map:
# - x tells us how far to walk sideways.
# - y tells us how far to walk upward.
#
# A point is placed where x and y meet.


# ============================================================
# EXAMPLE 1: Draw a simple line
# ============================================================
# A line chart joins points together.
#
# We have three days and the number of toys cleaned:
# Monday: 2 toys
# Tuesday: 4 toys
# Wednesday: 3 toys


days = ["Monday", "Tuesday", "Wednesday"]
toys_cleaned = [2, 4, 3]

plt.figure(figsize=(7, 4))
plt.plot(days, toys_cleaned, marker="o")
plt.title("Toys Cleaned Each Day")
plt.xlabel("Day")
plt.ylabel("Number of Toys")
plt.grid(True)
plt.tight_layout()
plt.show()

# THEORY:
# plot() draws a line.
# marker="o" puts a small circle on each value.
# title() gives the chart a name.
# xlabel() names the x-axis.
# ylabel() names the y-axis.
# grid() adds soft helper lines.
# show() displays the picture.


# ============================================================
# EXAMPLE 2: Draw a colorful line
# ============================================================
# A chart can have colors and different line styles.


days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
water_glasses = [2, 3, 3, 4, 5]

plt.figure(figsize=(7, 4))
plt.plot(
    days,
    water_glasses,
    color="blue",
    marker="o",
    linestyle="--",
    linewidth=2
)
plt.title("Glasses of Water")
plt.xlabel("Day")
plt.ylabel("Glasses")
plt.grid(True)
plt.tight_layout()
plt.show()

# THEORY:
# color changes the line color.
# marker changes the point shape.
# linestyle changes the line style.
# linewidth changes how thick the line is.


# ============================================================
# EXAMPLE 3: Draw a bar chart
# ============================================================
# A bar chart uses rectangles.
#
# Taller bars mean bigger numbers.
# Shorter bars mean smaller numbers.
#
# We can use a bar chart to compare toys.


toy_names = ["Car", "Ball", "Doll", "Blocks"]
toy_counts = [5, 3, 4, 8]

plt.figure(figsize=(7, 4))
plt.bar(toy_names, toy_counts, color=["red", "blue", "pink", "green"])
plt.title("How Many Toys We Have")
plt.xlabel("Toy")
plt.ylabel("Number of Toys")
plt.tight_layout()
plt.show()

# THEORY:
# bar() draws bars.
# Each toy gets one bar.
# The height of the bar shows the number.
#
# This is useful when we want to compare things.


# ============================================================
# EXAMPLE 4: Draw a horizontal bar chart
# ============================================================
# barh() draws bars from left to right.
#
# This can be easier to read when names are long.


animals = ["Cat", "Dog", "Rabbit", "Bird"]
animal_food = [2, 5, 3, 1]

plt.figure(figsize=(7, 4))
plt.barh(animals, animal_food, color="orange")
plt.title("Food Portions for Animals")
plt.xlabel("Number of Portions")
plt.ylabel("Animal")
plt.tight_layout()
plt.show()


# ============================================================
# EXAMPLE 5: Draw a pie chart
# ============================================================
# A pie chart is a round chart like a pizza.
#
# Each slice shows part of the whole.
#
# If a slice is big, that category has a big part.
# If a slice is small, that category has a small part.


snacks = ["Apples", "Bananas", "Cookies"]
snack_numbers = [4, 3, 2]

plt.figure(figsize=(6, 6))
plt.pie(
    snack_numbers,
    labels=snacks,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Favorite Snacks")
plt.show()

# THEORY:
# pie() draws a pie chart.
# labels gives names to the slices.
# autopct shows percentages.
# startangle changes where the first slice starts.
#
# A percentage tells us how much of the whole something is.


# ============================================================
# EXAMPLE 6: Draw a scatter plot
# ============================================================
# A scatter plot uses separate dots.
#
# It helps us look at pairs of numbers.
#
# Example:
# x = number of minutes playing
# y = number of happy smiles


playing_minutes = [5, 10, 15, 20, 25]
happy_smiles = [1, 2, 3, 4, 5]

plt.figure(figsize=(7, 4))
plt.scatter(playing_minutes, happy_smiles, color="purple", s=100)
plt.title("Playing Time and Happy Smiles")
plt.xlabel("Minutes of Playing")
plt.ylabel("Happy Smiles")
plt.grid(True)
plt.tight_layout()
plt.show()

# THEORY:
# scatter() draws separate dots.
# s controls the dot size.
#
# Each dot represents one pair of values.
#
# If dots move upward, the second number may be growing.


# ============================================================
# EXAMPLE 7: Draw a histogram
# ============================================================
# A histogram groups numbers into boxes called bins.
#
# It helps us see how often numbers appear.
#
# Imagine measuring the heights of children.
# The histogram shows how many children are in each height group.


child_heights = [95, 100, 102, 105, 105, 108, 110, 110, 112, 115]

plt.figure(figsize=(7, 4))
plt.hist(child_heights, bins=5, color="skyblue", edgecolor="black")
plt.title("Children's Heights")
plt.xlabel("Height")
plt.ylabel("Number of Children")
plt.tight_layout()
plt.show()

# THEORY:
# hist() draws a histogram.
# bins tells Python how many groups to make.
# edgecolor adds a border around each bar.
#
# A histogram is useful for seeing the shape of a collection
# of numbers.


# ============================================================
# EXAMPLE 8: Draw many lines on one chart
# ============================================================
# We can put more than one line on the same chart.
#
# Here we compare two children's reading progress.


weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
sara_pages = [2, 4, 5, 7]
omar_pages = [1, 3, 4, 6]

plt.figure(figsize=(8, 4))
plt.plot(weeks, sara_pages, marker="o", label="Sara")
plt.plot(weeks, omar_pages, marker="s", label="Omar")
plt.title("Reading Progress")
plt.xlabel("Week")
plt.ylabel("Pages Read")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# THEORY:
# label gives a name to each line.
# legend() shows the names.
#
# A legend is like a small guide that tells us
# which color or shape belongs to each person.


# ============================================================
# EXAMPLE 9: Add text to a chart
# ============================================================
# We can write a note next to an important point.


days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
smiles = [2, 4, 3, 6, 5]

plt.figure(figsize=(7, 4))
plt.plot(days, smiles, marker="o", color="green")
plt.title("Happy Smiles During the Week")
plt.xlabel("Day")
plt.ylabel("Number of Smiles")
plt.annotate(
    "Most smiles!",
    xy=("Thu", 6),
    xytext=("Tue", 6),
    arrowprops={"arrowstyle": "->"}
)
plt.grid(True)
plt.tight_layout()
plt.show()

# THEORY:
# annotate() adds a note to the chart.
# xy tells us where the important point is.
# xytext tells us where to put the note.
# An arrow can point from the note to the point.


# ============================================================
# EXAMPLE 10: Change the chart size
# ============================================================
# figsize changes the width and height of a chart.
#
# The first number is the width.
# The second number is the height.


colors = ["Red", "Blue", "Yellow"]
color_counts = [3, 5, 2]

plt.figure(figsize=(10, 5))
plt.bar(colors, color_counts, color=colors)
plt.title("Colorful Blocks")
plt.xlabel("Color")
plt.ylabel("Number of Blocks")
plt.show()


# ============================================================
# EXAMPLE 11: Make a chart with two parts
# ============================================================
# A figure is the whole drawing paper.
# An axes is one chart area on the paper.
#
# subplots() helps us make more than one chart in one figure.


fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].bar(["Red", "Blue"], [4, 6], color=["red", "blue"])
axes[0].set_title("Blocks")
axes[0].set_ylabel("Number")

axes[1].plot(["Mon", "Tue", "Wed"], [2, 4, 3], marker="o")
axes[1].set_title("Smiles")
axes[1].set_ylabel("Number")

plt.tight_layout()
plt.show()

# THEORY:
# fig is the whole piece of paper.
# axes[0] is the first chart.
# axes[1] is the second chart.
#
# This lets us compare different pictures together.


# ============================================================
# EXAMPLE 12: Save a chart as a picture file
# ============================================================
# savefig() saves a chart.
#
# The chart can be opened later like a normal picture.


months = ["Jan", "Feb", "Mar"]
flowers = [2, 5, 4]

plt.figure(figsize=(7, 4))
plt.plot(months, flowers, marker="o", color="magenta")
plt.title("Flowers in the Garden")
plt.xlabel("Month")
plt.ylabel("Number of Flowers")
plt.tight_layout()
plt.savefig("flowers_chart.png")
plt.show()

print("A chart was saved as flowers_chart.png.")

# THEORY:
# savefig() saves the current chart.
# .png is a common picture format.
#
# Always save before closing or changing the chart.


# ============================================================
# EXAMPLE 13: Close a chart
# ============================================================
# close() closes the current chart window.
#
# This is useful when a program creates many charts.

plt.close()


# ============================================================
# SIMPLE MATPLOTLIB WORD GUIDE
# ============================================================
# matplotlib       = a Python library for drawing charts
# pyplot           = the chart-drawing part of Matplotlib
# plt              = a short nickname for pyplot
# figure()         = create a drawing paper
# plot()           = draw a line
# bar()            = draw vertical bars
# barh()           = draw horizontal bars
# pie()            = draw a round pie chart
# scatter()        = draw separate dots
# hist()           = draw groups of numbers
# title()          = give the chart a name
# xlabel()         = name the x-axis
# ylabel()         = name the y-axis
# legend()         = show the chart guide
# grid()           = add helper lines
# annotate()       = add a note or arrow
# subplots()       = make several charts together
# savefig()        = save a chart as a picture
# show()           = display a chart
# close()          = close a chart


# ============================================================
# FINAL SIMPLE IDEA
# ============================================================
# Matplotlib is like a magic drawing helper.
#
# We give it numbers and names.
# It turns them into lines, bars, dots, slices, and pictures.
#
# Charts help us see information instead of only reading numbers.
#
# A line can show change.
# Bars can compare things.
# A pie can show parts of a whole.
# Dots can show pairs of numbers.
# A histogram can show groups of numbers.

print("\nMatplotlib is like a magic drawing box!")
print("It helps Python turn numbers into colorful pictures.")
