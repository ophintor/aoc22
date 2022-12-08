input = 'inputs/8.txt'

def read_input():
    with open(input) as f: lines = [[int(y) for y in x.strip()] for x in f.readlines()]
    return lines

def treetop():
    lines = read_input()
    max_score = 0
    visible_trees = len(lines)*2 + len(lines[0])*2 - 4

    for i in range(1,len(lines)-1):
        for j in range(1,len(lines[i])-1):
            north_score = 0
            south_score = 0
            west_score = 0
            east_score = 0
            hidden_sides = 0

            for north in range(i-1, -1, -1):
                north_score += 1
                if lines[i][j] <= lines[north][j]:
                    hidden_sides += 1
                    break

            for south in range(i+1,len(lines)):
                south_score += 1
                if lines[i][j] <= lines[south][j]:
                    hidden_sides += 1
                    break

            for west in range(j-1, -1, -1):
                west_score += 1
                if lines[i][j] <= lines[i][west]:
                    hidden_sides += 1
                    break

            for east in range(j+1,len(lines[j])):
                east_score += 1
                if lines[i][j] <= lines[i][east]:
                    hidden_sides += 1
                    break

            if hidden_sides < 4: visible_trees += 1
            scenic_score = north_score * south_score * west_score * east_score
            if scenic_score > max_score: max_score = scenic_score

    return visible_trees, max_score


if __name__ == '__main__':
    print("Part 1: %d" % treetop()[0])
    print("Part 2: %d" % treetop()[1])

