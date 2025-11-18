from cmcrameri import cm
from matplotlib.pyplot import get_cmap
from numpy import linspace


def get_color_array(cmap, data_length, c_start=0.075, c_end=1):
    try:
        return eval(f"cm.{cmap}(linspace({c_start}, {c_end}, {data_length}))")
    except:
        return eval(f"get_cmap('{cmap}')(linspace({c_start}, {c_end}, {data_length}))")


def rgb2hex(color_array):
    color_array = color_array*255
    r, g, b = round(color_array[0]), round(color_array[1]), round(color_array[2])
    return f"#{r:02x}{g:02x}{b:02x}"


c_red = "#FF2C43"
c_orange = "#FF9A47"
c_yellow = "#F8E448"
c_lime = "#98EE84"
c_green = "#1B9C21"
c_mint = "#76DDBE"
c_blue = "#49BCE6"
c_navy = "#4965E6"
c_purple = "#A588DB"
c_pink = "#FF7BCC"