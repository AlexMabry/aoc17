from day8.day8_input import commands

largest = 0
registers = {}
for c in commands:
    if eval(f'registers.get("{c[3]}", 0) {c[4]} {c[5]}'):
        registers[c[0]] = registers.get(c[0], 0) + c[2] if c[1] == "inc" else registers.get(c[0], 0) - c[2]

for r in registers:
    largest = registers[r] if registers[r] > largest else largest

print(largest)
