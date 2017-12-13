from day13.day13_input import layers


firewall = {}
for l in layers:
    parts = l.split(':')
    firewall[int(parts[0])] = int(parts[1])

severity = 0
for step, depth in firewall.items():
    if not step % ((depth - 1) * 2):
        severity += step * depth

print(severity)
