def parse():
    with open('day12.in') as f:
        return f.read().splitlines()

def get_price(grid):
    n = len(grid)
    m = len(grid)
    visited = [[False] * m for _ in range(n)]

    perimeters = []
    areas = []

    def dfs(i, j):
        visited[i][j] = True
        crop = grid[i][j]

        # check perimeter
        own_area = 1
        own_perimeter = 0
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] != crop:
                own_perimeter += 1

            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]:
                continue

            if grid[ni][nj] == crop:
                other_area, other_perimeter = dfs(ni, nj)
                own_area += other_area
                own_perimeter += other_perimeter
        return own_area, own_perimeter
        
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                area, perimeter = dfs(i, j)
                areas.append(area)
                perimeters.append(perimeter)

    res = 0
    for a, p in zip(areas, perimeters):
        res += a * p
    return res

def main():
    grid = parse()
    res = get_price(grid)
    print(f"Part 1: {res}")


if __name__ == "__main__":
    main()