import re 

input = 'inputs/7.txt'

def read_input():
    with open(input) as f: lines = [x for x in f.readlines()]
    return lines

def part1():
    lines = read_input()
    fs_sizes = fs_depths = {}
    fs_depths = {}
    current_dir = []
    depth = 0
    max_depth = 0
    solution = 0

    # Get dirs and sizes, keep track of the depth
    for line in lines:
        if line[0:4] == "$ cd":
            dir_name = line.split()[2]
            if dir_name == "..":
                current_dir.pop()
                depth -= 1
            else:
                current_dir.append(dir_name)
                current_dir_str = "/".join(current_dir)
                depth += 1
                fs_depths[current_dir_str] = depth
                fs_sizes[current_dir_str] = 0
                if depth > max_depth: 
                    max_depth = depth
        elif line.split()[0].isdigit():
            fs_sizes[current_dir_str] += int(line.split()[0])

    # Add the size of dirs into parents
    for dir_depth in range(max_depth, 1, -1):
        for dir in fs_sizes.keys():
            current_dir_size = fs_sizes[dir]
            if fs_depths[dir] == dir_depth:
                dir = re.sub('/\w*$', '', dir)
                if dir in fs_sizes.keys(): 
                    fs_sizes[dir] += current_dir_size

    # Compute solution
    for dir in fs_sizes.keys():
        if fs_sizes[dir] <= 100000:
            solution += fs_sizes[dir]

    return solution, fs_sizes

def part2(fs_sizes):
    max_occupied_space = 40000000
    fs_total_size = fs_sizes["/"]
    candidates = []
    for x in fs_sizes.keys():
        if fs_total_size - fs_sizes[x] < max_occupied_space:
            candidates.append(fs_sizes[x])

    return min(candidates)

if __name__ == '__main__':
    total, fs_sizes = part1()
    print("Part 1: %d" % total)
    print("Part 2: %d" % part2(fs_sizes))