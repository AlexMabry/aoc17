from day8.day8_input import commands


def all_registers(command_list):
    ret = set()
    for command in command_list:
        ret.add(command[0])
        ret.add(command[3])
    return ret


registers = {}
for r in all_registers(commands):
    registers[r] = 0

largest = 0
for c in commands:
    condition = f'registers["{c[3]}"] {c[4]} {c[5]}'
    if eval(condition):
        registers[c[0]] = registers[c[0]] + c[2] if c[1] == "inc" else registers[c[0]] - c[2]
        largest = registers[c[0]] if registers[c[0]] > largest else largest

print(largest)

largest = 0
for r in registers:
    val = registers[r]
    largest = val if val > largest else largest

print(largest)