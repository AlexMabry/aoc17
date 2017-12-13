from day13.day13_input import layers


def i_made_it(trip, delay):
    for step, distance in trip.items():
        if (step + delay) % distance == 0:
            return False
    return True


firewall = {}
for l in layers:
    parts = l.split(':')
    firewall[int(parts[0])] = (int(parts[1])-1)*2

for wait in range(20000000):
    if i_made_it(firewall, wait):
        print(wait)
        break

