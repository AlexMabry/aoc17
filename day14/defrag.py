from day10.knot_hash_2 import get_dense_hash

ones = 0
for row in range(128):
    dense_hash = get_dense_hash(f"hwlqcszp-{row}")
    knot_hash = "".join(['{0:08b}'.format(x) for x in dense_hash])
    ones += knot_hash.count("1")

print(ones)
