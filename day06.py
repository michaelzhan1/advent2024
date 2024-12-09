def parse():
    with open('day06.in') as f:
        lines = f.read().splitlines()
        return [list(line) for line in lines]

def count_tiles(grid):
    n = len(grid)
    m = len(grid[0])
    
    start_i = -1
    start_j = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                start_i, start_j = i, j
                break
    if start_i == -1:
        return 0
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_i][start_j] = True
    di = 0
    directions = [-1, 0, 1, 0, -1]

    i, j = start_i, start_j
    while True:        
        new_i = i + directions[di]
        new_j = j + directions[di + 1]

        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
            break

        if grid[new_i][new_j] == '#':
            di = (di + 1) % 4
        else:
            visited[new_i][new_j] = True
            i, j = new_i, new_j
    step_count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                step_count += 1
    return step_count

def check_cycle(grid, start_i, start_j):
    n = len(grid)
    m = len(grid[0])
    
    di = 0
    directions = [-1, 0, 1, 0, -1]
    visited = set()
    i, j = start_i, start_j
    while True:
        new_i = i + directions[di]
        new_j = j + directions[di + 1]

        if (i, j, di) in visited:
            return True

        visited.add((i, j, di))

        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
            break
        
        if grid[new_i][new_j] == '#':
            di = (di + 1) % 4
        else:
            i = new_i
            j = new_j
    return False

def count_possible_cycles(grid):
    n = len(grid)
    m = len(grid[0])

    start_i, start_j = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                start_i, start_j = i, j

    i, j = start_i, start_j
    di = 0
    directions = [-1, 0, 1, 0, -1]
    cycle_positions = set()
    while True:
        new_i = i + directions[di]
        new_j = j + directions[di + 1]

        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
            break

        if grid[new_i][new_j] == '#':
            di = (di + 1) % 4
        else:
            if start_i != new_i or start_j != new_j:
                grid[new_i][new_j] = '#'
                if check_cycle(grid, start_i, start_j):
                    cycle_positions.add((new_i, new_j))
                grid[new_i][new_j] = '.'
            i, j = new_i, new_j
    return len(cycle_positions)

def main():
    grid = parse()
    res = count_tiles(grid)
    print(f"Part 1: {res}")

    res = count_possible_cycles(grid)
    print(f"Part 2: {res}")

if __name__ == "__main__":
    main()