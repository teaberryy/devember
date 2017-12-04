# Part 2 of the same challenge, code will be mostly reused

f = open('input_day4','r')

# The input is +500 lines, I'd rather not have it here

input_lines = f.read().split('\n')
# It has a blank line at the end, let's remove that before it causes problems
del input_lines[-1]

input_words = {}
invalid_lines = 0

# Now we split the lines into words
for line in input_lines:
    input_words[line] = line.split()    # Giving the key the name of the
                                        # line? Explained in previous file

notepad = []

# Sweet. Now we check for repeated words in every line
for line in input_lines:
    notepad.clear() # We just flush the notepad after every loop

    # First we turn the word being inspected into an ordered list
    for wordies in input_words[line]:
        sliced_word = sorted(list(wordies))

        if (sliced_word in notepad):    # Then we see if it has been processed
            invalid_lines += 1          # If so, stop processing line
            break
        else:   notepad.append(sliced_word) # If not, process it and move on

total_lines = len(input_lines)

print('Total number of valid lines are: ' + str(total_lines - invalid_lines))
