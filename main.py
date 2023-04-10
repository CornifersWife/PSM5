import math

from matplotlib import pyplot as plt
import numpy as np
from CelestialBody import CelestialBody

dt = 600
t_max = 3600 * 24 * 500

color_map = plt.get_cmap('rainbow')

fig, ax = plt.subplots()

ax.set_aspect('equal')


xd = CelestialBody()
xd_2 = CelestialBody()
times, x_positions, y_positions = xd.euler_movement(dt, t_max)

colors = np.array([color_map(i/len(times)) for i in range(len(times))])[::-1]




#ax.scatter(x_positions, y_positions, s=1, c='black',alpha=0.05)

times, x_positions, y_positions = xd_2.euler_movement_2(dt, t_max)
ax.scatter(x_positions, y_positions, s=1, c=colors,alpha=0.05)

# Add labels and title
ax.set_xlabel('X position')
ax.set_ylabel('Y position')
ax.set_title('Positions over Time')

# Show the plot
plt.show()
