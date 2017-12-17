current_position = 0

for number in range(1, 50000000):
    current_position = (current_position + 356) % number + 1

    if current_position == 1:
        print(number)
