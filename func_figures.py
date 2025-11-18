import numpy as np
from matplotlib.transforms import Affine2D
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import AutoMinorLocator
from func_colors import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.colors import to_rgb
from matplotlib.colors import LinearSegmentedColormap
from numpy import polyfit, linspace, rad2deg, arctan
from func_basics import get_nearest_index
from matplotlib.gridspec import GridSpec
import matplotlib.transforms as transforms

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'
plt.rcParams['savefig.facecolor'] = 'white'

ttfs, axfs, tkfs = 17, 15, 13


def set_frame_style(axis, title='', double_axis=False, xtick_fontsize=tkfs, ytick_fontsize=tkfs, grid=False, title_fontsize=ttfs, xlabel='X', xlabel_fontsize=axfs, ylabel='Y', ylabel_fontsize=axfs,\
                    x_labelpad=10, y_labelpad=10, linewidth=0.7, is_minortick=True,\
                    tick_linewidth=1, minor_tick_linewidth=0.8, \
                    tick_length=1.5, minor_tick_length=1, style='thin', \
                    xtick_rotation=0, ytick_rotation=0,\
                    **kwargs):
    
    if is_minortick==True:
        axis.xaxis.set_minor_locator(AutoMinorLocator())
        axis.yaxis.set_minor_locator(AutoMinorLocator())
    title_fontsize = kwargs.get('ttfs', title_fontsize)
    xlabel_fontsize = kwargs.get('xlfs', xlabel_fontsize)
    ylabel_fontsize = kwargs.get('ylfs', ylabel_fontsize)
    xtick_fontsize = kwargs.get('xtkfs', xtick_fontsize)
    ytick_fontsize = kwargs.get('ytkfs', ytick_fontsize)
    xlabel = kwargs.get('xl', xlabel)
    ylabel = kwargs.get('yl', ylabel)
    if style == 'thick':
        linewidth=1.5
        tick_linewidth=1.5
        tick_length=5
        minor_tick_length=3
        minor_tick_linewidth=1.

    if grid:
        axis.grid(c='grey', alpha=0.1, lw=0.3)
    axis.tick_params(axis="x", which="major", direction="in", labelsize=xtick_fontsize, length=tick_length, width=tick_linewidth, labelrotation=xtick_rotation)
    axis.tick_params(axis="y", which="major", direction="in", labelsize=ytick_fontsize, length=tick_length, width=tick_linewidth, labelrotation=ytick_rotation)
    if is_minortick==True:
        axis.tick_params(axis="x", which="minor", direction="in", labelsize=xtick_fontsize, length=minor_tick_length, width=minor_tick_linewidth, labelrotation=xtick_rotation)
        axis.tick_params(axis="y", which="minor", direction="in", labelsize=ytick_fontsize, length=minor_tick_length, width=minor_tick_linewidth, labelrotation=ytick_rotation)
    elif is_minortick==False:
        pass
    
    if not double_axis:
        # axis_x2 = axis.secondary_xaxis('top')
        axis.tick_params(axis="x", which="major", direction="in", labelsize=xtick_fontsize, length=tick_length, width=tick_linewidth, labeltop=False, labelrotation=xtick_rotation)
        if is_minortick==True:
            axis.tick_params(axis="x", which="minor", direction="in", labelsize=xtick_fontsize, length=minor_tick_length, width=minor_tick_linewidth, labeltop=False, labelrotation=xtick_rotation)
            axis.xaxis.set_minor_locator(AutoMinorLocator())
        axis.xaxis.set_ticks_position('both')

        # axis_y2 = axis.secondary_yaxis('right')
        axis.tick_params(axis="y", which="major", direction="in", labelsize=ytick_fontsize, length=tick_length, width=tick_linewidth, labelright=False, labelrotation=ytick_rotation)
        if is_minortick==True:
            axis.tick_params(axis="y", which="minor", direction="in", labelsize=ytick_fontsize, length=minor_tick_length, width=minor_tick_linewidth, labelright=False, labelrotation=ytick_rotation)
            axis.yaxis.set_minor_locator(AutoMinorLocator())
        axis.yaxis.set_ticks_position('both')

    axis.set_title(f'{title}', fontsize=title_fontsize, y=1.05)
    axis.set_xlabel(f'{xlabel}', fontsize=xlabel_fontsize, labelpad=x_labelpad)
    
    
    axis.set_ylabel(f'{ylabel}', fontsize=ylabel_fontsize, labelpad=y_labelpad)
    
    
    # axis.xaxis.labelpad = 9
    # axis.yaxis.labelpad = 9
    for ax_i in ['top','bottom','left','right']:
        axis.spines[ax_i].set_linewidth(linewidth)
        


def set_textbox(axis, text, position, fontsize=10, edge=False, facecolor='k', fontcolor='k', 
                edgecolor='k', alpha=0, rotation=0, edgelinewidth=0.8, zorder=999, fontweight='light'):
    
    if edge == False:
        props = dict(boxstyle='square', facecolor=facecolor, alpha=alpha, linewidth=0, edgecolor=edgecolor)
    else:
        props = dict(boxstyle='square', facecolor=facecolor, alpha=alpha, linewidth=edgelinewidth, edgecolor=edgecolor)
    
    textbox = axis.text(position[0], position[1], text, transform=axis.transAxes, fontsize=fontsize, \
                        color=fontcolor, rotation=rotation, zorder=zorder, fontweight=fontweight, \
                        verticalalignment='center', horizontalalignment='center', bbox=props)



def set_legend_style(axis, ncols=1, frame=False, legend_title='', position='best', legend_fontsize=tkfs-1.5,  legend_title_fontsize=tkfs-1.5, frame_linewidth=0.6, handles=None, labelspacing=0.2, **kwargs):
    
    position = kwargs.get('pos', position)
    legend_title = kwargs.get('lt', legend_title)
    legend_fontsize = kwargs.get('lfs', legend_fontsize)
    legend_title_fontsize = kwargs.get('ltfs', legend_title_fontsize)

    if position is tuple:
        if legend_title is not None:
            set_legend = axis.legend(fontsize=legend_fontsize, ncol=ncols, frameon=frame, bbox_to_anchor=position, framealpha=1, borderpad=0.02, labelspacing=labelspacing, title=legend_title, title_fontsize=legend_title_fontsize, handles=handles,\
                                    handlelength=1.75, columnspacing=1)
        elif legend_title == None and legend_title_fontsize == None:
            set_legend = axis.legend(fontsize=legend_fontsize, ncol=ncols, frameon=frame, bbox_to_anchor=position, framealpha=1, borderpad=0.02, labelspacing=labelspacing, handles=handles,\
                                    handlelength=1.75, columnspacing=1)
    else:
        if legend_title is not None:
            set_legend = axis.legend(fontsize=legend_fontsize, ncol=ncols, frameon=frame, loc=position, framealpha=1, borderpad=0.02, labelspacing=labelspacing, title=legend_title, title_fontsize=legend_title_fontsize, handles=handles,\
                                    handlelength=1.75, columnspacing=1)
        elif legend_title == None and legend_title_fontsize == None:
            set_legend = axis.legend(fontsize=legend_fontsize, ncol=ncols, frameon=frame, loc=position, framealpha=1, borderpad=0.02, labelspacing=labelspacing, handles=handles,\
                                    handlelength=1.75, columnspacing=1)
    legend_frame = set_legend.get_frame()
    legend_frame.set_linewidth(frame_linewidth)
    legend_frame.set_edgecolor('k')
    legend_frame.set_boxstyle('square')   

        

def set_bounds(axis, x_bound, y_bound):
    axis.set_xlim(x_bound)
    axis.set_ylim(y_bound)


def set_box(axis, x_dim, y_dim, edgecolor=None, facecolor=None, alpha=1, hatch=None, lw=1, fill=True, ls='-', zorder=99):
    axis.add_patch(patches.Rectangle(
                                    (x_dim[0], y_dim[0]),
                                    x_dim[1]-x_dim[0],
                                    y_dim[1]-y_dim[0],
                                    edgecolor = edgecolor,
                                    facecolor = facecolor,
                                    alpha=alpha,
                                    fill=fill,
                                    hatch=hatch,
                                    zorder=zorder,
                                    lw=lw,
                                    ls=ls
                                    )
                    )


def set_axis_color(axis, auxilary_axis, color, auxilary_color, axis_position='left', auxilary_position='right', is_minortick=True):
    if is_minortick==True:
        axis.xaxis.set_minor_locator(AutoMinorLocator())
        axis.yaxis.set_minor_locator(AutoMinorLocator())
        auxilary_axis.xaxis.set_minor_locator(AutoMinorLocator())
        auxilary_axis.yaxis.set_minor_locator(AutoMinorLocator())
    for ax_i in ['top','bottom','left','right']:
        axis.spines[ax_i].set_linewidth(0.7)
    for ax_i in ['top','bottom','left','right']:
        auxilary_axis.spines[ax_i].set_linewidth(0.7)
    axis.spines[axis_position].set_color(color)    
    auxilary_axis.spines[axis_position].set_color(color)
    auxilary_axis.spines[auxilary_position].set_color(auxilary_color)

    axis.xaxis.set_ticks_position('both')
    axis.yaxis.label.set_color(color)
    axis.tick_params(axis="y", which="major", direction="in", colors=color, length=3, width=1, top=True)
    axis.tick_params(axis="y", which="minor", direction="in", colors=color, length=1.5, width=0.8, top=True)
    
    auxilary_axis.yaxis.label.set_color(auxilary_color)
    auxilary_axis.tick_params(axis="y", which="major", direction="in", colors=auxilary_color, length=3, width=1, top=True)
    auxilary_axis.tick_params(axis="y", which="minor", direction="in", colors=auxilary_color, length=1.5, width=0.8, top=True)


def set_arrow(axis, x, y, x0, x1, x_gap, y_gap, fit_factor=0, arrow_position='right', color='k', arrowsize=5, linewidth=1, linestyle='-', zorder=100000, deg_correction=0):
    x0_idx, x1_idx = get_nearest_index(x, x0), get_nearest_index(x, x1)
    
    y_fit = polyfit(x, y, fit_factor)
    x_fine = linspace(x0, x1, (x1_idx-x0_idx)*20)
    y_fine=0
    for i in range(fit_factor):
        y_fine += y_fit[0+i]*x_fine**(fit_factor-i)

    x_fine += x_gap
    y_fine += y_gap
    
    axis.plot(x_fine, y_fine, lw=linewidth, ls=linestyle, zorder=zorder, color=color)
    if arrow_position == 'right':
        dx, dy = x_fine[0]-x_fine[1], y_fine[0]-y_fine[1]
        deg = rad2deg(arctan(dx/dy))
        axis.scatter(x_fine[-1], y_fine[-1], marker=(3, 0, deg+deg_correction+60), s=arrowsize, zorder=zorder, color=color)
    elif arrow_position == 'left':
        dx, dy = x_fine[1]-x_fine[0], y_fine[1]-y_fine[0]
        deg = rad2deg(arctan(dx/dy))
        axis.scatter(x_fine[0], y_fine[0], marker=(3, 0, deg+deg_correction), s=arrowsize, zorder=zorder, color=color)


def help_Gridspec():
    print("fig = plt.figure(dpi=400)\
gs = GridSpec(3, 3, figure=fig, hspace=0.5)\
ax0 = fig.add_subplot(gs[:, 2:])\
ax1 = fig.add_subplot(gs[:, :2])\
axis = [ax0, ax1]")
    

def set_CurlyBrace(axis, ll_corner, width, height, direction='h', color='k', lw=1, ls='-'):
    
    def CurlyBrace(axis, ll_corner, width, height, direction=direction, color=color, lw=lw, ls=ls):
        Path = mpath.Path
        verts = np.array([(0, 0), (.5, 0), (.5, .2), (.5, .3), (.5, .5), (1, .5), (.5, .5), (.5, .7), (.5, .8), (.5, 1), (0, 1)])
        if direction == 'h':
            verts = np.array([(0, 0), (.5, 0), (.5, .2), (.5, .3), (.5, .5), (1, .5), (.5, .5), (.5, .7), (.5, .8), (.5, 1), (0, 1)])
        elif direction == 'v':
            verts = np.array([(0, 0), (0, .5), (.2, .5), (.3, .5), (.5, .5), (.5, 1), (.5, .5), (.7, .5), (.8, .5), (1, .5), (1, 0)])
        verts[:, 0] *= width
        verts[:, 1] *= height
        verts[:, 0] += ll_corner[0]
        verts[:, 1] += ll_corner[1]

        cb_patch = mpatches.PathPatch(
            Path(verts,
                [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CURVE3, Path.CURVE3]),
            fc="none", clip_on=False, transform=axis.transData, color=color, lw=lw, ls=ls)
        return cb_patch

    cb = CurlyBrace(axis=axis, ll_corner=ll_corner, width=width, height=height, direction=direction, color=color, lw=lw, ls=ls)
    axis.add_patch(cb)