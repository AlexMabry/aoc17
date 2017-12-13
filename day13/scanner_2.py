from day13.day13_input import layers


firewall = {}
for l in layers:
    parts = l.split(':')
    firewall[int(parts[0])] = int(parts[1])


for delay in range(20000000):
    caught = False
    for step in range(max(firewall.keys())+1):
        delayed_step = step+delay
        if step in firewall:
            caught |= delayed_step % ((firewall[step]-1)*2) == 0
            if caught:
                break

    if not caught:
        print(delay)
        break


