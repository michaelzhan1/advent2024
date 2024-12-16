import heapq

def parse():
    with open('day16.in') as f:
        grid = f.read().strip().splitlines()
        return grid
    
def find_lowest_score(grid):
    n = len(grid)
    m = len(grid[0])

    # find start and end
    start_i, start_j, end_i, end_j = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start_i, start_j = i, j
            if grid[i][j] == 'E':
                end_i, end_j = i, j

    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    best_cost = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
    best_cost[start_i][start_j][1] = 0
    pq = [(0, start_i, start_j, 1)]  # cost, i, j, last_dir

    directions = [-1, 0, 1, 0, -1]
    while pq:
        cost, i, j, last_dir = heapq.heappop(pq)
        if visited[i][j][last_dir]:
            continue
        visited[i][j][last_dir] = True

        if i == end_i and j == end_j:
            return cost

        for d_idx in range(4):
            di, dj = directions[d_idx], directions[d_idx + 1]
            ni, nj = i + di, j + dj
            if grid[ni][nj] == '#':
                continue

            turn_cost = 1000 if d_idx != last_dir else 0
            new_cost = cost + turn_cost + 1
            if new_cost <= best_cost[ni][nj][d_idx]:
                best_cost[ni][nj][d_idx] = new_cost
                heapq.heappush(pq, (new_cost, ni, nj, d_idx))
    return -1


def main():
    grid = parse()
    res = find_lowest_score(grid)
    print(f"Part 1: {res}")


if __name__ == "__main__":
    main()