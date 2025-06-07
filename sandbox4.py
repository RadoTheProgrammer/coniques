import numpy as np
import matplotlib.pyplot as plt

# Example data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Create contour
contours = plt.contour(X, Y, Z, levels=[0])
print(contours.levels)
contours.remove()
# Extract x and y values of contour lines
# x_vals_all = []
# y_vals_all = []

# for collection in contours.collections:
#     for path in collection.get_paths():
#         v = path.vertices
#         x_vals_all.append(v[:, 0])
#         y_vals_all.append(v[:, 1])

# # Now you can plot with plt.plot if needed
# for x_vals, y_vals in zip(x_vals_all, y_vals_all):
#     plt.plot(x_vals, y_vals, color='black', linewidth=1)

plt.title("Contour Lines via plt.plot")
plt.show()
