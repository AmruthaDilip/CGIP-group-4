import matplotlib.pyplot as plt
import numpy as np

# define the point (x, y)
x = 1
y = 1

# define the angle of rotation in radians
theta = np.pi / 4  # 45 degrees in radians

# create a rotation matrix
rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                       [np.sin(theta), np.cos(theta)]])

# apply the rotation to the point
rotated_point = rot_matrix @ np.array([x, y])

# plot the original and rotated points
fig, ax = plt.subplots()
ax.plot(x, y, 'ro', label='Original point')
ax.plot(rotated_point[0], rotated_point[1], 'bo', label='Rotated point')
ax.axis('equal')
ax.legend()
plt.show()