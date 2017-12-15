def get_next(num, product):
    return (num * product) % 2147483647


a, b, count, bug_num = 783, 325, 0, 2 ** 16
for _ in range(40000000):
    a = get_next(a, 16807)
    b = get_next(b, 48271)

    if a % bug_num == b % bug_num:
        count += 1

print(count)
