import re

input = 'inputs/5.txt'

def read_input():
    with open(input) as f: lines = [x for x in f.readlines()]
    return lines

def get_crane_size(lines):
    for l in lines:
        if l.strip()[0] == "1":
            size = int(l.strip()[-1])
            break
    return size

def init_stacks(lines, size):
    stacks = {}
    for l in lines:
        if l.strip()[0] == "1":
            size = int(l.strip()[-1])
            break
        for i in range(1, size*4, 4):
            if i <= len(l) and l[i] != ' ':
                stack_number = int((i/4)+1)
                if stack_number in stacks:
                    stacks[stack_number] = l[i] + stacks[stack_number]
                else:
                    stacks[stack_number] = l[i]
    return stacks

def get_instructions(lines):
    instructions = []
    for l in lines:
        if l.startswith("move"):
            instructions.append([int(x) for x in (re.findall(r'\d+', l))])
    return instructions

def rearrange(crate_mover_model):
    message = ""
    lines = read_input()
    size = get_crane_size(lines)
    stacks = init_stacks(lines, size)
    instructions = get_instructions(lines)

    if crate_mover_model == 9000:
        for instruction in instructions:
            for _ in range(instruction[0]):
                stacks[instruction[2]] += stacks[instruction[1]][-1]
                stacks[instruction[1]] = stacks[instruction[1]][:-1]
    elif crate_mover_model == 9001:
        for instruction in instructions:
            stacks[instruction[2]] += stacks[instruction[1]][-instruction[0]:]
            stacks[instruction[1]] = stacks[instruction[1]][:-instruction[0]]

    for crate in range(1, size+1):
        message += stacks[crate][-1]

    return message

if __name__ == '__main__':
    print("Part 1: %s" % rearrange(crate_mover_model=9000))
    print("Part 2: %s" % rearrange(crate_mover_model=9001))
