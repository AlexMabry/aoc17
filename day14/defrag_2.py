from day10.knot_hash_2 import get_dense_hash


def spread_group(t, group):
    blocks[t] = group
    for t in [(t[0] - 1, t[1]), (t[0] + 1, t[1]), (t[0], t[1] - 1), (t[0], t[1] + 1)]:
        if blocks.get(t, -1) == 0:
            spread_group(t, group)


blocks = {}
for row in range(128):
    dense_hash = get_dense_hash(f"hwlqcszp-{row}")
    knot_hash = "".join(['{0:08b}'.format(x) for x in dense_hash])
    for x, number in enumerate(knot_hash):
        blocks[(x, row)] = 0 if number == "1" else -1

total_groups = 0
for coord in blocks:
    if blocks[coord] == 0:
        total_groups += 1
        spread_group(coord, total_groups)

print(total_groups)
