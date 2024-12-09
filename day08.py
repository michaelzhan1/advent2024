from collections import defaultdict
from math import gcd

def parse():
    with open('day08.in') as f:
        return f.read().splitlines()
    
def count_antinodes(grid):
    n = len(grid)
    m = len(grid[0])

    nodes = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                nodes[grid[i][j]].append((i, j))
    
    # pairwise, count antinodes
    antinodes = set()
    for node in nodes:
        for i in range(len(nodes[node])):
            for j in range(i+1, len(nodes[node])):
                node1 = nodes[node][i]
                node2 = nodes[node][j]
                dx = node2[0] - node1[0]
                dy = node2[1] - node1[1]

                antinode1 = (node1[0] - dx, node1[1] - dy)
                antinode2 = (node2[0] + dx, node2[1] + dy)
                if 0 <= antinode1[0] < n and 0 <= antinode1[1] < m:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < n and 0 <= antinode2[1] < m:
                    antinodes.add(antinode2)
    return len(antinodes)

def count_antinodes_line(grid):
    n = len(grid)
    m = len(grid[0])

    nodes = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                nodes[grid[i][j]].append((i, j))
    
    # pairwise, count antinodes
    antinodes = set()
    for node in nodes:
        for i in range(len(nodes[node])):
            for j in range(i+1, len(nodes[node])):
                node1 = nodes[node][i]
                node2 = nodes[node][j]
                dx = node2[0] - node1[0]
                dy = node2[1] - node1[1]

                if dx == 0 or dy == 0:
                    if dx == 0:
                        dy = 1
                    if dy == 0:
                        dx = 1
                else:
                    factor = gcd(dx, dy)
                    dx //= factor
                    dy //= factor
                
                # go down
                cur_x, cur_y = node1
                while 0 <= cur_x + dx < n and 0 <= cur_y + dy < m:
                    cur_x += dx
                    cur_y += dy
                    antinodes.add((cur_x, cur_y))

                while 0 <= cur_x - dx < n and 0 <= cur_y - dy < m:
                    cur_x -= dx
                    cur_y -= dy
                    antinodes.add((cur_x, cur_y))

    return len(antinodes)
                    
    
def main():
    grid = parse()
    res = count_antinodes(grid)
    print(f"Part 1: {res}")

    res = count_antinodes_line(grid)
    print(f"Part 2: {res}")



if __name__ == "__main__":
    main()