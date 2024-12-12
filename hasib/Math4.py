import matplotlib.pyplot as plt
import numpy as np

# Create an array of 1000 points between -pi and pi
X = np.linspace(-np.pi, np.pi, 1000, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Create a figure and set up 4 subplots in a 2x2 grid
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# First subplot: Basic Cosine and Sine
axs[0, 0].plot(X, C, label='Cosine', color='blue', linewidth=2.5, linestyle='-.')
axs[0, 0].plot(X, S, label='Sine', color='red', linewidth=2.5, linestyle='-')
axs[0, 0].set_title('Basic Cosine and Sine')
axs[0, 0].set_xlabel('X-Axis')
axs[0, 0].set_ylabel('Y-Axis')
axs[0, 0].legend()

# Second subplot: Cosine and Sine with Larger Amplitude
axs[0, 1].plot(X, 2 * C, label='Cosine (Amplitude 2)', color='green', linewidth=2.5, linestyle='-.')
axs[0, 1].plot(X, 2 * S, label='Sine (Amplitude 2)', color='purple', linewidth=2.5, linestyle='-')
axs[0, 1].set_title('Cosine and Sine with Larger Amplitude')
axs[0, 1].set_xlabel('X-Axis')
axs[0, 1].set_ylabel('Y-Axis')
axs[0, 1].legend()

# Third subplot: Cosine and Sine with Doubled Frequency
axs[1, 0].plot(X, np.cos(2 * X), label='Cosine (Frequency 2)', color='orange', linewidth=2.5, linestyle='-.')
axs[1, 0].plot(X, np.sin(2 * X), label='Sine (Frequency 2)', color='brown', linewidth=2.5, linestyle='-')
axs[1, 0].set_title('Cosine and Sine with Doubled Frequency')
axs[1, 0].set_xlabel('X-Axis')
axs[1, 0].set_ylabel('Y-Axis')
axs[1, 0].legend()

# Fourth subplot: Cosine and Sine with Phase Shift
axs[1, 1].plot(X, np.cos(X + np.pi / 4), label='Cosine (Phase Shift)', color='cyan', linewidth=2.5, linestyle='-.')
axs[1, 1].plot(X, np.sin(X + np.pi / 4), label='Sine (Phase Shift)', color='magenta', linewidth=2.5, linestyle='-')
axs[1, 1].set_title('Cosine and Sine with Phase Shift')
axs[1, 1].set_xlabel('X-Axis')
axs[1, 1].set_ylabel('Y-Axis')
axs[1, 1].legend()

# Adjust layout to make sure the subplots don't overlap
plt.tight_layout()

# Show the plot
plt.show()
