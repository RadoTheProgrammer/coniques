import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Paramètres initiaux de la droite : y = a*x + b
a = 1
b = 0
x_vals = np.array([-5, 5])
y_vals = a * x_vals + b
line, = ax.plot(x_vals, y_vals, 'g-', linewidth=2)

# Variables de suivi
dragging = False
last_event = None

def update_line(dx, dy):
    global a, b, x_vals, y_vals
    # Translate la droite verticalement (modifie l'ordonnée à l'origine)
    b_new = b + dy
    y_new = a * x_vals + b_new
    line.set_ydata(y_new)
    fig.canvas.draw_idle()

def on_press(event):
    global dragging, last_event
    if line.contains(event)[0]:
        dragging = True
        last_event = event

def on_release(event):
    global dragging
    dragging = False

def on_motion(event):
    global dragging, last_event, b
    if dragging and event.xdata is not None and event.ydata is not None:
        dy = event.ydata - last_event.ydata
        #b += dy
        b = event.ydata - a * event.xdata
        y_vals = a * x_vals + b
        line.set_ydata(y_vals)
        last_event = event
        fig.canvas.draw_idle()

# Lier les événements souris
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

plt.title("Clique et déplace la droite verte")
plt.grid()
plt.show()
