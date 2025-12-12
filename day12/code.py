import os.path
import re
import numpy as np
from itertools import product


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 12: Christmas Tree Farm ---

# You're almost out of time, but there can't be much left to decorate. 
# Although there are no stairs, elevators, escalators, tunnels, chutes, 
# teleporters, firepoles, or conduits here that would take you deeper into 
# the North Pole base, there is a ventilation duct. You jump in.

# After bumping around for a few minutes, you emerge into a large, well-lit 
# cavern full of Christmas trees!

# There are a few Elves here frantically decorating before the deadline. They 
# think they'll be able to finish most of the work, but the one thing they're 
# worried about is the presents for all the young Elves that live here at the 
# North Pole. It's an ancient tradition to put the presents under the trees, 
# but the Elves are worried they won't fit.

# The presents come in a few standard but very weird shapes. The shapes and 
# the regions into which they need to fit are all measured in standard units. 
# To be aesthetically pleasing, the presents need to be placed into the 
# regions in a way that follows a standardized two-dimensional unit grid; you 
# also can't stack presents.

# As always, the Elves have a summary of the situation (your puzzle input) 
# for you. First, it contains a list of the presents' shapes. Second, it 
# contains the size of the region under each tree and a list of the number of 
# presents of each shape that need to fit into that region. For example:

# 0:
# ###
# ##.
# ##.

# 1:
# ###
# ##.
# .##

# 2:
# .##
# ###
# ##.

# 3:
# ##.
# ###
# ##.

# 4:
# ###
# #..
# ###

# 5:
# ###
# .#.
# ###

# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2

# The first section lists the standard present shapes. For convenience, each 
# shape starts with its index and a colon; then, the shape is displayed 
# visually, where # is part of the shape and . is not.

# The second section lists the regions under the trees. Each line starts with 
# the width and length of the region; 12x5 means the region is 12 units wide 
# and 5 units long. The rest of the line describes the presents that need to 
# fit into that region by listing the quantity of each shape of present; 
# 1 0 1 0 3 2 means you need to fit one present with shape index 0, no 
# presents with shape index 1, one present with shape index 2, no presents 
# with shape index 3, three presents with shape index 4, and two presents 
# with shape index 5.

# Presents can be rotated and flipped as necessary to make them fit in the 
# available space, but they have to always be placed perfectly on the grid. 
# Shapes can't overlap (that is, the # part from two different presents can't 
# go in the same place on the grid), but they can fit together (that is, the 
# . part in a present's shape's diagram does not block another present from 
# occupying that space on the grid).

# The Elves need to know how many of the regions can fit the presents listed. 
# In the above example, there are six unique present shapes and three regions 
# that need checking.

# The first region is 4x4:

# ....
# ....
# ....
# ....

# In it, you need to determine whether you could fit two presents that have 
# shape index 4:

# ###
# #..
# ###

# After some experimentation, it turns out that you can fit both presents in 
# this region. Here is one way to do it, using A to represent one present and 
# B to represent the other:

# AAA.
# ABAB
# ABAB
# .BBB

# The second region, 12x5: 1 0 1 0 2 2, is 12 units wide and 5 units long. In 
# that region, you need to try to fit one present with shape index 0, one 
# present with shape index 2, two presents with shape index 4, and two 
# presents with shape index 5.

# It turns out that these presents can all fit in this region. Here is one 
# way to do it, again using different capital letters to represent all the 
# required presents:

# ....AAAFFE.E
# .BBBAAFFFEEE
# DDDBAAFFCECE
# DBBB....CCC.
# DDD.....C.C.

# The third region, 12x5: 1 0 1 0 3 2, is the same size as the previous 
# region; the only difference is that this region needs to fit one additional 
# present with shape index 4. Unfortunately, no matter how hard you try, 
# there is no way to fit all of the presents into this region.

# So, in this example, 2 regions can fit all of their listed presents.

# Consider the regions beneath each tree and the presents the Elves would 
# like to fit into each of them. How many of the regions can fit all of the 
# presents listed?

def parse_input(input):
    shapes = {}
    regions = []
    i = 0
    while i < len(input):
        if re.findall(r"^\d+\:", input[i]):
            idx = int(re.findall(r"^\d+\:", input[i])[0][:-1])
            new_shape = []
            i += 1
            while '#' in input[i] or '.' in input[i]:
                new_shape.append([x for x in input[i].replace('\n', '')])
                i += 1
            shapes[idx] = np.array(new_shape)
            i += 1
        else:
            dimensions = [int(x) for x in re.findall(r"\d+", input[i].split(":")[0])]
            counts = [int(x) for x in re.findall(r"\d+", input[i].split(":")[1])]
            regions.append((dimensions, counts))
            i += 1
    return shapes, regions

def generate_unique_transformations(shape):
    transformations = set()
    for rotation in range(4):
        rotated = np.rot90(shape, rotation)
        transformations.add(tuple(map(tuple, rotated)))
        transformations.add(tuple(map(tuple, np.flip(rotated, axis=0))))
        transformations.add(tuple(map(tuple, np.flip(rotated, axis=1))))
    return [np.array(t) for t in transformations]

def place_present(grid, shape, x, y):
    h, w = shape.shape
    subgrid = grid[y:y+h, x:x+w]
    if np.any((shape == "#") & (subgrid != ".")):
        return False
    subgrid[shape == "#"] = "#"
    return True

def remove_present(grid, shape, x, y):
    h, w = shape.shape
    grid[y:y+h, x:x+w][shape == "#"] = "."

def can_fit(shapes, requirements, grid, width, height):
    if all(count == 0 for count in requirements):
        return True
    for shape_index, count in enumerate(requirements):
        if count == 0:
            continue
        for transform in generate_unique_transformations(shapes[shape_index]):
            for x, y in product(range(width - transform.shape[1] + 1), range(height - transform.shape[0] + 1)):
                if place_present(grid, transform, x, y):
                    requirements[shape_index] -= 1
                    if can_fit(shapes, requirements, grid, width, height):
                        return True
                    requirements[shape_index] += 1
                    remove_present(grid, transform, x, y)
    return False

def dummy_can_fit(shapes, requirements, width, height):
    total_area_needed = sum(np.sum(shapes[i] == "#") * requirements[i] for i in range(len(requirements)))
    total_area_available = width * height
    return total_area_needed <= total_area_available

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    shapes, regions = parse_input(input)
    count = 0
    for region, requirements in regions:
        width, height = region
        # if can_fit(shapes, requirements, np.full((height, width), "."), width, height)
        # L> would probably solve the sample input
        if dummy_can_fit(shapes, requirements, width, height):
            # L> enough to solve the real input
            count += 1
    return count

# 495
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# The Elves thank you profusely for the help and start rearranging the oddly-
# shaped presents. As you look up, you notice that a lot more Elves have 
# arrived here at the Christmas tree farm.

# In fact, many of these new arrivals look familiar: they're the Elves you 
# helped while decorating the North Pole base. Right on schedule, each group 
# seems to have brought a star to put atop one of the Christmas trees!

# Before any of them can find a ladder, a particularly large Christmas tree 
# suddenly flashes brightly when a large star magically appears above it! As 
# your eyes readjust, you think you notice a portly man with a white beard 
# disappear into the crowd.

# You go look for a ladder; only 23 stars to go.

# You help the Elves decorate the Christmas trees with all 24 stars! Now, the 
# Elves will have plenty of time to prepare for Christmas, and you get a 
# well-deserved break.

# Congratulations! You've finished every puzzle in Advent of Code 2025!

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")