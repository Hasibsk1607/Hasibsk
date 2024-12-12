import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='Quad')
ax.plot(x, x**3, label='Cube')

ax.set_xlabel('x_label')
ax.set_ylabel('y_label')

ax.set_title('Simple Plot')
ax.axhline(4, color='red', lw=1, alpha=1)
ax.legend()
ax.annotate('KUET', xy=(1,1), xytext=(50,50), textcoords='offset points', arrowprops=dict(facecolor='black', arrowstyle='<->'), fontsize=10)
ax.annotate('KUET', xy=(1,1), xytext=(150,150), textcoords='offset points', arrowprops=dict(facecolor='blue', arrowstyle='<->'), fontsize=10)
plt.show()


