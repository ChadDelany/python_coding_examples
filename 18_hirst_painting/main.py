"""Generate a Hirst-style Spot Painting"""

import colorgram

rgb_colors = []
colors = colorgram.extract('hist_spot_painting.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

