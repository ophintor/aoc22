input = 'inputs/4.txt'

def read_input():
    with open(input) as f: lines = [x.strip() for x in f.readlines()]
    return lines
    

def read_sections():
    lines = read_input()
    contained_fully = 0
    overlap = 0

    for sections in lines:
        s1,s2 = sections.split(',')

        s1_set = {x for x in range(int(s1.split('-')[0]),int(s1.split('-')[1])+1)}
        s2_set = {x for x in range(int(s2.split('-')[0]),int(s2.split('-')[1])+1)}

        if s1_set & s2_set == s1_set or s1_set & s2_set == s2_set:
            contained_fully +=1 
        if s1_set & s2_set:
            overlap +=1 

    return contained_fully, overlap


if __name__ == '__main__':
    print("Part 1: %d" % read_sections()[0])
    print("Part 2: %d" % read_sections()[1])
