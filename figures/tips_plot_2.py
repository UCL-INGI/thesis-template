import matplotlib.pyplot as plt
import numpy as np

from figure import latexify

latexify(fig_height=1.5)

x = np.linspace(-2,2,200)
curve_1 = x

fig = plt.figure()
plt.plot(x, curve_1, color="#000000", label="y = x")
plt.legend(loc="lower right")
plt.xlim(xmin=-2, xmax=2)
plt.ylim(ymin=-2, ymax=2)
plt.xlabel("$x$ value")
plt.ylabel("$y$ value")
plt.grid()
plt.tight_layout()

plt.savefig("tips_plot_2.pgf")
