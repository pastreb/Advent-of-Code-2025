import os.path
import re

from pulp import LpProblem, LpVariable, LpInteger, lpSum, LpStatus

def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 10: Factory ---

# Just across the hall, you find a large factory. Fortunately, the Elves here 
# have plenty of time to decorate. Unfortunately, it's because the factory 
# machines are all offline, and none of the Elves can figure out the 
# initialization procedure.

# The Elves do have the manual for the machines, but the section detailing 
# the initialization procedure was eaten by a Shiba Inu. All that remains of 
# the manual are some indicator light diagrams, button wiring schematics, and 
# joltage requirements for each machine.

# For example:

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

# The manual describes one machine per line. Each line contains a single 
# indicator light diagram in [square brackets], one or more button wiring 
# schematics in (parentheses), and joltage requirements in {curly braces}.

# To start a machine, its indicator lights must match those shown in the 
# diagram, where . means off and # means on. The machine has the number of 
# indicator lights shown, but its indicator lights are all initially off.

# So, an indicator light diagram like [.##.] means that the machine has four 
# indicator lights which are initially off and that the goal is to 
# simultaneously configure the first light to be off, the second light to be 
# on, the third to be on, and the fourth to be off.

# You can toggle the state of indicator lights by pushing any of the listed 
# buttons. Each button lists which indicator lights it toggles, where 0 means 
# the first light, 1 means the second light, and so on. When you push a 
# button, each listed indicator light either turns on (if it was off) or 
# turns off (if it was on). You have to push each button an integer number of 
# times; there's no such thing as "0.5 presses" (nor can you push a button a 
# negative number of times).

# So, a button wiring schematic like (0,3,4) means that each time you push 
# that button, the first, fourth, and fifth indicator lights would all toggle 
# between on and off. If the indicator lights were [#.....], pushing the 
# button would change them to be [...##.] instead.

# Because none of the machines are running, the joltage requirements are 
# irrelevant and can be safely ignored.

# You can push each button as many times as you like. However, to save on 
# time, you will need to determine the fewest total presses required to 
# correctly configure all indicator lights for all machines in your list.

# There are a few ways to correctly configure the first machine:

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

# - You could press the first three buttons once each, a total of 3 button 
#   presses.
# - You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 
#   button presses.
# - You could press all of the buttons except (1,3) once each, a total of 
#   5 button presses.

# However, the fewest button presses required is 2. One way to do this is by 
# pressing the last two buttons ((0,2) and (0,1)) once each.

# The second machine can be configured with as few as 3 button presses:

# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

# One way to achieve this is by pressing the last three buttons ((0,4), 
# (0,1,2), and (1,2,3,4)) once each.

# The third machine has a total of six indicator lights that need to be 
# configured correctly:

# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

# The fewest presses required to correctly configure it is 2; one way to do 
# this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.

# So, the fewest button presses required to correctly configure the indicator 
# lights on all of the machines is 2 + 3 + 2 = 7.

# Analyze each machine's indicator light diagram and button wiring 
# schematics. What is the fewest button presses required to correctly 
# configure the indicator lights on all of the machines?

def recurse(lights, buttons, n_buttons_pressed, diagram):
    if len(buttons) == 0:
        return n_buttons_pressed if all([lights[i] == diagram[i] for i in range(len(lights))]) else 1000
    # It does not make sense to press any button more than once...
    # Ether press next button ... or not
    switched_lights = [lights[i] if i not in buttons[0] else '#' if lights[i] == '.' else '.' for i in range(len(lights))]
    return min(recurse(switched_lights, buttons[1:], n_buttons_pressed + 1, diagram), recurse(lights, buttons[1:], n_buttons_pressed, diagram))

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    diagrams = [[x for x in re.findall(r"\.|\#", line)] for line in input]
    buttons = [[[int(x) for x in re.findall(r"\d+", numbers)] for numbers in re.findall(r"\((.*?)\)", line)] for line in input]
    button_press_sum = 0
    for i in range(len(diagrams)):
        button_press_sum += recurse(['.' for _ in range(len(diagrams[i]))], buttons[i], 0, diagrams[i])
    return button_press_sum

# 479
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# All of the machines are starting to come online! Now, it's time to worry 
# about the joltage requirements.

# Each machine needs to be configured to exactly the specified joltage levels 
# to function properly. Below the buttons on each machine is a big lever that 
# you can use to switch the buttons from configuring the indicator lights to 
# increasing the joltage levels. (Ignore the indicator light diagrams.)

# The machines each have a set of numeric counters tracking its joltage 
# levels, one counter per joltage requirement. The counters are all initially 
# set to zero.

# So, joltage requirements like {3,5,4,7} mean that the machine has four 
# counters which are initially 0 and that the goal is to simultaneously 
# configure the first counter to be 3, the second counter to be 5, the third 
# to be 4, and the fourth to be 7.

# The button wiring schematics are still relevant: in this new joltage 
# configuration mode, each button now indicates which counters it affects, 
# where 0 means the first counter, 1 means the second counter, and so on. 
# When you push a button, each listed counter is increased by 1.

# So, a button wiring schematic like (1,3) means that each time you push that 
# button, the second and fourth counters would each increase by 1. If the 
# current joltage levels were {0,1,2,3}, pushing the button would change them 
# to be {0,2,2,4}.

# You can push each button as many times as you like. However, your finger is 
# getting sore from all the button pushing, and so you will need to determine 
# the fewest total presses required to correctly configure each machine's 
# joltage level counters to match the specified joltage requirements.

# Consider again the example from before:

# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

# Configuring the first machine's counters requires a minimum of 10 button 
# presses. One way to do this is by pressing (3) once, (1,3) three times, 
# (2,3) three times, (0,2) once, and (0,1) twice.

# Configuring the second machine's counters requires a minimum of 12 button 
# presses. One way to do this is by pressing (0,2,3,4) twice, (2,3) five 
# times, and (0,1,2) five times.

# Configuring the third machine's counters requires a minimum of 11 button 
# presses. One way to do this is by pressing (0,1,2,3,4) five times, 
# (0,1,2,4,5) five times, and (1,2) once.

# So, the fewest button presses required to correctly configure the joltage 
# level counters on all of the machines is 10 + 12 + 11 = 33.

# Analyze each machine's joltage requirements and button wiring schematics. 
# What is the fewest button presses required to correctly configure the 
# joltage level counters on all of the machines?

def re_recurse(joltages, buttons, n_buttons_pressed, joltage_requirements):
    if all([joltages[i] == joltage_requirements[i] for i in range(len(joltages))]):
        return n_buttons_pressed
    if any([joltages[i] > joltage_requirements[i] for i in range(len(joltages))]):
        return 10000 # too many buttons pressed
    if len(buttons) == 0:
        return 10000  # no more buttons to press
    # Ether press next button once, multiple times or not
    adjusted_joltages = [joltages[i] + (1 if i in buttons[0] else 0) for i in range(len(joltages))]
    return min(re_recurse(adjusted_joltages, buttons, n_buttons_pressed+1, joltage_requirements),
               re_recurse(joltages, buttons[1:], n_buttons_pressed, joltage_requirements))

def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    buttons = [[[int(x) for x in re.findall(r"\d+", numbers)] for numbers in re.findall(r"\((.*?)\)", line)] for line in input]
    joltages = [[[int(x) for x in re.findall(r"\d+", numbers)] for numbers in re.findall(r"\{(.*?)\}", line)][0] for line in input]
    button_press_sum = 0
    for i in range(len(joltages)):
        # Create problem
        problem = LpProblem("Integer_Linear_Program", sense=1)  # sense=1 for minimization
        # Define variables
        variables = [LpVariable(f"button_{xi}", lowBound=0, cat=LpInteger) for xi in range(len(buttons[i]))]
        # Add constraints for each joltage
        for j in range(len(joltages[i])):
            lhs = lpSum(variables[xi] for xi in range(len(variables)) if j in buttons[i][xi])  # Sum of relevant variables
            problem += lhs == joltages[i][j]  # Constraint: lhs must equal the joltage value
        problem += lpSum(variables) # Objective Function: minimize the sum of variables
        problem.solve()
        if LpStatus[problem.status] == "Optimal":
            button_press_sum += int(sum(var.varValue for var in variables))
        else:
            print(f"No solution found for joltage set {i}")
    return button_press_sum

# 19574
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
