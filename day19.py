from functools import cache

def parse():
    with open('day19.in') as f:
        lines = f.read().strip()
        patterns, goals = lines.split('\n\n')
        patterns = patterns.split(', ')
        goals = goals.split('\n')
        return patterns, goals
    
def try_target(patterns, target):
    # dfs with backtracking
    @cache
    def dfs(i):
        if i == len(target):
            return True
        for pattern in patterns:
            if target.startswith(pattern, i):
                if dfs(i + len(pattern)):
                    return True
        return False
    return dfs(0)
    
def count_possible_targets(patterns, targets):
    return sum(1 for target in targets if try_target(patterns, target))

def count_all_ways_to_make_target(patterns, target):
    @cache
    def dfs(i):
        if i == len(target):
            return 1
        res = 0
        for pattern in patterns:
            if target.startswith(pattern, i):
                res += dfs(i + len(pattern))
        return res
    return dfs(0)

def count_all_ways(patterns, targets):
    return sum(count_all_ways_to_make_target(patterns, target) for target in targets)


def main():
    patterns, targets = parse()
    res = count_possible_targets(patterns, targets)
    print(f'Part 1: {res}')

    res = count_all_ways(patterns, targets)
    print(f'Part 2: {res}')


if __name__ == "__main__":
    main()