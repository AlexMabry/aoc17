from day6.day6_input import banks


def biggest(memory_banks):
    big = (0, 0)
    for position, number in enumerate(memory_banks):
        if number > big[1]:
            big = (position, number)

    return big


def spread_the_wealth(memory_banks):
    (most_pos, most_val) = biggest(memory_banks)
    memory_banks[most_pos] = 0

    for block in range(most_val):
        lucky_bank = (most_pos + block+1) % len(memory_banks)
        memory_banks[lucky_bank] += 1

    return memory_banks


def reallocation_results(init):
    results = set()
    new_result = spread_the_wealth(init)
    while tuple(new_result) not in results:
        results.add(tuple(new_result))
        new_result = spread_the_wealth(new_result)

    return results, new_result


(_, repeat) = reallocation_results(banks)
(repeat_results, _) = reallocation_results(repeat)

print(len(repeat_results))