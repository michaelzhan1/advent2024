from functools import cache

def parse():
    with open('day21.in') as f:
        return f.read().splitlines()

def generate_paths():
    paths = {
        'digits': {},
        'directions': {}
    }

    kps = [
        ['789', '456', '123', '.0A'],
        ['.^A', '<v>']
    ]

    names = ['digits', 'directions']

    for i in range(2):
        keypad = kps[i]
        n = len(keypad)
        m = len(keypad[0])
        positions = {keypad[i][j]: (i, j) for i in range(n) for j in range(m)}

        gap_i, gap_j = positions['.']
        
        for key1 in positions:
            for key2 in positions:
                if key1 == '.' or key2 == '.':
                    continue

                i1, j1 = positions[key1]
                i2, j2 = positions[key2]

                di = abs(i2 - i1)
                dj = abs(j2 - j1)

                i_char = 'v' if i2 > i1 else '^' if i2 < i1 else ''
                j_char = '>' if j2 > j1 else '<' if j2 < j1 else ''


                if i1 == i2 and j1 == j2:
                    move = 'A'
                elif (i1 == gap_i and j2 == gap_j) or (i2 == gap_i and j1 == gap_j):
                    if i1 == gap_i and j2 == gap_j:
                        move = i_char * di + j_char * dj + 'A'
                    else:
                        move = j_char * dj + i_char * di + 'A'
                else:
                    if (i2 < i1 and j2 > j1) or (i2 > i1 and j2 > j1):
                        move = di * i_char + dj * j_char + 'A'
                    else:
                        move = dj * j_char + di * i_char + 'A'

                paths[names[i]][(key1, key2)] = move
    return paths

def get_final_length(code, times):
    all_paths = generate_paths()

    @cache
    def count(code, remaining):
        if remaining == times: # first time
            paths = all_paths['digits']
        else:
            paths = all_paths['directions']

        if remaining == 0:
            return len(code)
        
        prev = 'A'
        res = 0
        for char in code:
            res += count(paths[(prev, char)], remaining - 1)
            prev = char
        return res
    
    return count(code, times)

def get_total_complexity(codes, count):
    res = 0
    for code in codes:
        res += get_final_length(code, count) * int(code[:-1])
    return res
        
def main():
    codes = parse()
    res = get_total_complexity(codes, 3)
    print(f"Part 1: {res}")

    res = get_total_complexity(codes, 26)
    print(f"Part 2: {res}")

if __name__ == "__main__":
    main()