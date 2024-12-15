from collections import deque

def parse():
    with open('day15.in') as f:
        grid, moves = f.read().strip().split('\n\n')
        grid = [list(line) for line in grid.split('\n')]
        moves = ''.join(moves.split('\n'))
        return grid, moves
    
def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()
    
def make_moves(grid, moves):
    n = len(grid)
    m = len(grid[0])
    
    # find starting point
    start_i, start_j = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                start_i, start_j = i, j
                break
    
    # make moves
    directions = [-1, 0, 1, 0, -1]
    move_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    i, j = start_i, start_j
    for move in moves:
        direction_i = move_map[move]
        di = directions[direction_i]
        dj = directions[direction_i + 1]

        ni = i + di
        nj = j + dj

        # track first element in chain for quick movements
        first_element_i = ni
        first_element_j = nj
        
        # move through chain
        while grid[ni][nj] == 'O':
            ni += di
            nj += dj
        
        if grid[ni][nj] == '#':
            continue
        
        grid[ni][nj] = grid[first_element_i][first_element_j]
        grid[first_element_i][first_element_j] = '@'
        grid[i][j] = '.'

        i, j = first_element_i, first_element_j

    # calculate score
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                res += 100 * i + j
    return res

def build_larger_grid(grid):
    res = []
    for row in grid:
        new_row = []
        for char in row:
            if char == '#':
                new_row.extend(['#', '#'])
            elif char == 'O':
                new_row.extend(['[', ']'])
            elif char == '.':
                new_row.extend(['.', '.'])
            else:
                new_row.extend(['@', '.'])
        res.append(new_row)
    return res

def make_moves_large(grid, moves):
    n = len(grid)
    m = len(grid[0])

    # find starting point
    start_i, start_j = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                start_i, start_j = i, j
                break
    
    # make moves
    i, j = start_i, start_j

    for move in moves:        
        # move right
        if move == '>':
            ni, nj = i, j + 1

            # get the list of boxes to move right
            to_move_right = []
            while grid[ni][nj] == '[':
                to_move_right.append((ni, nj))
                nj += 2
            
            # can't move right
            if grid[ni][nj] == '#':
                continue
            
            # push boxes
            for box_left_i, box_left_j in to_move_right:
                grid[box_left_i][box_left_j + 1] = '['
                grid[box_left_i][box_left_j + 2] = ']'
            
            # move robot
            grid[i][j + 1] = '@'
            grid[i][j] = '.'

            j += 1

        # move left
        elif move == '<':
            ni, nj = i, j - 1
                
            # get the list of boxes to move left
            to_move_left = []
            while grid[ni][nj] == ']':
                to_move_left.append((ni, nj))
                nj -= 2
            
            # can't move left
            if grid[ni][nj] == '#':
                continue
            
            # push boxes
            for box_left_i, box_left_j in to_move_left:
                grid[box_left_i][box_left_j - 1] = ']'
                grid[box_left_i][box_left_j - 2] = '['
            
            # move robot
            grid[i][j - 1] = '@'
            grid[i][j] = '.'

            j -= 1

        # move down
        elif move == 'v':
            ni, nj = i + 1, j

            # get list of boxes to move down (bfs, each node is the left bracket)
            to_move_down = deque()
            seen = set()
            if grid[ni][nj] == '[':
                to_move_down.append((ni, nj))
                seen.add((ni, nj))
            elif grid[ni][nj] == ']':
                to_move_down.append((ni, nj - 1))
                seen.add((ni, nj - 1))

            can_move_down = grid[ni][nj] != '#'
            while to_move_down:
                left_bracket_i, left_bracket_j = to_move_down.popleft()
                if grid[left_bracket_i + 1][left_bracket_j] == '[':
                    to_move_down.append((left_bracket_i + 1, left_bracket_j))
                    seen.add((left_bracket_i + 1, left_bracket_j))
                
                if grid[left_bracket_i + 1][left_bracket_j] == ']':
                    to_move_down.append((left_bracket_i + 1, left_bracket_j - 1))
                    seen.add((left_bracket_i + 1, left_bracket_j - 1))
                
                if grid[left_bracket_i + 1][left_bracket_j + 1] == '[':
                    to_move_down.append((left_bracket_i + 1, left_bracket_j + 1))
                    seen.add((left_bracket_i + 1, left_bracket_j + 1))
                
                # check if we can't move down
                if grid[left_bracket_i + 1][left_bracket_j] == '#' or grid[left_bracket_i + 1][left_bracket_j + 1] == '#':
                    can_move_down = False
                    break
            
            if not can_move_down:
                continue

            # push boxes
            for box_left_i, box_left_j in sorted(list(seen), reverse=True):
                grid[box_left_i + 1][box_left_j] = '['
                grid[box_left_i + 1][box_left_j + 1] = ']'

                grid[box_left_i][box_left_j] = '.'
                grid[box_left_i][box_left_j + 1] = '.'
            
            # move robot
            grid[i + 1][j] = '@'
            grid[i][j] = '.'

            i += 1
        
        # move up
        elif move == '^':
            ni, nj = i - 1, j

            # get list of boxes to move up (bfs, each node is the left bracket)
            to_move_up = deque()
            seen = set()
            if grid[ni][nj] == '[':
                to_move_up.append((ni, nj))
                seen.add((ni, nj))
            elif grid[ni][nj] == ']':
                to_move_up.append((ni, nj - 1))
                seen.add((ni, nj - 1))

            can_move_up = grid[ni][nj] != '#'

            while to_move_up:
                left_bracket_i, left_bracket_j = to_move_up.popleft()
                if grid[left_bracket_i - 1][left_bracket_j] == '[':
                    to_move_up.append((left_bracket_i - 1, left_bracket_j))
                    seen.add((left_bracket_i - 1, left_bracket_j))
                
                if grid[left_bracket_i - 1][left_bracket_j] == ']':
                    to_move_up.append((left_bracket_i - 1, left_bracket_j - 1))
                    seen.add((left_bracket_i - 1, left_bracket_j - 1))
                
                if grid[left_bracket_i - 1][left_bracket_j + 1] == '[':
                    to_move_up.append((left_bracket_i - 1, left_bracket_j + 1))
                    seen.add((left_bracket_i - 1, left_bracket_j + 1))
                
                # check if we can't move up
                if grid[left_bracket_i - 1][left_bracket_j] == '#' or grid[left_bracket_i - 1][left_bracket_j + 1] == '#':
                    can_move_up = False
                    break

            if not can_move_up:
                continue

            # push boxes
            for box_left_i, box_left_j in sorted(list(seen)):
                grid[box_left_i - 1][box_left_j] = '['
                grid[box_left_i - 1][box_left_j + 1] = ']'

                grid[box_left_i][box_left_j] = '.'
                grid[box_left_i][box_left_j + 1] = '.'

            # move robot
            grid[i - 1][j] = '@'
            grid[i][j] = '.'

            i -= 1

    # calculate score
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '[':
                res += 100 * i + j
    return res


def main():
    grid, moves = parse()
    res = make_moves(grid, moves)
    print(f"Part 1: {res}")

    grid, moves = parse()
    larger_grid = build_larger_grid(grid)
    res = make_moves_large(larger_grid, moves)
    print(f"Part 2: {res}")

if __name__ == "__main__":
    main()