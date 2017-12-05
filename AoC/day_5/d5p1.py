# This looks like a problem for Recursion Man!

# Pump the values into a list
f = open('input_day5', 'r')
jump_strings_list = f.read().split('\n')

# Remove the (empty) last value
del jump_strings_list[-1]

# Make all of the values usable ints and not strings
jump_list = [int(x) for x in jump_strings_list]

count = index = 0

while index < len(jump_list) and index >=0:
    prev_index = index
    index += jump_list[index]
    jump_list[prev_index] += 1
    count += 1

print(count)
