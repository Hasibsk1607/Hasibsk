import matplotlib.pyplot as plt
import numpy as np

# Create an array of 1000 points between -2*pi and 2*pi
X = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Sine and cosine functions with different transformations
sin_1 = np.sin(X)
cos_1 = np.cos(X)

sin_2 = 2 * np.sin(X)  # Sine with larger amplitude
cos_2 = 2 * np.cos(X)  # Cosine with larger amplitude

sin_3 = np.sin(2 * X)  # Sine with doubled frequency
cos_3 = np.cos(2 * X)  # Cosine with doubled frequency

sin_4 = np.sin(X + np.pi / 4)  # Sine with phase shift
cos_4 = np.cos(X + np.pi / 4)  # Cosine with phase shift

# Create a figure with 4 subplots (2 rows and 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# First subplot: Basic Sine and Cosine
axs[0, 0].plot(X, sin_1, label='Sine', color='blue')
axs[0, 0].plot(X, cos_1, label='Cosine', color='red')
axs[0, 0].set_title('Basic Sine and Cosine')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].legend()

# Second subplot: Sine and Cosine with larger amplitude
axs[0, 1].plot(X, sin_2, label='Sine (Amplitude 2)', color='green')
axs[0, 1].plot(X, cos_2, label='Cosine (Amplitude 2)', color='purple')
axs[0, 1].set_title('Sine and Cosine with Larger Amplitude')
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Y-axis')
axs[0, 1].legend()

# Third subplot: Sine and Cosine with doubled frequency
axs[1, 0].plot(X, sin_3, label='Sine (Frequency 2)', color='orange')
axs[1, 0].plot(X, cos_3, label='Cosine (Frequency 2)', color='brown')
axs[1, 0].set_title('Sine and Cosine with Doubled Frequency')
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Y-axis')
axs[1, 0].legend()

# Fourth subplot: Sine and Cosine with phase shift
axs[1, 1].plot(X, sin_4, label='Sine (Phase Shift)', color='cyan')
axs[1, 1].plot(X, cos_4, label='Cosine (Phase Shift)', color='magenta')
axs[1, 1].set_title('Sine and Cosine with Phase Shift')
axs[1, 1].set_xlabel('X-axis')
axs[1, 1].set_ylabel('Y-axis')
axs[1, 1].legend()

# Adjust layout to make it look nice
plt.tight_layout()

# Show the plot
plt.show()
