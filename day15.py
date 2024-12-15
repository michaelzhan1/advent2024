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


def main():
    grid, moves = parse()
    res = make_moves(grid, moves)
    print(f"Part 1: {res}")

if __name__ == "__main__":
    main()