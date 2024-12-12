import matplotlib.pyplot as plt
import numpy as np

# Create an array of 10 points between -pi and pi
X = np.linspace(-np.pi, np.pi, 10, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Create a figure and axis
fig = plt.figure()

# Add an axis to the figure
ax = fig.add_subplot(111)

# Set axis limits, title, and labels
ax.set(xlim=[-3.14, 3.14], ylim=[-2, 2], 
       title='An Example Axis', ylabel='Y-Axis', xlabel='X-Axis')

# Plot the cosine and sine functions
ax.plot(X, C, label='Cosine', color='blue', linewidth=2.5, linestyle='-.')  # Plot cosine in blue
ax.plot(X, S, label='Sine', color='red', linewidth=2.5, linestyle='-')    # Plot sine in red

# Add a legend to the plot
ax.legend()

# Show the plot
plt.show()
