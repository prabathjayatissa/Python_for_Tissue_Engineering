import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### 2. Basic Data Structures

#### Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:")
print(s)

#### DataFrame
data = {
    'Cell line': ['HEK293', 'MCF-7', 'A549'],
    'Experiment': ['Differentiation', 'Proliferation', 'Apoptosis']
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

### 4. Reading and Writing Data

#### Reading from a CSV File
# Create the CSV data as a string
csv_data = """Cell line,Experiment
HEK293,Differentiation
MCF-7,Proliferation
A549,Apoptosis"""

# Write the CSV data to a file
with open('data.csv', 'w') as f:
    f.write(csv_data)

# Read the CSV file
df = pd.read_csv('data.csv')
print("\nFirst 5 rows of the CSV file:")
print(df.head())

#### Writing to a CSV File
df.to_csv('output.csv', index=False)
print("\nData written to 'output.csv'. Check the file.")

### 5. Basic Data Manipulation

#### Selecting Data
print("\nSelect 'Experiment' column:")
print(df['Experiment'])

print("\nSelect multiple columns ['Experiment', 'Cell line']:")
print(df[['Experiment', 'Cell line']])

#### Filtering Data
filtered_df = df[df['Experiment'] == 'Differentiation']
print("\nFiltered DataFrame where Experiment is 'Differentiation':")
print(filtered_df)

### 6. Data Aggregation

# Example data with quantity and experiment type
data = {
    'Experiment': ['Differentiation', 'Proliferation', 'Apoptosis', 'Differentiation'],
    'Quantity': [30, 45, 20, 60]
}
df = pd.DataFrame(data)

aggregated_df = df.groupby('Experiment').mean()
print("\nAggregated DataFrame (Mean Quantity by Experiment):")
print(aggregated_df)

### 7. Merging and Joining Data

df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C'],
    'Value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'Key': ['A', 'B', 'D'],
    'Value2': [4, 5, 6]
})

merged_df = pd.merge(df1, df2, on='Key', how='outer')
print("\nMerged DataFrame:")
print(merged_df)

### 8. Data Cleaning

#### Handling Missing Values
data_with_nan = {
    'Experiment': ['Differentiation', 'Proliferation', None, 'Apoptosis'],
    'Quantity': [30, np.nan, 20, 60]
}
df = pd.DataFrame(data_with_nan)

print("\nDataFrame with missing values:")
print(df)

# Detecting missing values
print("\nMissing values in DataFrame:")
print(df.isnull())

# Filling missing values with a specific value
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Dropping rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

### 9. Visualization

plt.figure(figsize=(8, 4))
df = pd.DataFrame({
    'Experiment': ['Differentiation', 'Proliferation', 'Apoptosis'],
    'Quantity': [30, 45, 20]
})
df.plot(x='Experiment', y='Quantity', kind='line', marker='o')
plt.title('Quantity by Experiment Type')
plt.xlabel('Experiment Type')
plt.ylabel('Quantity')
plt.show()

print("\nPlot displayed. Check the Matplotlib output.")

### 10. Conclusion
print("\nPandas Tutorial Completed! You have mastered basic to intermediate Pandas concepts.")

