from day11.day11_input import directions

d_list = directions.split(',')
x, y, steps = 0, 0, 0

for d in d_list:
    x += 1 if 'e' in d else -1 if 'w' in d else 0
    y += -1*(x % 2) if 's' in d else (x % 2)

while x != 0 or y != 0:
    steps += 1

    y += 1 if y < 0 else -1 if y > 0 else 0
    x += 1 if x < 0 else -1 if x > 0 else 0

print(steps)
