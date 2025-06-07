import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Création de la figure et de l'axe
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Données initiales
x = np.linspace(0, 2 * np.pi, 400)
freq_init = 1
y = np.sin(freq_init * x)
line, = ax.plot(x, y)

# Position et paramètres du curseur

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax=ax_slider,
    label='Fréquence',
    valmin=0,
    valmax=2,
    valinit=freq_init,
    valstep=0.01,
)

# Fonction de mise à jour appelée à chaque changement de valeur du curseur
def update(val):
    print(val)
    freq = slider.val
    line.set_ydata(np.sin(freq * x))
    fig.canvas.draw_idle()

# Lier la fonction de mise à jour au curseur
slider.on_changed(update)

# Afficher
plt.show()

