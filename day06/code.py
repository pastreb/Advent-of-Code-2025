import os.path
import re
from operator import mul
from functools import reduce

def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 6: Trash Compactor ---

# After helping the Elves in the kitchen, you were taking a break and helping 
# them re-enact a movie scene when you over-enthusiastically jumped into the 
# garbage chute!

# A brief fall later, you find yourself in a garbage smasher. Unfortunately, 
# the door's been magnetically sealed.

# As you try to find a way out, you are approached by a family of 
# cephalopods! They're pretty sure they can get the door open, but it will 
# take some time. While you wait, they're curious if you can help the 
# youngest cephalopod with her math homework.

# Cephalopod math doesn't look that different from normal math. The math 
# worksheet (your puzzle input) consists of a list of problems; each problem 
# has a group of numbers that need to either be either added (+) or 
# multiplied (*) together.

# However, the problems are arranged a little strangely; they seem to be 
# presented next to each other in a very long horizontal list. For example:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  

# Each problem's numbers are arranged vertically; at the bottom of the 
# problem is the symbol for the operation that needs to be performed. 
# Problems are separated by a full column of only spaces. The left/right 
# alignment of numbers within each problem can be ignored.

# So, this worksheet contains four problems:

# - 123 * 45 * 6 = 33210
# - 328 + 64 + 98 = 490
# - 51 * 387 * 215 = 4243455
# - 64 + 23 + 314 = 401

# To check their work, cephalopod students are given the grand total of 
# adding together all of the answers to the individual problems. In this 
# worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

# Of course, the actual worksheet is much wider. You'll need to make sure to 
# unroll it completely so that you can read the problems clearly.

# Solve the problems on the math worksheet. What is the grand total found by 
# adding together all of the answers to the individual problems?

def solve_problem(numbers, op):
    return sum(numbers) if op == "+" else (reduce(mul, numbers) if op == "*" else -1)

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    numbers = [[int(x) for x in re.findall(r"\d+", line)] for line in input[:-1]]
    operations = [x for x in re.findall(r"\+|\*", input[-1])]
    results = [solve_problem([numbers[j][i] for j in range(len(numbers))], operations[i]) for i in range(len(numbers[0]))]
    return sum(results)

# 5381996914800
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# The big cephalopods come back to check on how things are going. When they 
# see that your grand total doesn't match the one expected by the worksheet, 
# they realize they forgot to explain how to read cephalopod math.

# Cephalopod math is written right-to-left in columns. Each number is given 
# in its own column, with the most significant digit at the top and the least 
# significant digit at the bottom. (Problems are still separated with a 
# column consisting only of spaces, and the symbol at the bottom of the 
# problem is still the operator to use.)

# Here's the example worksheet again:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  

# Reading the problems right-to-left one column at a time, the problems are 
# now quite different:

# - The rightmost problem is 4 + 431 + 623 = 1058
# - The second problem from the right is 175 * 581 * 32 = 3253600
# - The third problem from the right is 8 + 248 + 369 = 625
# - Finally, the leftmost problem is 356 * 24 * 1 = 8544

# Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

# Solve the problems on the math worksheet again. What is the grand total 
# found by adding together all of the answers to the individual problems?

def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    digits = [[x for x in re.findall(r"\d|\s", line.replace('\n', ''))] for line in input[:-1]]
    rearranged_digits = [[digits[j][i] for j in range(len(digits)) if digits[j][i] != ' '] for i in range(len(digits[0]))]
    operations = [x for x in re.findall(r"\+|\*", input[-1])]
    total, idx, op = 0, 0, 0
    while idx < len(rearranged_digits):
        result = int(''.join(rearranged_digits[idx]))
        while idx + 1 < len(rearranged_digits) and rearranged_digits[idx+1]:
            idx += 1
            result = result + int(''.join(rearranged_digits[idx])) if operations[op] == "+" else result * int(''.join(rearranged_digits[idx]))
        total += result
        idx += 2
        op += 1
    return total

# 9627174150897
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
