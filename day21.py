def parse():
    with open('day21.in') as f:
        return f.read().splitlines()
    
def get_key_presses(sequence, keypad_type):
    if keypad_type == 1:
        keypad = ['789', '456', '123', '.0A']
        positions = {keypad[i][j]: (i, j) for i in range(len(keypad)) for j in range(len(keypad[i]))}
        i, j = positions['A']
        all_res = []
        for char in sequence:
            new_moves = set()
            new_i, new_j = positions[char]

            i_char = 'v' if new_i > i else '^' if new_i < i else ''
            j_char = '>' if new_j > j else '<' if new_j < j else ''
            di = abs(new_i - i)
            dj = abs(new_j - j)

            # add horizontal first: can't move from 0A line to first column
            if not (i == 3 and new_j == 0):
                new_moves.add(j_char * dj + i_char * di + 'A')
            
            # add vertical first: can't move from left column to 0A line in this manner
            if not (new_i == 3 and j == 0):
                new_moves.add(i_char * di + j_char * dj + 'A')
            
            i, j = new_i, new_j

            if len(all_res) == 0:
                all_res = list(new_moves)
            else:
                all_res = [res + new_move for res in all_res for new_move in new_moves]
        return all_res
    elif keypad_type == 2:
        keypad = ['.^A', '<v>']
        positions = {keypad[i][j]: (i, j) for i in range(len(keypad)) for j in range(len(keypad[i]))}
        i, j = positions['A']
        all_res = []
        for char in sequence:
            new_moves = set()
            new_i, new_j = positions[char]

            i_char = 'v' if new_i > i else '^' if new_i < i else ''
            j_char = '>' if new_j > j else '<' if new_j < j else ''
            di = abs(new_i - i)
            dj = abs(new_j - j)

            # horizontal first: can't move from ^A line to first column in this manner
            if not (i == 0 and new_j == 0):
                new_moves.add(j_char * dj + i_char * di + 'A')

            # vertical first: can't move from left column to ^A line in this manner
            if not (new_i == 0 and j == 0):
                new_moves.add(i_char * di + j_char * dj + 'A')
            
            i, j = new_i, new_j

            if len(all_res) == 0:
                all_res = list(new_moves)
            else:
                all_res = [res + new_move for res in all_res for new_move in new_moves]
        return all_res
                

def get_complexity(original_code):
    # first abstraction
    codes_1 = get_key_presses(original_code, 1)
    
    # second abstraction
    codes_2 = []
    for code in codes_1:
        codes_2 += get_key_presses(code, 2)
        min_length = min(map(len, codes_2))
        codes_2 = [code for code in codes_2 if len(code) == min_length]
    
    # last abstraction
    codes_3 = []
    for code in codes_2:
        codes_3 += get_key_presses(code, 2)
        min_length = min(map(len, codes_3))
        codes_3 = [code for code in codes_3 if len(code) == min_length]
    
    return len(codes_3[0]) * int(original_code[:-1])

    
def get_complexities(codes):
    res = 0
    for code in codes:
        res += get_complexity(code)
    return res

def main():
    codes = parse()
    print(get_complexities(codes))



if __name__ == "__main__":
    main()