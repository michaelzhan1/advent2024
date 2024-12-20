from functools import cache

def parse():
    with open('day20.in') as f:
        lines = f.read().splitlines()
        return lines
    
def count_skips(grid, skip_threshold):
    # idea: do a regular dfs-based fastest path search
    # then, for each point, check places manhattan distance 2 away and see if we can make a shortcut
    end_i, end_j = -1, -1

    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                end_i, end_j = i, j
                break

    min_distance = [[float('inf')] * m for _ in range(n)]
    distance = 0

    # at each point, have the minimum distance to the end
    i, j = end_i, end_j
    while True:
        min_distance[i][j] = distance
        if grid[i][j] == 'S':
            break

        distance += 1
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if grid[ni][nj] == '#' or min_distance[ni][nj] != float('inf'):
                continue

            i, j = ni, nj
            break
    
    # go through the path and see if we can make any shortcuts that save at least skip_threshold
    res = 0
    while grid[i][j] != 'E':
        # first, check within manhattan distance of 2
        for ni, nj in [(i + 2, j), (i - 2, j), (i, j + 2), (i, j - 2), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)]:
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if grid[ni][nj] == '#' or min_distance[ni][nj] == float('inf'):
                continue

            skip_distance = min_distance[i][j] - min_distance[ni][nj] - 2
            if skip_distance >= skip_threshold:
                res += 1
        
        # then, move
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if min_distance[ni][nj] == distance - 1:
                i, j = ni, nj
                distance -= 1
                break
    return res
    

def main():
    grid = parse()
    res = count_skips(grid, 100)
    print(f'Part 1: {res}')


if __name__ == "__main__":
    main()