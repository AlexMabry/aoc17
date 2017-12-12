from day12.day12_input import pipes


def init_programs(input_list):
    ret = {}
    for p in input_list:
        links = p.replace(' ', "").split('<->')
        ret[links[0]] = set(links[1].split(','))
    return ret


def add_links(old_links):
    new_links = set()
    for link in old_links:
        new_links |= programs[link]
    return old_links if new_links <= old_links else add_links(old_links | new_links)


programs = init_programs(pipes)

contain_zero = set()
for p, l in programs.items():
    if '0' in add_links(l):
        contain_zero.add(p)

print(len(contain_zero))



