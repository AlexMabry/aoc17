from day5.d5_input import jumps

location = 0
turns = 0

while location < len(jumps):
    turns += 1
    new_jump = jumps[location]
    jumps[location] += 1
    location += new_jump

print(turns)
