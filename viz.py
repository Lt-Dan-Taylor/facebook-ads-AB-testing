import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
sns.set_style('ticks')

# Formatting to billion, million or thousand
def numeric_formatter(x, pos):
    if x >= 1e9:
        return f'{x/1e9:.1f} B'
    elif x >= 1e6:
        return f'{x/1e6:.1f} M'
    elif x >= 1e4:
        return f'{x/1e3:.1f} K'
    else:
         return str(int(x))

# Bar chart visualization
def bar_plot(ax, xcolumn, ycolumn, xlabel, ylabel, palette, fontsize):
    sns.barplot(ax=ax, x=xcolumn, y=ycolumn, palette=palette)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.yaxis.set_major_formatter(FuncFormatter(numeric_formatter))

# Histogram visiualiztion
def hist_plot(ax, df, xlabel, ylabel, color, fontsize):
    sns.histplot(ax=ax, data=df, color=color, bins=40)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

# ECDF chart visualization
def ecdf_plot(ax, column, hue, xlabel, ylabel, palette, fontsize):
    sns.ecdfplot(ax=ax, x=column, hue=hue, palette=palette, linewidth=2)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.xaxis.set_major_formatter(FuncFormatter(numeric_formatter))

# Boxplot visualization
def box_plot(ax, xcolumn, ycolumn, xlabel, ylabel, palette, fontsize):
    sns.boxplot(ax=ax, x=xcolumn, y=ycolumn, palette=palette)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.yaxis.set_major_formatter(FuncFormatter(numeric_formatter))

# Violinplot visualization
def violin_plot(ax, xcolumn, ycolumn, xlabel, ylabel, title, palette, fontsize):
    sns.violinplot(ax=ax, x=xcolumn, y=ycolumn, palette=palette)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=13)
    ax.yaxis.set_major_formatter(FuncFormatter(numeric_formatter))

# Line chart visualization
def line_plot(ax, xcolumn, ycolumn, color, marker, linestyle, linewidth, label, fontsize):
    sns.lineplot(ax=ax, x=xcolumn, y=ycolumn, label=label, color=color, marker=marker, markersize=10, ls=linestyle, lw=linewidth)
    ax.legend(fontsize=fontsize)
            
# Despine subplot
def despine_subplot(ax):
    sns.despine(bottom=False, left=True, top=True, right=True, trim=False, ax=ax)
    ax.set_yticks([])