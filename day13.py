def parse():
    with open('day13.in') as f:
        lines = f.read().strip()
        groups = lines.split('\n\n')
        
        res = []
        for group in groups:
            a_info, b_info, goal_info = group.split('\n')
            a_info = a_info.split()[2:]
            b_info = b_info.split()[2:]
            goal_info = goal_info.split()[1:]

            res.append([
                [int(a_info[0][1:-1]), int(a_info[1][1:])],
                [int(b_info[0][1:-1]), int(b_info[1][1:])],
                [int(goal_info[0][2:-1]), int(goal_info[1][2:])]
            ])
        return res

def count_min_tokens(games):
    token_count = 0
    for game in games:
        (a1, a2), (b1, b2), (c1, c2) = game

        numerator = a1 * c2 - a2 * c1
        denominator = a1 * b2 - a2 * b1
        if numerator % denominator != 0:
            continue

        y = numerator // denominator
        numerator = c1 - b1 * y
        if numerator % a1 != 0:
            continue

        x = numerator // a1

        if x >= 0 and y >= 0:
            token_count += 3 * x + y
    return token_count

def count_min_tokens_large(games):
    token_count = 0
    for game in games:
        (a1, a2), (b1, b2), (c1, c2) = game
        c1 += 10000000000000
        c2 += 10000000000000

        numerator = a1 * c2 - a2 * c1
        denominator = a1 * b2 - a2 * b1
        if numerator % denominator != 0:
            continue

        y = numerator // denominator
        numerator = c1 - b1 * y
        if numerator % a1 != 0:
            continue

        x = numerator // a1

        if x >= 0 and y >= 0:
            token_count += 3 * x + y
    return token_count

def main():
    games = parse()
    res = count_min_tokens(games)
    print(f'Part 1: {res}')

    res = count_min_tokens_large(games)
    print(f'Part 2: {res}')


if __name__ == "__main__":
    main()