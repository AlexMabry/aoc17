from day7.day7_input import towers

bases = set()
subs = set()

for t in towers:
    bases.add(t[0])

    if len(t) == 3:
        for s in t[2]:
            subs.add(s)

print(bases - subs)
