import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(num=None, figsize=(8, 8), dpi=80, facecolor='#212946', edgecolor='k')

RADIUS = 1 # Don't change
AMOUNT = 1000 # Points

x = np.linspace(-1,1, AMOUNT)
y = np.linspace(-1,1, AMOUNT)

x = np.random.choice(x, AMOUNT)
y = np.random.choice(y, AMOUNT)

CIRCLE_AREA = np.sqrt((x)**2 + (y)**2)
INSIDE = CIRCLE_AREA < RADIUS

OUTSIDE = CIRCLE_AREA > RADIUS

pi = 4*(x[INSIDE].size/(x[OUTSIDE].size+x[INSIDE].size))

for spine in ax.spines.values():
		spine.set_edgecolor('black')
		spine.set_linewidth(2)
		spine.set_capstyle("round")
textstr1 = (f"Points Total = {AMOUNT}\nPoints Inside = {x[INSIDE].size} \nPoints Outside = {x[OUTSIDE].size}")
textstr2 = (f"Pi = {pi}")
text_box = dict(boxstyle='round', facecolor='#2A3459', alpha=0.5)

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.patch.set_antialiased(True)
ax.set_facecolor("black")

OUTSIDE_PLOT = plt.scatter(x[OUTSIDE], y[OUTSIDE], s = .5, color="#08F7FE", label="Outside")
INSIDE_PLOT = plt.scatter(x[INSIDE], y[INSIDE], s = .5, color="#FE53BB", label="Inside")

plt.gca().set_aspect('equal')

legend = ax.legend(bbox_to_anchor=(1.022, 1.1), edgecolor="black", facecolor="#212946")

plt.setp(legend.get_texts(), color='#F5D300')

for handle in legend.legendHandles:
	handle.set_sizes([8.0])

plt.gca().add_artist(legend)

ax.text(-1, 1.05, textstr1, fontfamily="monospace", color="#F5D300", size=12, bbox=text_box)
ax.text(-.125, 1.1, textstr2, fontfamily="monospace", color="#F5D300", size=12, bbox=text_box)

plt.show()