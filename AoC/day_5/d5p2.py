# This looks like a problem for Recursion Man!

# Pump the values into a list
f = open('input_day5', 'r')
jump_strings_list = f.read().split('\n')

# Remove the (empty) last value
del jump_strings_list[-1]

# Make all of the values ints and not strings
jump_list = [int(x) for x in jump_strings_list]

count = index = 0

print('This is going to take a while')

while index < len(jump_list) and index >=0:
    prev_index = index
    index += jump_list[index]
    if jump_list[prev_index] >= 3:   # Pesky boundary conditions
        jump_list[prev_index] -= 1
    else:
        jump_list[prev_index] += 1
    count += 1

print(count)
