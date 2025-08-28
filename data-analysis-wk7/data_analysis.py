
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

# URL for the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Define column names for the dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Load the dataset using pandas
df = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataset
print("---" + " First 5 Rows of the Dataset " + "---")
print(df.head())
print("\n" + "-"*30 + "\n")

# Explore the structure of the dataset
print("---" + " Dataset Structure and Info " + "---")
df.info()
print("\n" + "-"*30 + "\n")

# Clean the dataset (check for missing values)
print("---" + " Missing Values " + "---")
print(df.isnull().sum())
print("\n" + "-"*30 + "\n")

# Task 2: Basic Data Analysis

# Compute basic statistics of the numerical columns
print("---" + " Basic Statistics " + "---")
print(df.describe())
print("\n" + "-"*30 + "\n")

# Perform groupings on the 'species' column and compute the mean
print("---" + " Mean of Each Feature by Species " + "---")
print(df.groupby('species').mean())
print("\n" + "-"*30 + "\n")

# Task 3: Data Visualization

# Set the style for the plots
sns.set_style("whitegrid")

# 1. Line Chart: Trends in sepal length across the dataset
plt.figure(figsize=(10, 6))
plt.plot(df['sepal_length'], marker='o', linestyle='-')
plt.title('Trend of Sepal Length Across the Dataset')
plt.xlabel('Data Point Index')
plt.ylabel('Sepal Length (cm)')
plt.savefig('data-analysis-wk6/sepal_length_trend.png')
plt.close()

# 2. Bar Chart: Average petal length for each species
plt.figure(figsize=(10, 6))
species_petal_length = df.groupby('species')['petal_length'].mean().reset_index()
sns.barplot(x='species', y='petal_length', data=species_petal_length)
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.savefig('data-analysis-wk6/average_petal_length.png')
plt.close()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(10, 6))
sns.histplot(df['sepal_width'], kde=True, bins=20)
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.savefig('data-analysis-wk6/sepal_width_distribution.png')
plt.close()

# 4. Scatter Plot: Sepal length vs. petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.savefig('data-analysis-wk6/sepal_vs_petal_length.png')
plt.close()

print("---" + " Data visualizations have been generated and saved as PNG files. " + "---")
