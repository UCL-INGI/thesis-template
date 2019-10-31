import matplotlib.pyplot as plt
import numpy as np

from figure import latexify

latexify()

x = np.linspace(-2,2,200)
curve_1 = x**2
curve_2 = x**3

fig = plt.figure()
plt.plot(x, curve_1, color="#bfbfbf", label="y = x$^2$")
plt.plot(x, curve_2, color="#000000", ls="--", label="y = x$^3$")
plt.legend(loc="lower right")
plt.xlim(xmin=-2, xmax=2)
plt.ylim(ymin=-8, ymax=8)
plt.xlabel("$x$ value")
plt.ylabel("$y$ value")
plt.grid()
plt.tight_layout()

plt.savefig("tips_plot_1.pgf")
