from bisect import bisect_left
from collections import defaultdict

def parse():
    with open('day06.in') as f:
        return f.read().splitlines()

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

def check_cycle(row_objs, col_objs, start_i, start_j):
    visited = set()
    di = 0
    i, j = start_i, start_j

    while True:
        match di:
            case 0: # check same col, to smaller index
                idx = bisect_left(col_objs[j], i)
                if idx == 0:
                    break
                new_i = col_objs[j][idx - 1] + 1
                new_j = j
            case 1: # check same row, to larger index
                idx = bisect_left(row_objs[i], j)
                if idx == len(row_objs[i]):
                    break
                new_i = i
                new_j = row_objs[i][idx] - 1
            case 2: # check same col, to larger index
                idx = bisect_left(col_objs[j], i)
                if idx == len(col_objs[j]):
                    break
                new_i = col_objs[j][idx] - 1
                new_j = j
            case 3: # check same row, to smaller index
                idx = bisect_left(row_objs[i], j)
                if idx == 0:
                    break
                new_i = i
                new_j = row_objs[i][idx - 1] + 1
            case _:
                pass

        i, j = new_i, new_j
        if (i, j, di) in visited:
            return True
        visited.add((i, j, di))
        di = (di + 1) % 4
    return False

# TODO: at each step in the path, check if we can make a cycle
def count_possible_cycles(grid):
    n = len(grid)
    m = len(grid[0])

    row_objs = defaultdict(list)
    col_objs = defaultdict(list)
    start_i, start_j = -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                row_objs[i].append(j)
                col_objs[j].append(i)
            if grid[i][j] == "^":
                start_i, start_j = i, j
    
    # print(check_cycle(row_objs, col_objs, start_i, start_j))
    di = 0
    directions = [-1, 0, 1, 0, -1]
    i, j = start_i, start_j
    cycle_positions = set()
    while True:
        new_i, new_j = i + directions[di], j + directions[di + 1]

        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m:
            break

        if grid[new_i][new_j] == '#':
            di = (di + 1) % 4
        else:
            # try to put an object at (new_i, new_j) and see what happens
            if di == 0 or di == 2:
                idx = bisect_left(col_objs[new_j], new_i)
                col_objs[new_j].insert(idx, new_i)
                if check_cycle(row_objs, col_objs, start_i, start_j):
                    cycle_positions.add((new_i, new_j))
                col_objs[new_j].pop(idx)
            else:
                idx = bisect_left(row_objs[new_i], new_j)
                row_objs[new_i].insert(idx, new_j)
                if check_cycle(row_objs, col_objs, start_i, start_j):
                    cycle_positions.add((new_i, new_j))
                row_objs[new_i].pop(idx)
            
            i, j = new_i, new_j
    print(cycle_positions)
    return len(cycle_positions)



def main():
    grid = parse()
    # res = count_tiles(grid)
    # print(f"Part 1: {res}")

    res = count_possible_cycles(grid)
    print(f"Part 2: {res}")

if __name__ == "__main__":
    main()