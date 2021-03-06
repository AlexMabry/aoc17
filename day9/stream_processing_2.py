from day9.day9_input import stream
from collections import deque

in_group = deque([True])
ignore = False
total_garbage = 0

for character in stream:
    if in_group[-1]:
        if character == '{':
            in_group.append(True)
        elif character == '<':
            in_group.append(False)
        elif character == '}':
            in_group.pop()
    else:
        if ignore:
            ignore = False
        elif character == '!':
            ignore = True
        elif character == '>':
            in_group.pop()
        else:
            total_garbage += 1

print(total_garbage)
