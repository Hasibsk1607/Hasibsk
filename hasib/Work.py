import pandas as pd

# ডেটা প্রস্তুত করা
data = {
    'ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'CGPA': [3.7, 3.4, 3.8, 3.6, 3.9, 3.5, 3.7, 3.2, 3.6, 3.8],
    'Department': ['CSE', 'EEE', 'ME', 'CSE', 'BBA', 'EEE', 'CSE', 'BBA', 'EEE', 'CSE']
}

# DataFrame তৈরি করা
df = pd.DataFrame(data)
sd = df[df['Name'] == 'Frank'][['ID', 'Name']]
print(sd)
# DataFrame প্রিন্ট করা
print(df)

# CGPA এর গড় (average) বের করা
average_cgpa = df['CGPA'].mean()
max_cgpa = df['CGPA'].max()
min_cgpa = df['CGPA'].min()
department_stats = df.groupby('Department')['CGPA'].agg(['min', 'max'])
department_avg_cgpa = df.groupby('Department')[['CGPA']].mean()

# গড় CGPA প্রিন্ট করা
print(f"Average CGPA: {average_cgpa:.2f}")
print(f"Max CGPA: {max_cgpa}")
print(f"Max CGPA: {min_cgpa}")
print(department_stats)
print(department_avg_cgpa)

