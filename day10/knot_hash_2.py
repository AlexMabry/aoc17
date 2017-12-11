from functools import reduce

day10 = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"

lengths = [ord(x) for x in day10] + [17, 31, 73, 47, 23]
circle = [x for x in range(256)]
current = 0
skip = 0

for _ in range(64):
    for length in lengths:
        new_list = [circle[(current + x) % 256] for x in range(length)]
        new_list.reverse()

        for idx, n in enumerate(new_list):
            circle[(current + idx) % 256] = n

        current = (current + length + skip) % 256
        skip += 1

dense_hash = []
for dense in range(16):
    sub_list = circle[dense * 16:(dense + 1) * 16]
    dense_hash.append(reduce(lambda x, y: x ^ y, sub_list))

knot_hash = "".join(['%02x' % x for x in dense_hash])
print(knot_hash)
