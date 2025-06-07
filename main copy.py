import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math
# Étape 1 : Créer une grille
zoom = 5
xlim = (-zoom,zoom)
ylim = (-zoom,zoom)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
F = (0,0) # foyer
P1, P2 = (-1,0), (-1,1) # droite directrice
line, = ax.plot(xlim,ylim, 'g-', linewidth=2)
#line.set_data([-1, -1], (-5, 5))
#line, = ax.plot([-1],[-5], 'g-', linewidth=2)
#line.set_data([-1, -1],[-5, 5])
d = {"a":1,"b":0,"c":5} # droite directrice (a,b,c) tq ax+by+c=0 
#e = (6,6.25,7)
e_min, e_max,e = 0, 2, 0.5 # excentricité
dragging_foyer = False


ax_e_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
e_slider = Slider(
    ax=ax_e_slider,
    label="excentricity",
    valmin=e_min,
    valmax=e_max,
    valinit=e,
    valstep=0.01
)

def update_slider(val):
    global e
    e=val
    update()

def update():
    global foyer,droite_directrice

    Z = evaluate(X, Y)

    # droite directrice


    line.set_data([-1, -1], (-5, 5))
    foyer, = ax.plot(F[0], F[1], 'go', label='Foyer F')
    ax.text(F[0]+0.2, F[1], 'F', color='green')
    contours = ax.contour(X, Y, Z, levels=[e], colors=['blue'])

    ax.set_aspect('equal')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    fig.canvas.draw_idle()
    
def evaluate(x,y):
    """
    Return e = d(P,F)/d(P,d)
    Retourne l'excentricité pour lequel le point est sur la conique
    """
    dpf = np.sqrt((x-F[0])**2+(y-F[1])**2)
    dpd = abs(d["a"]*x+d["b"]*y+d["c"]) / np.sqrt(d["a"]**2 + d["b"]**2)
    return dpf/dpd

def droite_directrice(x,y):
    return d["a"]*x+d["b"]*y+d["c"]

def on_press(event):
    global dragging_foyer
    contains, _ = foyer.contains(event)
    if contains:
        dragging_foyer = True

def on_release(event):
    global dragging_foyer
    dragging_foyer = False

def on_motion(event):
    global F
    if dragging_foyer and event.xdata is not None and event.ydata is not None:
        F = (event.xdata,event.ydata)
        update()

x = np.linspace(*xlim, 400)
y = np.linspace(*ylim, 400)
X, Y = np.meshgrid(x, y)
update()
#line.set_data([-1, -1], (-5, 5))
e_slider.on_changed(update_slider)

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)



plt.show()
