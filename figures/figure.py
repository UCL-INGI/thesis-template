import matplotlib.pyplot as plt
import numpy as np

def latexify(fig_width=None, fig_height=None, columns=2):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples
    # also adapted from http://bkanuka.com/posts/native-latex-plots/

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    from math import sqrt
    import matplotlib

    assert(columns in [1,2])

    if fig_width is None:
        fig_width_pt = 341.43307                             # Get this from LaTeX using \the\textwidth
        inches_per_pt = 1.0 / 72.27                      # Convert pt to inch
        scale = 3.39 / 6.9 if columns == 1 else 1
        fig_width = fig_width_pt * inches_per_pt * scale # width in inches
        # fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large {}: so will reduce to {} inches.".format(fig_height, MAX_HEIGHT_INCHES))
        fig_height = MAX_HEIGHT_INCHES

    params = {'backend': 'ps',
              'text.latex.preamble': [r'\usepackage{libertine}', r'\usepackage[libertine]{newtxmath}', r'\usepackage[T1]{fontenc}', r'\usepackage{gensymb}'],
              'axes.labelsize': 12, # fontsize for x and y labels (was 10)
              'axes.titlesize': 12,
              'font.size': 12, # was 10
              'legend.fontsize': 12, # was 10
              'xtick.labelsize': 10,
              'ytick.labelsize': 10,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'pgf.texsystem': 'pdflatex',
              'grid.alpha': 0.25,
              'mathtext.default': 'regular', # Don't italize math text
              # 'font.family': 'serif'
    }

    matplotlib.rcParams.update(params)


def get_cdf_data(sample):
    sorted_array = np.sort(sample)
    yvals = np.arange(len(sorted_array)) / float(len(sorted_array))
    if len(sorted_array) > 0:
        # Add a last point
        sorted_array = np.append(sorted_array, sorted_array[-1])
        yvals = np.append(yvals, 1.0)
        # This allows keeping graphs low-sized
        # data = list(map(lambda x, y: (x, y), sorted_array, yvals))
        # data = [(x[0], x[1]) for i, x in enumerate(data) if i % 100 == 0 or x[0] > 1000.0]
        # sorted_array, yvals = [x[0] for x in data], [x[1] for x in data]

    return sorted_array, yvals


def plot_cdf(plt, sample, **kwargs):
    sample_x, sample_y = get_cdf_data(sample)
    line, = plt.plot(sample_x, sample_y, **kwargs)
    return line

def set_box_color(plt, bp, color):
    plt.setp(bp['boxes'], color=color, linewidth=1)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color, linewidth=1.25)
    plt.setp(bp['fliers'], color=color, marker='.')
