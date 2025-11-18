from numpy import linspace, array
from matplotlib.pyplot import figure, imread, imshow, axis, show
from cmcrameri import cm
from matplotlib.pyplot import get_cmap


def help_colormap():
    figure(dpi=600)
    help_image = imread('C:/Users/kangh/Documents/RESEARCH/Functions/Crameri colormaps.png')
    imshow(help_image)
    axis('off')
    show()


def get_color_array(cmap, data_length, c_start=0.075, c_end=1):
    try:
        return eval(f"cm.{cmap}(linspace({c_start}, {c_end}, {data_length}))")
    except:
        return eval(f"get_cmap('{cmap}')(linspace({c_start}, {c_end}, {data_length}))")


def rgb2hex(color_array):
    color_array = color_array*255
    r, g, b = round(color_array[0]), round(color_array[1]), round(color_array[2])
    return f"#{r:02x}{g:02x}{b:02x}"

c_blue, c_red = get_color_array('berlin', 2, c_start=0.2,c_end=0.87)
c_magenta, c_green = get_color_array('bam', 2, c_start=0.2,c_end=0.9)
_, c_yellow = get_color_array('bamako', 2, c_start=0.2,c_end=0.9)

c_red = rgb2hex(c_red)
c_blue = rgb2hex(c_blue)
c_green = rgb2hex(c_green)
c_magenta = rgb2hex(c_magenta)
c_yellow = rgb2hex(c_yellow)