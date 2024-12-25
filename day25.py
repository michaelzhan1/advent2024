def parse():
    n = 7
    m = 5

    with open('day25.in') as f:
        data = f.read().strip().split('\n\n')
        locks = []
        keys = []
        for grid in data:
            grid = grid.split('\n')
            if grid[0] == '.....':  # key
                i_iter = range(n - 1, -1, -1)
                group = keys
            else:
                i_iter = range(n)
                group = locks
            
            cols = []
            for j in range(m):
                count = 0
                for i in i_iter:
                    if grid[i][j] == '#':
                        count += 1
                    else:
                        break
                cols.append(count)
            group.append(tuple(cols))

        return locks, keys


def count_possible_pairs(locks, keys):

    res = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if lock[i] + key[i] > 7:
                    break
            else:
                res += 1
    return res

def main():
    locks, keys = parse()
    res = count_possible_pairs(locks, keys)
    print(f'Part 1: {res}')


if __name__ == "__main__":
    main()