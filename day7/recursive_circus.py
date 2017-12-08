from day7.day7_input import towers

bases = {}

for t in towers:
    tower = {"name": t[0], "weight": t[1], "kids": t[2] if len(t) == 3 else None}
    bases[t[0]] = tower


def get_weight(sub):
    sub["total"] = sub["weight"]

    if sub["kids"]:
        kids_weights = [get_weight(bases[kid]) for kid in sub["kids"]]

        balanced = set()
        for kid in kids_weights:
            balanced.add(kid["total"])
            sub["total"] += kid["total"]

        if len(balanced) != 1:
            raise Exception(kids_weights)

    return sub


get_weight(bases['bsfpjtc'])



[{'weight': 1597, 'kids': ['lqwwuqk', 'shypdye', 'javnv'], 'total': 1951},
 {'weight': 85, 'kids': ['xgydg', 'hgyhzc', 'pqqxhy', 'qadkf', 'nsxfciq', 'gbuhi'], 'total': 1951},
 {'weight': 538, 'kids': ['jmrywkk', 'skrlqr', 'gbhssic', 'bxbaua', 'rwvvlbx', 'fftxfs'], 'total': 1960}]

[{'name': 'bbytzn', 'weight': 1597, 'kids': ['lqwwuqk', 'shypdye', 'javnv'], 'total': 1951},
 {'name': 'fzvctf', 'weight': 85, 'kids': ['xgydg', 'hgyhzc', 'pqqxhy', 'qadkf', 'nsxfciq', 'gbuhi'], 'total': 1951},
 {'name': 'utnrb', 'weight': 538, 'kids': ['jmrywkk', 'skrlqr', 'gbhssic', 'bxbaua', 'rwvvlbx', 'fftxfs'], 'total': 1960}]
