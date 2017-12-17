current_position = 0
circle_buf = [0]

for number in range(1, 2018):
    current_position = (current_position + 356) % number + 1
    circle_buf.insert(current_position, number)

print(circle_buf[current_position+1])