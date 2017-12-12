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


def get_group(program):
    group = set()
    for p, l in programs.items():
        if program in add_links(l):
            group.add(p)
    return group

programs = init_programs(pipes)
programs_in_groups = set()
groups = 0
for program in programs:
    if program not in programs_in_groups:
        groups += 1
        programs_in_groups |= get_group(program)

print(groups)
