#### Big thanks to Christian Witts for debugging my code!
#### https://zatech.slack.com/messages/@U0CT5B4UD

# This challenge seems relatively easy
# It's similar to the one from day 2, so sorting everything will be both
# inefficient and familiar :D

f = open('input_day4','r')

# The input is +500 lines, I'd rather not have it here

input_lines = f.read().split('\n')
# It has a blank line at the end, let's remove that before it causes problems
del input_lines[len(input_lines) - 1]

input_words = {}
invalid_lines = 0

# Now we split the lines into words
for line in input_lines:
    input_words[line] = line.split()    # Giving the key the name of the
                                        # line? Just look at for loop below

# Sweet. Now we check for repeated words in every line
for line in input_lines:
    notepad = []
    for word in input_words[line]:  # <-- Here we save an extra variable
        if word in notepad: invalid_lines +=1; break
        else:   notepad.append(word)

total_lines = len(input_lines)

print('Total number of valid lines are: ' + str(total_lines - invalid_lines))
