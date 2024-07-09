import matplotlib as mpl

def set_plot_params():
    mpl.rcParams['lines.linewidth'] = 1.5
    mpl.rcParams['lines.linestyle'] = '-'
    mpl.rcParams['axes.grid'] = True
    mpl.rcParams['grid.alpha'] = 0.5
    mpl.rcParams['xtick.top'] = True
    mpl.rcParams['ytick.right'] = True 
    mpl.rcParams['xtick.minor.visible'] = True
    mpl.rcParams['ytick.minor.visible'] = True
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    mpl.rcParams['lines.marker'] = ''