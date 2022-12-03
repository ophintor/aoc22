input = 'inputs/3.txt'

def read_input():
    with open(input) as f: lines = [x.strip() for x in f.readlines()]
    return lines

def get_priority(x):
    if x.islower():
        return ord(x) - 96
    elif x.isupper():
        return ord(x) - 38
    else:
        return 0

def part1():
    lines = read_input()
    priorities = 0

    for rucksack in lines:
        item = (set(rucksack[0:len(rucksack)/2]) & set(rucksack[len(rucksack)/2:])).pop()[0]
        priorities += get_priority(item)

    return priorities

def part2():
    lines = read_input()
    priorities = 0
    rucksack_number = 0
    items = []

    for rucksack in lines:
        items.append(rucksack)
        rucksack_number += 1
        if rucksack_number == 3:
            badge = (set(items[0]) & set(items[1]) & set(items[2])).pop()[0]
            priorities += get_priority(badge)
            items = []
            rucksack_number = 0

    return priorities

if __name__ == '__main__':
    print("Part 1: %d" % part1())
    print("Part 2: %d" % part2())
