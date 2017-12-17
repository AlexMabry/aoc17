from day16.day16_input import raw_moves

moves = raw_moves.split(",")
dancers = list("abcdefghijklmnop")

for x in range(16):
    for move in moves:
        if move[0] == 's':
            shift = 16-int(move[1:])
            dancers = dancers[shift:]+dancers[:shift]
        elif move[0] == 'x':
            partners = [int(c) for c in move[1:].split("/")]
            dancers[partners[0]], dancers[partners[1]] = dancers[partners[1]], dancers[partners[0]]
        elif move[0] == 'p':
            partners = [dancers.index(c) for c in move[1:].split("/")]
            dancers[partners[0]], dancers[partners[1]] = dancers[partners[1]], dancers[partners[0]]
        else:
            raise Exception("ERROR")

    if "".join(dancers) == "abcdefghijklmnop":
        print(x)

print("".join(dancers))