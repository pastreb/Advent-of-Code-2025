import os.path
import re

def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 5: Cafeteria ---

# As the forklifts break through the wall, the Elves are delighted to 
# discover that there was a cafeteria on the other side after all.

# You can hear a commotion coming from the kitchen. "At this rate, we won't 
# have any time left to put the wreaths up in the dining hall!" Resolute in 
# your quest, you investigate.

# "If only we hadn't switched to the new inventory management system right 
# before Christmas!" another Elf exclaims. You ask what's going on.

# The Elves in the kitchen explain the situation: because of their 
# complicated new inventory management system, they can't figure out which of 
# their ingredients are fresh and which are spoiled. When you ask how it 
# works, they give you a copy of their database (your puzzle input).

# The database operates on ingredient IDs. It consists of a list of fresh 
# ingredient ID ranges, a blank line, and a list of available ingredient IDs. 
# For example:

# 3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32

# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 
# 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is 
# fresh if it is in any range.

# The Elves are trying to determine which of the available ingredient IDs are 
# fresh. In this example, this is done as follows:

# - Ingredient ID 1 is spoiled because it does not fall into any range.
# - Ingredient ID 5 is fresh because it falls into range 3-5.
# - Ingredient ID 8 is spoiled.
# - Ingredient ID 11 is fresh because it falls into range 10-14.
# - Ingredient ID 17 is fresh because it falls into range 16-20 as well as 
#   range 12-18.
# - Ingredient ID 32 is spoiled.

# So, in this example, 3 of the available ingredient IDs are fresh.

# Process the database file from the new inventory management system. How 
# many of the available ingredient IDs are fresh?

def get_id_ranges_and_ingredients(input):
    id_ranges = []
    ingredients = []
    for line in input:
        if '-' in line:
            id_ranges.append([int(x) for x in re.findall(r"\d+", line)])
        elif line != '\n':
            ingredients.append(int(line))
    return id_ranges, ingredients

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    id_ranges, ingredients = get_id_ranges_and_ingredients(input)
    total = 0
    for id in ingredients:
        for id_range in id_ranges:
            if id_range[0] <= id and id <= id_range[1]:
                total += 1
                break
    return total

# 782
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# The Elves start bringing their spoiled inventory to the trash chute at the 
# back of the kitchen.

# So that they can stop bugging you when they get new inventory, the Elves 
# would like to know all of the IDs that the fresh ingredient ID ranges 
# consider to be fresh. An ingredient ID is still considered fresh if it is 
# in any range.

# Now, the second section of the database (the available ingredient IDs) is 
# irrelevant. Here are the fresh ingredient ID ranges from the above example:

# 3-5
# 10-14
# 16-20
# 12-18

# The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 
# 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh 
# ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

# Process the database file again. How many ingredient IDs are considered to 
# be fresh according to the fresh ingredient ID ranges?

def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    id_ranges, _ = get_id_ranges_and_ingredients(input)
    # Filter out id ranges that are completely contained in other id ranges
    id_ranges_to_be_ignored = []
    for i in range(len(id_ranges)):
        for j in range(len(id_ranges)):
            if i != j and id_ranges[j][0] <= id_ranges[i][0] and id_ranges[i][1] <= id_ranges[j][1] and j not in id_ranges_to_be_ignored:
                # Overlap such as [...<...>...]
                id_ranges_to_be_ignored.append(i)
    # Adjust partially overlapping id ranges
    total_ids = 0
    for i in range(len(id_ranges)):
        if i in id_ranges_to_be_ignored:
            continue
        for j in range(len(id_ranges)):
            if i == j or j in id_ranges_to_be_ignored:
                continue
            if id_ranges[j][0] <= id_ranges[i][0] and id_ranges[i][0] <= id_ranges[j][1]:
                # Overlap such as [...<...]...>
                # -> Move:        [......]<...>
                id_ranges[i][0] = id_ranges[j][1]+1
            if id_ranges[j][0] <= id_ranges[i][1] and id_ranges[i][1] <= id_ranges[j][1]:
                # Overlap such as <...[...>...]
                # -> Move:        <...>[......]
                id_ranges[i][1] = id_ranges[j][0]-1
        total_ids += max(0, id_ranges[i][1]-id_ranges[i][0]+1)
    return total_ids

# 353863745078671
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
