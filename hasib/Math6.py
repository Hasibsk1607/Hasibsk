import matplotlib.pyplot as plt
import numpy as np

# Generate data for x values from 0 to 10
X = np.linspace(0, 10, 400)
Y_linear = X  # y = x
Y_quadratic = X**2  # y = x^2
Y_cubic = X**3  # y = x^3
Y_sin = np.sin(X)  # y = sin(x)

# Create a single plot
plt.figure(figsize=(8, 6))

# Plot the four lines with labels
line1, = plt.plot(X, Y_linear, label='Linear (y = x)', color='blue', linestyle='-', linewidth=2)
line2, = plt.plot(X, Y_quadratic, label='Quadratic (y = x^2)', color='green', linestyle='--', linewidth=2)
line3, = plt.plot(X, Y_cubic, label='Cubic (y = x^3)', color='red', linestyle='-.', linewidth=2)
line4, = plt.plot(X, Y_sin, label='Sine (y = sin(x))', color='purple', linestyle=':', linewidth=2)

# Add title and labels
plt.title('Multiple Lines in One Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Add a legend to distinguish the lines
plt.legend(title="Functions")

# Add annotations for each line (at specific points)

# Annotating for Linear Line
plt.annotate('Linear (y = x)', xy=(5, 5), xytext=(6, 6),
             arrowprops=dict(facecolor='blue', arrowstyle='->'),
             fontsize=12, color='blue')

# Annotating for Quadratic Line
plt.annotate('KUET', xy=(3, 9), xytext=(4, 25),
             arrowprops=dict(facecolor='green', arrowstyle='->'),
             fontsize=12, color='green')

# Annotating for Cubic Line
plt.annotate('NUW', xy=(2, 8), xytext=(3, 35),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=12, color='red')

# Annotating for Sine Line
plt.annotate('KU', xy=(5, np.sin(5)), xytext=(6, 1.5),
             arrowprops=dict(facecolor='purple', arrowstyle='->'),
             fontsize=12, color='purple')

# Show grid for better readability
plt.grid(True)

# Ensure everything fits in the plot area
plt.tight_layout()

# Show the plot
plt.show()
