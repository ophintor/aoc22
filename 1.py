input = 'inputs/1.txt'

def read_input():
    with open(input) as f: lines = [x.strip() for x in f.readlines()]
    return lines

def calculate_calories():
    lines = read_input()
    elf_cals = 0
    max = []

    for v in lines:
        if v.isdigit():
            elf_cals += int(v)
        else:
            max.append(elf_cals)
            elf_cals = 0

    max.sort(reverse=True)
    return max

if __name__ == '__main__':
    calories = calculate_calories()
    print("Part 1: %d" % calories[0])
    print("Part 2: %d" % sum(calories[0:3]))
