import os
from collections import defaultdict

def parse():
    with open('day14.in') as f:
        lines = f.read().strip().splitlines()
        res = []
        for line in lines:
            p_str, v_str = line.split()
            res.append([
                list(map(int, p_str.split('=')[-1].split(','))),
                list(map(int, v_str.split('=')[-1].split(',')))
            ])
        return res
    
def get_safety_score(robots, n, m):
    pos, vels = zip(*robots)
    
    final_pos = []
    for i in range(len(pos)):
        final_x = pos[i][0] + 100 * vels[i][0]
        final_y = pos[i][1] + 100 * vels[i][1]

        final_x %= n
        final_y %= m

        final_pos.append((final_x, final_y))
    
    quadrants = [0] * 4
    for x, y in final_pos:
        if x < n // 2 and y < m // 2:
            quadrants[0] += 1
        elif x > n // 2 and y < m // 2:
            quadrants[1] += 1
        elif x < n // 2 and y > m // 2:
            quadrants[2] += 1
        elif x > n // 2 and y > m // 2:
            quadrants[3] += 1
    
    res = 1
    for q in quadrants:
        res *= q
    return res

def find_when_all_unique(robots, n, m):
    pos, vels = zip(*robots)
    last_touched = [[0] * m for _ in range(n)]

    for t in range(1, 100000):
        duplicate = False
        for i in range(len(pos)):
            pos[i][0] += vels[i][0]
            pos[i][1] += vels[i][1]
            pos[i][0] %= n
            pos[i][1] %= m

            if last_touched[pos[i][0]][pos[i][1]] == t:
                duplicate = True
            last_touched[pos[i][0]][pos[i][1]] = t
        
        if not duplicate:
            return t
    return -1

def main():
    robots = parse()
    res = get_safety_score(robots, 101, 103)
    print(f'Part 1: {res}')

    res = find_when_all_unique(robots, 101, 103)
    print(f'Part 2: {res}')

if __name__ == "__main__":
    main()