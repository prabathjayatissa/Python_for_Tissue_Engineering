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
# Create the expanded CSV data as a string
csv_data = """Cell line,Experiment,Quantity,Time (hours),Condition
HEK293,Differentiation,50,24,TGF-β1
HEK293,Proliferation,75,16,Cytokines
HEK293,Apoptosis,20,48,Drug X1
MCF-7,Differentiation,65,30,TGF-β1
MCF-7,Proliferation,80,24,Cytokines
MCF-7,Apoptosis,15,48,Drug X2
A549,Differentiation,70,36,TGF-β1
A549,Proliferation,85,20,Cytokines
A549,Apoptosis,10,48,Drug X3"""

# Write the expanded CSV data to a file
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

#### Group By and Aggregate
aggregated_df = df.groupby('Experiment').agg({'Quantity': 'mean', 'Time (hours)': 'max'})
print("\nAggregated DataFrame (Mean Quantity and Max Time by Experiment):")
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
    'Cell line': ['HEK293', 'MCF-7', None, 'A549'],
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

#### Bar Plot
plt.figure(figsize=(10, 6))
df.groupby('Experiment')['Quantity'].mean().plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.title('Average Quantity by Experiment Type')
plt.xlabel('Experiment Type')
plt.ylabel('Average Quantity')
plt.show()

print("\nBar plot displayed. Check the Matplotlib output.")

#### Line Plot
plt.figure(figsize=(10, 6))
for cell_line in df['Cell line'].unique():
    subset = df[df['Cell line'] == cell_line]
    plt.plot(subset['Experiment'], subset['Quantity'], marker='o', label=cell_line)

plt.title('Quantity by Experiment Type for Each Cell Line')
plt.xlabel('Experiment Type')
plt.ylabel('Quantity')
plt.legend()
plt.show()

print("\nLine plot displayed. Check the Matplotlib output.")

### 10. Conclusion
print("\nPandas Tutorial Completed! You have mastered basic to intermediate Pandas concepts.")

