import matplotlib.pyplot as plt
import numpy as np

# Create an array of 1000 points between -pi and pi for a smoother plot
X = np.linspace(-np.pi, np.pi, 1000, endpoint=True)

# Calculate the tangent and cotangent (cot = 1/tan)
T = np.tan(X)
C = 1 / T  # Cotangent

# Avoid division by zero by setting values close to infinity to NaN
T[np.abs(T) > 10] = np.nan
C[np.abs(C) > 10] = np.nan

# Create a figure and axis
fig = plt.figure()

# Add an axis to the figure
ax = fig.add_subplot(111)

# Set axis limits, title, and labels
ax.set(xlim=[-3.14, 3.14], ylim=[-10, 10], 
       title='Tangent and Cotangent Functions', ylabel='Y-Axis', xlabel='X-Axis')

# Plot the tangent and cotangent functions
ax.plot(X, T, label='Tangent', color='blue', linewidth=2.5, linestyle='-.')  # Plot tangent in blue
ax.plot(X, C, label='Cotangent', color='red', linewidth=2.5, linestyle='-')    # Plot cotangent in red

# Add a legend to the plot
ax.legend()

# Show the plot
plt.show()
