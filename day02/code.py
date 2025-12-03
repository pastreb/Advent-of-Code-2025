import os.path
import re


def read_input(input_file_name):
    input_file = os.path.join(os.path.dirname(__file__), input_file_name)
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines

# --- Day 2: Gift Shop ---

# You get inside and take the elevator to its only other stop: the gift shop. 
# "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. 
# You aren't sure who is even allowed to visit the North Pole, but you know 
# you can access the lobby through here, and from there you can access the 
# rest of the North Pole base.

# As you make your way through the surprisingly extensive selection, one of 
# the clerks recognizes you and asks for your help.

# As it turns out, one of the younger Elves was playing on a gift shop 
# computer and managed to add a whole bunch of invalid product IDs to their 
# gift shop database! Surely, it would be no trouble for you to identify the 
# invalid product IDs for them, right?

# They've even checked most of the product ID ranges already; they only have 
# a few product ID ranges (your puzzle input) that you'll need to check. For 
# example:

# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124

# (The ID ranges are wrapped here for legibility; in your input, they appear 
# on a single long line.)

# The ranges are separated by commas (,); each range gives its first ID and 
# last ID separated by a dash (-).

# Since the young Elf was just doing silly patterns, you can find the invalid 
# IDs by looking for any ID which is made only of some sequence of digits 
# repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) 
# would all be invalid IDs.

# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a 
# valid ID that you would ignore.)

# Your job is to find all of the invalid IDs that appear in the given ranges. 
# In the above example:

# - 11-22 has two invalid IDs, 11 and 22.
# - 95-115 has one invalid ID, 99.
# - 998-1012 has one invalid ID, 1010.
# - 1188511880-1188511890 has one invalid ID, 1188511885.
# - 222220-222224 has one invalid ID, 222222.
# - 1698522-1698528 contains no invalid IDs.
# - 446443-446449 has one invalid ID, 446446.
# - 38593856-38593862 has one invalid ID, 38593859.

# The rest of the ranges contain no invalid IDs.

# Adding up all the invalid IDs in this example produces 1227775554.

# What do you get if you add up all of the invalid IDs?

def compute_part_1_brute_force(input_file_name="input.txt"):
    input = read_input(input_file_name)
    id_ranges = [[x for x in re.findall(r"\d+\-\d+", line)] for line in input][0]
    n = 0
    for id_range in id_ranges:
        range_numbers = [int(x) for x in re.findall(r"\d+", id_range)]
        start = range_numbers[0]
        stop = range_numbers[1]
        for id in range(start, stop+1):
            str_id = str(id)
            str_id_len = len(str_id)
            if str_id_len%2!=0:
                continue
            if int(str_id[0:str_id_len//2]) == int(str_id[str_id_len//2:]):
                n += id
    return n

def compute_part_1(input_file_name="input.txt"):
    input = read_input(input_file_name)
    id_ranges = [[x for x in re.findall(r"\d+\-\d+", line)] for line in input][0]
    n = 0
    for id_range in id_ranges:
        range_numbers = [int(x) for x in re.findall(r"\d+", id_range)]
        start = range_numbers[0]
        stop = range_numbers[1]
        curr = str(start)[:len(str(start))//2] if len(str(start)) % 2 == 0 else ("1" + "0"*((len(str(start))-1)//2))
        while int(curr + curr) < start:
            curr = str(int(curr)+1)        
        while int(curr + curr) <= stop:
            n += int(curr + curr)
            curr = str(int(curr)+1)
    return n

# 38437576669
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

# --- Part Two ---

# The clerk quickly discovers that there are still invalid IDs in the ranges 
# in your list. Maybe the young Elf was doing other silly patterns as well?

# Now, an ID is invalid if it is made only of some sequence of digits 
# repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 
# three times), 1212121212 (12 five times), and 1111111 (1 seven times) are 
# all invalid IDs.

# From the same example as before:

# - 11-22 still has two invalid IDs, 11 and 22.
# - 95-115 now has two invalid IDs, 99 and 111.
# - 998-1012 now has two invalid IDs, 999 and 1010.
# - 1188511880-1188511890 still has one invalid ID, 1188511885.
# - 222220-222224 still has one invalid ID, 222222.
# - 1698522-1698528 still contains no invalid IDs.
# - 446443-446449 still has one invalid ID, 446446.
# - 38593856-38593862 still has one invalid ID, 38593859.
# - 565653-565659 now has one invalid ID, 565656.
# - 824824821-824824827 now has one invalid ID, 824824824.
# - 2121212118-2121212124 now has one invalid ID, 2121212121.

# Adding up all the invalid IDs in this example produces 4174379265.

# What do you get if you add up all of the invalid IDs using these new rules?

def split_and_check_equal(s, size):
    # Split the string into parts of the given size
    parts = re.findall(f'.{{1,{size}}}', s)
    # Check if all parts are equal
    return len(set(parts)) == 1

def compute_part_2(input_file_name="input.txt"):
    input = read_input(input_file_name)
    id_ranges = [[x for x in re.findall(r"\d+\-\d+", line)] for line in input][0]
    n = 0
    for id_range in id_ranges:
        range_numbers = [int(x) for x in re.findall(r"\d+", id_range)]
        start = range_numbers[0]
        stop = range_numbers[1]
        for id in range(start, stop+1):
            str_id = str(id)
            for i in range(len(str_id)//2, 0, -1):
               if split_and_check_equal(str_id, i):
                   n += id
                   break
    return n

# 49046150754
# That's the right answer! You are one gold star closer to decorating the 
# North Pole.

if __name__ == "__main__":
    print(f"PART 1: {compute_part_1()}")
    print(f"PART 2: {compute_part_2()}")
