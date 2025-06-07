import matplotlib.pyplot as plt
import numpy as np

# Création de la figure et des axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Un point qu'on pourra déplacer
point, = ax.plot(0,0, 'ro', markersize=10)

# Une ligne qui dépend de la position du point (ici juste pour illustrer)
line, = ax.plot([], [], 'b--')

# Fonction de mise à jour du graphe
def update_lines(x, y):
    # Par exemple, on trace une ligne entre l'origine et le point
    line.set_data([0, x], [0, y])
    fig.canvas.draw_idle()

update_lines(0, 0)  # Initialisation

# Variables de suivi
dragging = False

def on_press(event):
    print("on_press")
    global dragging,contains,c2
    # Si clic proche du point rouge
    contains, c2 = point.contains(event)
    if contains:
        dragging = True

def on_release(event):
    print("on_release")
    global dragging
    dragging = False

def on_motion(event):
    print("on_release")
    print(event)
    #print(dir(event))
    global dragging
    if dragging and event.xdata is not None and event.ydata is not None:
        # Met à jour la position du point
        point.set_data([event.xdata], [event.ydata])
        update_lines(event.xdata, event.ydata)

# Connexion des événements
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

plt.title("Déplace le point rouge avec la souris")
plt.grid()
plt.show()
