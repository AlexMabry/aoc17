def get_next(num, product, mod):
    val = (num * product) % 2147483647
    return get_next(val, product, mod) if val % mod else val


a, b, count, bug_num = 783, 325, 0, 2**16
for _ in range(5000000):
    a = get_next(a, 16807, 4)
    b = get_next(b, 48271, 8)

    if a % bug_num == b % bug_num:
        count += 1

print(count)
