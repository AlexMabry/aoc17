from enum import Enum
input = 289326


class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 3
    DOWN = 4


def all_neighbors(m, x, y):
    acc = 0
    for x_off in [-1,0,1]:
        for y_off in [-1,0,1]:
            acc += m.get((x + x_off, y + y_off),0)
    return acc


def change_direction(d):
    if d == Direction.RIGHT:
        return Direction.UP
    if d == Direction.UP:
        return Direction.LEFT
    if d == Direction.LEFT:
        return Direction.DOWN
    if d == Direction.DOWN:
        return Direction.RIGHT


def advance_position(x, y, d):
    if d == Direction.RIGHT:
        return x+1, y
    if d == Direction.UP:
        return x, y+1
    if d == Direction.LEFT:
        return x-1, y
    if d == Direction.DOWN:
        return x, y-1


def find_higher_value(max_value):
    x_cord = 50
    y_cord = 50
    matrix = {(x_cord, y_cord): 1}

    side_len = 1
    direction = Direction.RIGHT

    for itr in range(40):
        for side in range(2):
            for elem in range(side_len):
                matrix[(x_cord, y_cord)] = all_neighbors(matrix, x_cord, y_cord)

                if matrix[(x_cord, y_cord)] > max_value:
                    return matrix[(x_cord, y_cord)]

                (x_cord, y_cord) = advance_position(x_cord, y_cord, direction)

            direction = change_direction(direction)
        side_len += 1


print(find_higher_value(input))