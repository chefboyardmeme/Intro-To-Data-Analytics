import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the provided file path
data = pd.read_csv('Covid.csv')

# Display basic information about the dataset
print(data.info())

# Descriptive Analysis

## Describe data characteristics
print("\nData Characteristics:")
print(data.describe())

## Descriptive statistics for key attributes
print("\nDescriptive Statistics for Key Attributes:")
print(data.groupby(['Sex']).describe())  # Example: Group by 'Sex'

## Visualizations

### Bar chart for deaths by age group and sex
plt.figure(figsize=(10, 6))
sns.barplot(x='Age Group', y='COVID-19 Deaths', hue='Sex', data=data)
plt.title('COVID-19 Deaths by Age Group and Sex')
plt.xlabel('Age Group')
plt.ylabel('Number of Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

### Box plot for deaths by sex
plt.figure(figsize=(8, 6))
sns.boxplot(x='Sex', y='COVID-19 Deaths', data=data)
plt.title('COVID-19 Deaths by Sex')
plt.xlabel('Sex')
plt.ylabel('Number of Deaths')
plt.tight_layout()
plt.show()

### Scatter plot for exploring interactions
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age Group', y='COVID-19 Deaths', hue='Sex', data=data)
plt.title('COVID-19 Deaths by Age Group and Sex')
plt.xlabel('Age Group')
plt.ylabel('Number of Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()