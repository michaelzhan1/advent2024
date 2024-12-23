def parse():
    with open('day21.in') as f:
        return f.read().splitlines()
    
def get_key_presses(sequence, keypad_type):
    if keypad_type == 1:
        keypad = ['789', '456', '123', '.0A']
        n = len(keypad)
        m = len(keypad[0])
    else:
        keypad = ['.^A', '<v>']
        n = len(keypad)
        m = len(keypad[0])

    positions = {keypad[i][j]: (i, j) for i in range(n) for j in range(m)}
    i, j = positions['A']
    gap_i, gap_j = positions['.']

    move = ''
    for char in sequence:
        new_i, new_j = positions[char]
        i_char = 'v' if new_i > i else '^' if new_i < i else ''
        j_char = '>' if new_j > j else '<' if new_j < j else ''

        di = abs(new_i - i)
        dj = abs(new_j - j)

        if (i == gap_i and new_j == gap_j) or (new_i == gap_i and j == gap_j):
            # horizontal first
            if i == gap_i and new_j == gap_j:
                move += i_char * di + j_char * dj + 'A'
            else:
                move += j_char * dj + i_char * di + 'A'
        else:
            # up right or down right: press vertical first
            if (new_i < i and new_j > j) or (new_i > i and new_j > j):
                move += di * i_char + dj * j_char + 'A'
            else:
                move += dj * j_char + di * i_char + 'A'

        i, j = new_i, new_j

    return move

def get_complexity(original_code):
    code1 = get_key_presses(original_code, 1)
    code2 = get_key_presses(code1, 2)
    code3 = get_key_presses(code2, 2)
    return len(code3) * int(original_code[:-1])
    
def get_complexities(codes):
    res = 0
    for code in codes:
        res += get_complexity(code)
    return res

def get_complexity_25(original_code):
    code = get_key_presses(original_code, 1)
    for _ in range(25):
        code = get_key_presses(code, 2)
    return len(code) * int(original_code[:-1])

def get_complexities_25(codes):
    res = 0
    for code in codes:
        print(code)
        res += get_complexity_25(code)
    return res

def main():
    codes = parse()
    res = get_complexities(codes)
    print(f"Part 1: {res}")

    res = get_complexities_25(codes)
    print(f"Part 2: {res}")



if __name__ == "__main__":
    main()