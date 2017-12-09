from day8.day8_input import commands


registers = {}
for c in commands:
    condition = f'registers.get("{c[3]}", 0) {c[4]} {c[5]}'
    if eval(condition):
        registers[c[0]] = registers.get(c[0], 0) + c[2] if c[1] == "inc" else registers.get(c[0],0) - c[2]

largest = 0
for r in registers:
    val = registers[r]
    largest = val if val > largest else largest

print(largest)