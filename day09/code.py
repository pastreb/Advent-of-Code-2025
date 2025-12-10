import os.path
import re


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 9: Movie Theater ---

# You slide down the firepole in the corner of the playground and land in the 
# North Pole base movie theater!

# The movie theater has a big tile floor with an interesting pattern. Elves 
# here are redecorating the theater by switching out some of the square tiles 
# in the big grid they form. Some of the tiles are red; the Elves would like 
# to find the largest rectangle that uses red tiles for two of its opposite 
# corners. They even have a list of where the red tiles are located in the 
# grid (your puzzle input).

# For example:

# 7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3

# Showing red tiles as # and other tiles as ., the above arrangement of red 
# tiles would look like this:

# ..............
# .......#...#..
# ..............
# ..#....#......
# ..............
# ..#......#....
# ..............
# .........#.#..
# ..............

# You can choose any two red tiles as the opposite corners of your rectangle; 
# your goal is to find the largest rectangle possible.

# For example, you could make a rectangle (shown as O) with an area of 24 
# between 2,5 and 9,7:

# ..............
# .......#...#..
# ..............
# ..#....#......
# ..............
# ..OOOOOOOO....
# ..OOOOOOOO....
# ..OOOOOOOO.#..
# ..............

# Or, you could make a rectangle with area 35 between 7,1 and 11,7:

# ..............
# .......OOOOO..
# .......OOOOO..
# ..#....OOOOO..
# .......OOOOO..
# ..#....OOOOO..
# .......OOOOO..
# .......OOOOO..
# ..............

# You could even make a thin rectangle with an area of only 6 between 7,3 and 
# 2,3:

# ..............
# .......#...#..
# ..............
# ..OOOOOO......
# ..............
# ..#......#....
# ..............
# .........#.#..
# ..............

# Ultimately, the largest rectangle you can make in this example has area 50. 
# One way to do this is between 2,5 and 11,1:

# ..............
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..............
# .........#.#..
# ..............

# Using two red tiles as opposite corners, what is the largest area of any 
# rectangle you can make?

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    numbers = [[int(x) for x in re.findall(r"\d+", line)] for line in input]
    return max([max([(abs(numbers[i][0]-numbers[j][0])+1) * (abs(numbers[i][1]-numbers[j][1])+1) for j in range(i+1, len(numbers))]) for i in range(len(numbers)-1)])

# 4741848414
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# The Elves just remembered: they can only switch out tiles that are red or 
# green. So, your rectangle can only include red or green tiles.

# In your list, every red tile is connected to the red tile before and after 
# it by a straight line of green tiles. The list wraps, so the first red tile 
# is also connected to the last red tile. Tiles that are adjacent in your 
# list will always be on either the same row or the same column.

# Using the same example as before, the tiles marked X would be green:

# ..............
# .......#XXX#..
# .......X...X..
# ..#XXXX#...X..
# ..X........X..
# ..#XXXXXX#.X..
# .........X.X..
# .........#X#..
# ..............

# In addition, all of the tiles inside this loop of red and green tiles are 
# also green. So, in this example, these are the green tiles:

# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............

# The remaining tiles are never red nor green.

# The rectangle you choose still must have red tiles in opposite corners, but 
# any other tiles it includes must now be red or green. This significantly 
# limits your options.

# For example, you could make a rectangle out of red and green tiles with an 
# area of 15 between 7,3 and 11,1:

# ..............
# .......OOOOO..
# .......OOOOO..
# ..#XXXXOOOOO..
# ..XXXXXXXXXX..
# ..#XXXXXX#XX..
# .........XXX..
# .........#X#..
# ..............

# Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

# ..............
# .......#XXX#..
# .......XXXXX..
# ..#XXXX#XXXX..
# ..XXXXXXXXXX..
# ..#XXXXXXOXX..
# .........OXX..
# .........OX#..
# ..............

# The largest rectangle you can make in this example using only red and green 
# tiles has area 24. One way to do this is between 9,5 and 2,3:

# ..............
# .......#XXX#..
# .......XXXXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# .........XXX..
# .........#X#..
# ..............

# Using two red tiles as opposite corners, what is the largest area of any 
# rectangle you can make using only red and green tiles?

def check_part_2_criteria(numbers, i, j):
    x0 = min(numbers[i][0], numbers[j][0])
    y0 = max(numbers[i][0], numbers[j][0])
    x1 = min(numbers[i][1], numbers[j][1])
    y1 = max(numbers[i][1], numbers[j][1])
    for k in range(i+1, i+len(numbers)):
        current = numbers[k%len(numbers)]
        c0 = current[0]
        c1 = current[1]
        next = numbers[(k+1)%len(numbers)]
        n0 = next[0]
        n1 = next[1]
        while c0 != n0 or c1 != n1:
            if (x0 < c0 and c0 < y0) and (x1 < c1 and c1 < y1):
                # Border goes inside of rectangle!!1!1
                return False
            c0 += 1 if c0 < n0 else -1 if c0 > n0 else 0
            c1 += 1 if c1 < n1 else -1 if c1 > n1 else 0
    return True

def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    numbers = [[int(x) for x in re.findall(r"\d+", line)] for line in input]
    current_max = 0
    for i in range(len(numbers)-1):
        print(f"{i}/{len(numbers)}")
        for j in range(i+1, len(numbers)):
            candidate_max = (abs(numbers[i][0]-numbers[j][0])+1) * (abs(numbers[i][1]-numbers[j][1])+1)
            if candidate_max > current_max and check_part_2_criteria(numbers, i, j):
                print("new max: ", candidate_max)
                current_max = candidate_max
    return current_max
            
# 1508918480
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

def create_map(numbers):
    max_i = max([number[0] for number in numbers])+2
    max_j = max([number[1] for number in numbers])+2
    map = [['.' for _ in range(max_i)] for _ in range(max_j)]
    for k in range(len(numbers)):
        curr = [numbers[k][0], numbers[k][1]]
        next = numbers[(k+1)%len(numbers)]
        print(curr, next)
        map[curr[1]][curr[0]] = '#'
        while(curr[0] < next[0]):
            curr[0] += 1
            map[curr[1]][curr[0]] = 'X'
        while(curr[0] > next[0]):
            curr[0] -= 1
            map[curr[1]][curr[0]] = 'X'    
        while(curr[1] < next[1]):
            curr[1] += 1
            map[curr[1]][curr[0]] = 'X'
        while(curr[1] > next[1]):
            curr[1] -= 1
            map[curr[1]][curr[0]] = 'X'
    for line in map:
        for k in range(1, len(line)-1):
            if line[k] == '.' and ('X' in line[:k] or '#' in line[:k]) and ('X' in line[k+1:] or '#' in line[k+1:]):
                line[k] = 'X'
    return map

def print_map(map):
    for row in map:
        for x in row:
            print(x, end='')
        print()

def contains_dot(map, i1, i2, j1, j2):
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            if map[j][i] == '.':
                return True
    return False

def compute_part_2_inefficient(input_file_name="sample_input.txt"):
    input = read_input(input_file_name)
    numbers = [[int(x) for x in re.findall(r"\d+", line)] for line in input]
    map = create_map(numbers)
    print("map created")
    current_max = 0
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            print(i, j, numbers[i], numbers[j])
            candidate = (abs(numbers[j][0]-numbers[i][0])+1) * (abs(numbers[j][1]-numbers[i][1])+1)
            if candidate > current_max and not(contains_dot(map, 
                                                            min(numbers[i][0], numbers[j][0]), 
                                                            max(numbers[i][0], numbers[j][0]), 
                                                            min(numbers[i][1], numbers[j][1]), 
                                                            max(numbers[i][1], numbers[j][1]))):
                    current_max = candidate
    return current_max

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
