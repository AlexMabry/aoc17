from day13.day13_input import layers


firewall = {}
for l in layers:
    parts = l.split(':')
    firewall[int(parts[0])] = int(parts[1])

severity = 0
for step in range(max(firewall.keys())+1):
    if step in firewall:
        caught = step % ((firewall[step]-1)*2) == 0
        if caught:
            severity += step*firewall[step]

print(severity)