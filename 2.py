input = 'inputs/2.txt'

# A,X rock
# B,Y paper
# C,Z scissors

scores = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}


def read_input():
    with open(input) as f: lines = [x.strip() for x in f.readlines()]
    return lines


def part1():
    lines = read_input()
    my_score = 0

    for game in lines:
        elf_hand, my_hand = game.split()
        
        my_score += scores[my_hand]

        if (elf_hand == "A" and my_hand == "X") or (elf_hand == "B" and my_hand == "Y") or (elf_hand == "C" and my_hand == "Z"):
            my_score += 3
        elif (elf_hand == "A" and my_hand == "Y") or (elf_hand == "B" and my_hand == "Z") or (elf_hand == "C" and my_hand == "X"):
            my_score += 6

    return my_score


def part2():
    lines = read_input()
    my_score = 0

    for game in lines:
        elf_hand, end_result = game.split()

        if end_result == "X":
            my_score += ((scores[elf_hand] + 1) % 3) + 1
        elif end_result == "Y":
            my_score += 3 + scores[elf_hand]
        elif end_result == "Z":
            my_score += 6 + (scores[elf_hand] % 3) + 1

    return my_score


if __name__ == '__main__':
    print("Part 1: %d" % part1())
    print("Part 2: %d" % part2())
