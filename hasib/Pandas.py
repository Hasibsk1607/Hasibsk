import pandas as pd
import matplotlib.pyplot as plt

# 10 ওভার এর ডেটা
data = {
    'Over': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Runs': [8, 12, 15, 7, 10, 14, 9, 20, 6, 11],
    'Wickets': [0, 0, 1, 1, 0, 1, 1, 2, 0, 3]
}

# DataFrame তৈরি
df = pd.DataFrame(data)

# DataFrame প্রিন্ট করা
print(df)

# Runs এবং Wickets এর জন্য Bar Graph তৈরি করা

# এক্সাক্টলি দুটি বার প্লট তৈরি করবো: একটিতে Runs, আরেকটিতে Wickets
fig, ax = plt.subplots(figsize=(10,6))

# Runs এর জন্য বার গ্রাফ
df.plot(x='Over', y='Runs', kind='bar', ax=ax, position=1, width=0.4, color='blue', label='Runs')

# Wickets এর জন্য বার গ্রাফ
df.plot(x='Over', y='Wickets', kind='bar', ax=ax, position=0, width=0.4, color='red', label='Wickets')

# x এবং y- axis এর লেবেল
ax.set_xlabel('Over')
ax.set_ylabel('Runs/Wickets')

# গ্রাফের টাইটেল
plt.title('Cricket Match Score (Bar Graph)')

# লেজেন্ড (legend) দেখানো
plt.legend()

# গ্রাফ দেখানো
plt.show()
