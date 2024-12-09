def parse():
    with open('day09.in') as f:
        return f.read().strip()

def compact(line):
    # even = ID, odd = blank
    res = [""] * sum(int(x) for x in line)
    res_i = 0
    for i in range(len(line)):
        if i % 2 == 0:
            for _ in range(int(line[i])):
                res[res_i] = str(i // 2)
                res_i += 1
        else:
            res_i += int(line[i])

    i = 0
    j = len(res) - 1
    while i < j:
        if res[i] != '':
            i += 1
        elif res[j] == '':
            j -= 1
        else:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1

    final_idx = 0
    while res[final_idx] != '':
        final_idx += 1
    return res[:final_idx]

def get_checksum(line):
    compacted = compact(line)
    return sum([int(compacted[i]) * i for i in range(len(compacted))])

def compact_blocks(line):
    # file: (id, count)
    # gap: (filled bool, count, filled id)
    memory = []
    for i in range(len(line)):
        if i % 2 == 0:
            memory.append((str(i // 2), int(line[i])))
        else:
            memory.append((False, int(line[i]), None))
    
    i = len(memory) - 1
    while i >= 0:
        if len(memory[i]) == 2: # file
            for j in range(i):
                # if there's a gap that can fit the file, we need to:
                # 1. fill in the correct amount in the gap
                # 2. turn the existing file space into a gap
                # 3. recreate the remaining gap (and update i accordingly)
                if len(memory[j]) == 3 and not memory[j][0] and memory[j][1] >= memory[i][1]:
                    remaining = memory[j][1] - memory[i][1]
                    memory[j] = (True, memory[i][1], memory[i][0])
                    memory[i] = (False, memory[i][1], None)
                    if remaining > 0:
                        memory.insert(j + 1, (False, remaining, None))
                        i += 1
                    break
        i -= 1

    # recreate the memory
    arr = []
    for cell in memory:
        if len(cell) == 2:
            for _ in range(cell[1]):
                arr.append(cell[0])
        elif cell[0]:
            for _ in range(cell[1]):
                arr.append(cell[2])
        else:
            for _ in range(cell[1]):
                arr.append('0')
    
    return arr

def get_checksum_blocks(line):
    compacted = compact_blocks(line)
    return sum([int(compacted[i]) * i for i in range(len(compacted))])

def main():
    line = parse()
    res = get_checksum(line)
    print(f"Part 1: {res}")

    res = get_checksum_blocks(line)
    print(f"Part 2: {res}")
    



if __name__ == "__main__":
    main()