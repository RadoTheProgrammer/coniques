import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math
# Étape 1 : Créer une grille
zoom = 5
xlim = (-zoom,zoom)
ylim = (-zoom,zoom)

F = (0,0) # foyer
P1, P2 = (-1,0), (0,1) # droite directrice
e_min, e_max,e = 0, 100, 0.5 # excentricité


def update_slider(val):
    global e
    e=val
    update()

def update():
    global foyer,d_equ,cs,P1,P2


    # droite directrice
    if P1[0] == P2[0]:
        d_equ = {"a":1,"b":0,"c":-P1[0]}
        #print(d_equ)
        x_vals = [P1[0], P1[0]]
        y_vals = ylim
    else:
        m = (P2[1]-P1[1]) / (P2[0]-P1[0])
        h = P1[1] - m * P1[0]
        d_equ = {"a":m, "b":-1, "c":h}
        x_vals = np.array(xlim)
        y_vals = m * x_vals + h

    d_plot.set_data(x_vals, y_vals)
    foyer.set_data([F[0]],[F[1]])
    P1_plot.set_data([P1[0]],[P1[1]])
    P2_plot.set_data([P2[0]],[P2[1]])
    print(d_plot)
    Z = evaluate(X, Y)
    if cs:
        cs.remove()
    cs=ax.contour(X, Y, Z, levels=[e], colors=['blue'])

    fig.canvas.draw_idle()
    
def evaluate(x,y):
    """
    Return e = d(P,F)/d(P,d)
    Retourne l'excentricité pour lequel le point est sur la conique
    """
    dpf = np.sqrt((x-F[0])**2+(y-F[1])**2)
    dpd = abs(d_equ["a"]*x+d_equ["b"]*y+d_equ["c"]) / np.sqrt(d_equ["a"]**2 + d_equ["b"]**2)
    return dpf*dpd
    #return dpf/dpd



def on_press(event):
    global dragging_foyer,dragging_point

    if foyer.contains(event)[0]:
        dragging_foyer = True
    elif P1_plot.contains(event)[0]:
        dragging_point = 1
    elif P2_plot.contains(event)[0]:
        dragging_point = 2

def on_release(event):
    global dragging_foyer, dragging_point
    dragging_foyer = False
    dragging_point = 0

def on_motion(event):
    global F, P1, P2
    if event.xdata is not None and event.ydata is not None:
        if dragging_foyer:
            F = (event.xdata,event.ydata)
        elif dragging_point==1:
            P1 = (event.xdata,event.ydata)
        elif dragging_point==2:
            P2 = (event.xdata,event.ydata)
        update()
cs = None
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

d_plot, = ax.plot([],[],'r-', linewidth=2)
dragging_foyer = False
dragging_point = 0

ax_e_slider = plt.axes((0.25, 0.1, 0.65, 0.03))
e_slider = Slider(
    ax=ax_e_slider,
    label="excentricity",
    valmin=e_min,
    valmax=e_max,
    valinit=e,
    valstep=0.01
)

x = np.linspace(*xlim, 400)
y = np.linspace(*ylim, 400)
X, Y = np.meshgrid(x, y)

foyer, = ax.plot(F[0], F[1], 'go', label='Foyer F')
P1_plot, = ax.plot(*P1, "ro")
P2_plot, = ax.plot(*P2, "ro")
update()
#line.set_data([-1, -1], (-5, 5))
e_slider.on_changed(update_slider)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)



plt.show()
