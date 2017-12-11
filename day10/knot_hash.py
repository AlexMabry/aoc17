from day10.day10_input import lengths

circle = [x for x in range(256)]
current = 0
skip = 0

for length in lengths:
    new_list = [circle[(current + x) % 256] for x in range(length)]
    new_list.reverse()

    for idx, n in enumerate(new_list):
        circle[(current + idx) % 256] = n

    current = (current + length + skip) % 256
    skip += 1

print(circle)
print(circle[0] * circle[1])
