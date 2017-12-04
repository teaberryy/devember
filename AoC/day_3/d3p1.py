# Each bottom right square is a perfect square, let's work with that
# Imagine that every "layer" of squares sits no top of the previous,
# for each layer the side length of the square increases by two

import math as mt
num = 265149

def side_length(num):
    # First off, we want to get the square root of the outermost "layer"
    # doing this will give us the distance of the layer and the center
    side = mt.ceil(mt.sqrt(num))
    length = side if side % 2 != 0 else side + 1
    return length

side = side_length(num)

# The distance from the center...
distance_to_center = (side-1)/2

# Plus the distance from the axis...
axes = [side**2 - ((side-1) * i)  - mt.floor(side/2) for i in range(0, 4)]
distance_to_axis = min([abs(axis - num) for axis in axes])

# Is the Manhattan distance to the source!
print(distance_to_axis + distance_to_center)
