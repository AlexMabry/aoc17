from day11.day11_input import directions


def distance_home(ex, why):
    steps = 0
    while ex != 0 or why != 0:
        steps += 1

        why += 1 if why < 0 else -1 if why > 0 else 0
        ex += 1 if ex < 0 else -1 if ex > 0 else 0
    return steps


most_steps = 0
d_list = directions.split(',')
x, y = 0, 0

for d in d_list:
    x += 1 if 'e' in d else -1 if 'w' in d else 0
    y += -1*(x % 2) if 's' in d else (x % 2)
    how_far = distance_home(x,y)
    print(how_far)
    if how_far > most_steps:
        most_steps = how_far


print(most_steps)
