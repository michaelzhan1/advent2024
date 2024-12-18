from collections import deque

def parse():
    with open('day18.in') as f:
        bytes = f.read().splitlines()
        res = [list(map(int, line.split(','))) for line in bytes]
        return res

def reach_exit(bytes, n, num_bytes):
    obstacles = set()
    for i in range(num_bytes):
        obstacles.add((bytes[i][0], bytes[i][1]))
    
    res = 0
    queue = deque([(0, 0)])
    seen = set([(0, 0)])
    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.popleft()
            if i == n - 1 and j == n - 1:
                return res
            
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or x >= n or y < 0 or y >= n or (x, y) in obstacles or (x, y) in seen:
                    continue
                    
                queue.append((x, y))
                seen.add((x, y))
        res += 1
    return -1

def find_first_byte(bytes, n, num_bytes):
    obstacles = set()
    for i in range(num_bytes):
        obstacles.add((bytes[i][0], bytes[i][1]))

    def run_bfs():
        res = 0
        queue = deque([(0, 0)])
        seen = set([(0, 0)])
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if i == n - 1 and j == n - 1:
                    return res
                
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or x >= n or y < 0 or y >= n or (x, y) in obstacles or (x, y) in seen:
                        continue
                        
                    queue.append((x, y))
                    seen.add((x, y))
            res += 1
        return -1
    
    for i in range(num_bytes, len(bytes)):
        obstacles.add((bytes[i][0], bytes[i][1]))
        res = run_bfs()
        if res == -1:
            return f'{bytes[i][0]},{bytes[i][1]}'
                

def main():
    bytes = parse()
    res = reach_exit(bytes, 71, 1024)
    print(f'Part 1: {res}')

    res = find_first_byte(bytes, 71, 1024)
    print(f'Part 2: {res}')



if __name__ == "__main__":
    main()