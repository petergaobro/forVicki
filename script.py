import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the heart shape in parametric form
def heart_shape(t):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    z = np.sin(t) * np.abs(np.sin(t)) * 5  # Adding some 3D height variation
    return x, y, z

# Generate points for the heart
t = np.linspace(0, 2 * np.pi, 1000)
x, y, z = heart_shape(t)

# Initial plot
line, = ax.plot(x, y, z, color='pink')

# Set limits for better visualization
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-10, 10])

# Animation function
def update(num):
    ax.view_init(elev=10., azim=num)  # Rotate the view for the animation
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=range(0, 360, 2), interval=50)

# Show plot
plt.show()
