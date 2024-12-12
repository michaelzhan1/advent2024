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

def get_price_sides(grid):
    n = len(grid)
    m = len(grid[0])

    visited = [[False] * m for _ in range(n)]
    areas = []
    side_counts = []

    def calc_area(i, j, potential_sides):
        visited[i][j] = True
        area = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or grid[ni][nj] != grid[i][j]:
                if (di, dj) == (-1, 0):
                    potential_sides.append((i, j, 0))
                elif (di, dj) == (0, 1):
                    potential_sides.append((i, j, 1))
                elif (di, dj) == (1, 0):
                    potential_sides.append((i, j, 2))
                elif (di, dj) == (0, -1):
                    potential_sides.append((i, j, 3))

            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]:
                continue

            if grid[ni][nj] == grid[i][j]:
                area += calc_area(ni, nj, potential_sides)
            
        return area
    
    # first, prep side counts for each cell
    # up, right, down, left
    sides = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]
    directions = [-1, 0, 1, 0, -1]
    for i in range(n):
        for j in range(m):
            for di in range(4):
                ni, nj = i + directions[di], j + directions[di + 1]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    sides[i][j][di] = True
                elif grid[ni][nj] != grid[i][j]:
                    sides[i][j][di] = True

    visited_sides = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]
    
    def find_num_sides(i, j, side_i):
        starting_pos = (i, j, side_i)
        first_step = True
        side_count = 0

        # define directions like this. an "up" side while going clockwise means we're checking to the right
        directions = [0, 1, 0, -1, 0]

        while (i, j, side_i) != starting_pos or first_step:
            visited_sides[i][j][side_i] = True

            first_step = False
            # first, check if there are other sides clockwise of the current side
            if sides[i][j][(side_i + 1) % 4]:
                side_i = (side_i + 1) % 4
                side_count += 1
                continue

            # if not, try for the next cell with the same side. OOB should never happen and should be handled by the first case
            di, dj = directions[side_i], directions[side_i + 1]
            if sides[i + di][j + dj][side_i]:
                i, j = i + di, j + dj

            # otherwise, we need to make a diagonal step. This should also always be legal
            else:
                match side_i:
                    case 0:
                        i -= 1
                        j += 1
                    case 1:
                        i += 1
                        j += 1
                    case 2:
                        i += 1
                        j -= 1
                    case 3:
                        i -= 1
                        j -= 1
                    case _:
                        assert False, "Invalid side index"
                side_count += 1
                side_i = (side_i + 3) % 4
        return side_count

    
    for i in range(n):
        for j in range(m):
            potential_sides = []
            if not visited[i][j]:
                area = calc_area(i, j, potential_sides)
                areas.append(area)
                    
                side_count = 0
                for i, j, side_i in potential_sides:
                    if not visited_sides[i][j][side_i]:
                        side_count += find_num_sides(i, j, side_i)
                side_counts.append(side_count)

    
    res = 0
    for a, s in zip(areas, side_counts):
        res += a * s
    return res

def main():
    grid = parse()
    res = get_price(grid)
    print(f"Part 1: {res}")

    res = get_price_sides(grid)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()