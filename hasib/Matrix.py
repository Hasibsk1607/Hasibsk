import matplotlib.pyplot as plt
import numpy as np
import time
start_time = time.time()

# Create some sample data
X = np.linspace(-np.pi, np.pi, 100)
C = np.cos(X)
S = np.sin(X)

# Create a figure
fig = plt.figure(figsize=(10, 8))

# Add the first subplot (1 row, 2 columns, 1st plot)
ax1 = fig.add_subplot(221)  # 2 rows, 2 columns, 1st plot (top-left)
ax1.plot(X, C, label='Cosine', color='blue')
ax1.set_title('Cosine Function')
ax1.set_xlabel('X-Axis')
ax1.set_ylabel('Y-Axis')
ax1.legend()

# Add the second subplot (1 row, 2 columns, 2nd plot)
ax2 = fig.add_subplot(222)  # 2 rows, 2 columns, 2nd plot (top-right)
ax2.plot(X, S, label='Sine', color='red')
ax2.set_title('Sine Function')
ax2.set_xlabel('X-Axis')
ax2.set_ylabel('Y-Axis')
ax2.legend()

# Add the third subplot (1 row, 2 columns, 3rd plot)
ax3 = fig.add_subplot(223)  # 2 rows, 2 columns, 3rd plot (bottom-left)
ax3.plot(X, C + S, label='Cosine + Sine', color='green')
ax3.set_title('Cosine + Sine')
ax3.set_xlabel('X-Axis')
ax3.set_ylabel('Y-Axis')
ax3.legend()

# Add the fourth subplot (1 row, 2 columns, 4th plot)
ax4 = fig.add_subplot(224)  # 2 rows, 2 columns, 4th plot (bottom-right)
ax4.plot(X, C - S, label='Cosine - Sine', color='purple')
ax4.set_title('Cosine - Sine')
ax4.set_xlabel('X-Axis')
ax4.set_ylabel('Y-Axis')
ax4.legend()

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()

end_time = time.time()

# Print the runtime
print(f"Code execution time: {end_time - start_time} seconds")
