import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.title("Déplace les deux points pour modifier la droite")

# Points initiaux
point1_coords = np.array([-2, -1])
point2_coords = np.array([2, 2])

# Affichage des points
point1, = ax.plot(*point1_coords, 'ro', markersize=10, picker=5)
point2, = ax.plot(*point2_coords, 'bo', markersize=10, picker=5)

# Affichage de la droite entre les deux points
line, = ax.plot(
    [point1_coords[0], point2_coords[0]],
    [point1_coords[1], point2_coords[1]],
    'g-', linewidth=2
)

# Suivi de quel point est en cours de déplacement
dragging_point = None

def update_line():
    """Met à jour la droite selon les deux points."""
    x_vals = [point1.get_xdata()[0], point2.get_xdata()[0]]
    y_vals = [point1.get_ydata()[0], point2.get_ydata()[0]]
    line.set_data(x_vals, y_vals)
    fig.canvas.draw_idle()

def on_press(event):
    global dragging_point
    if event.inaxes != ax:
        return

    if point1.contains(event)[0]:
        dragging_point = point1
    elif point2.contains(event)[0]:
        dragging_point = point2

def on_release(event):
    global dragging_point
    dragging_point = None

def on_motion(event):
    if dragging_point is None or event.xdata is None or event.ydata is None:
        return
    dragging_point.set_data([event.xdata], [event.ydata])
    update_line()

# Connexion des événements
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

plt.grid()
plt.show()
