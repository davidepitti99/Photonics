import gdsfactory as gf
import numpy as np 

# define the function to generate the 50:50 beamsplitter based on a directional coupler with half the critical length
@gf.cell
def beamsplitter_50_50(gap, interaction_length, dx, dy, cross_section):
    c = gf.Component()

    directional_coupler = gf.components.coupler(gap = gap, length = interaction_length, dy = dy, dx = dx, cross_section=cross_section)
    directional_coupler_ref = c.add_ref(directional_coupler)
    return c

# set the layer
layer = (1, 0)

# directional coupler parameters to obtain a 50:50 beamsplitter 
gap = 0.250
interaction_length = 9.8
dx = 10
dy = 10
wg_width = 0.430
cross_section = gf.cross_section.cross_section(width=wg_width, layer=layer, radius = 0)

# edge coupler parameters 
coupler_length = 10
edge_width = 0.2
length_straight = 10

#generate the structure and the gds 
beamsplitter = beamsplitter_50_50(gap = gap, interaction_length = interaction_length, dx = dx, dy = dy, cross_section=cross_section)
beamsplitter.show()
beamsplitter.write_gds(r"C:\Users\Davide\Documents\GitHub\Photonics\Xanadu\\beamsplitter.gds")