import os
import pickle
from collections import Counter

def parse():
    with open('day22.in') as f:
        return list(map(int, f.read().splitlines()))

def iter_secret(num):
    num = ((num << 6) ^ num) & 0xFFFFFF
    num = ((num >> 5) ^ num) & 0xFFFFFF
    num = ((num << 11) ^ num) & 0xFFFFFF
    return num

def write_all_nums(all_nums):
    with open('data/day22.pkl', 'wb') as f:
        pickle.dump(all_nums, f)

def get_all_nums(secrets):
    if os.path.exists('data/day22.pkl'):
        with open('data/day22.pkl', 'rb') as f:
            return pickle.load(f)
    
    all_nums = []
    for num in secrets:
        nums = [num]
        for _ in range(2000):
            nums.append(iter_secret(nums[-1]))
        all_nums.append(nums)
    write_all_nums(all_nums)
    return all_nums
    
def find_total_score(secrets):
    all_nums = get_all_nums(secrets)
    return sum(nums[-1] for nums in all_nums)

def find_best_sequence(secrets):
    all_nums = get_all_nums(secrets)
    all_diffs = [[(nums[i] % 10) - (nums[i - 1] % 10) for i in range(1, len(nums))] for nums in all_nums]
    
    total_prices = Counter()
    used = [set() for _ in range(len(all_diffs))]

    for i in range(len(all_diffs)):
        for j in range(len(all_diffs[0]) - 3):
            window = tuple(all_diffs[i][j:j + 4])
            if window in used[i]:
                continue

            used[i].add(window)
            total_prices[window] += all_nums[i][j + 4] % 10

    return max(total_prices.values())

def main():
    secrets = parse()
    res = find_total_score(secrets)
    print(f"Part 1: {res}")

    res = find_best_sequence(secrets)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()
