import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns 
import pandas as pd

dst = pd.read_csv('E:\Capture\\toprich2024.csv', header=0, sep=",")
# print(dst)
# print(dst.columns)
# print(dst.info())
# print("Hasib",dst.describe())
# print("Shape",dst.shape)
print("Data Jog",dst['Total net worth '].mean)
print("Data Medium",dst['Total net worth '].median)
print("Data mode",dst['Total net worth '].mode)


top_10 = dst[['Rank', 'Total net worth ']].head(20)  # Adjust column names as needed

# Plotting the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Rank', y='Total net worth ', data=top_10, palette='viridis')  # Adjust column names as needed
plt.title('Top 10 Richest People')
plt.xlabel('Rank')
plt.ylabel('Total Net Worth (in billions)')  # Adjust the unit if needed
plt.xticks(rotation=45)  # Rotate the x-axis labels for readability
plt.tight_layout()  # Adjust layout for better visibility
plt.show()








