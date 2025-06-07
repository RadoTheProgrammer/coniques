import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.title("Déplace les points rouges pour orienter la droite infinie")


# Affichage des points
x1,y1 = (-2,-1)
x2,y2 = (2, 2)
point1, = ax.plot(x1,y1, 'ro', markersize=10)
point2, = ax.plot(x2,y2, 'ro', markersize=10)

# Affichage de la droite (prolongée)
line, = ax.plot([], [], 'g-', linewidth=2)

# Suivi du point qu'on déplace
dragging_point = None

def update_line():
    """Trace une droite infinie passant par les deux points."""
    global x1,x2,y1,y2,y_vals
    x1, y1 = point1.get_data()
    x2, y2 = point2.get_data()
    x1,y1,x2,y2 = x1[0],y1[0],x2[0],y2[0]
    # Calcul de la pente (évite division par zéro)
    x2 = x1
    if x1 == x2:
        # Droite verticale
        print("AIE")
        x_vals = [x1, x1]
        y_vals = ax.get_ylim()
    else:
        # Droite avec pente
        print(y2,y1)
        print(type(y1),type(y2))
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1

        x_vals = np.array(ax.get_xlim())
        y_vals = a * x_vals + b

    line.set_data(x_vals, y_vals)
    fig.canvas.draw_idle()

update_line()

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

# Connexion des événements souris
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

plt.grid()
plt.show()
