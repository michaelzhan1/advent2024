from collections import deque

def parse():
    with open('day10.in') as f:
        lines = f.readlines()
        res = [list(map(int, line.strip())) for line in lines]
        return res
    
def get_trailhead_score(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    count = 0
    queue = deque([(i, j)])
    seen = {(i, j)}

    while queue:
        i, j = queue.popleft()
        if grid[i][j] == 9:
            count += 1
            continue

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == grid[i][j] + 1 and (ni, nj) not in seen:
                queue.append((ni, nj))
                seen.add((ni, nj))
    return count

    
def sum_trailhead_scores(grid):
    n = len(grid)
    m = len(grid[0])
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                res += get_trailhead_score(grid, i, j)
    return res

def get_trailhead_score_full(grid, i, j):
    n = len(grid)
    m = len(grid[0])
    count = 0
    queue = deque([(i, j)])

    while queue:
        i, j = queue.popleft()
        if grid[i][j] == 9:
            count += 1
            continue

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == grid[i][j] + 1:
                queue.append((ni, nj))
    return count

def sum_trailhead_scores_again(grid):
    n = len(grid)
    m = len(grid[0])
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                res += get_trailhead_score_full(grid, i, j)
    return res


def main():
    grid = parse()
    res = sum_trailhead_scores(grid)
    print(f"Part 1: {res}")

    res = sum_trailhead_scores_again(grid)
    print(f"Part 2: {res}")

if __name__ == "__main__":
    main()