input = 'inputs/6.txt'

def find_signal(signal_size):
    with open(input) as f: line = f.readline()
    for i in range(signal_size,len(line)+1):
        if len(set(line[i-signal_size:i])) == signal_size:
            return i

if __name__ == '__main__':
    print("Part 1: %d" % find_signal(4))
    print("Part 2: %s" % find_signal(14))