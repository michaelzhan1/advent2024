from math import log
from functools import cache

def parse():
    with open('day11.in') as f:
        return list(map(int, f.readline().strip().split()))
    
def blink(stones):
    res = []
    for stone in stones:
        if stone == 0:
            res.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            res.append(int(stone_str[:len(stone_str) // 2]))
            res.append(int(stone_str[len(stone_str) // 2:]))
        else:
            res.append(stone * 2024)
    return res

@cache
def count_single_stone_after_n_blinks(stone, n):
    if n == 0:  # base case
        return 1
    
    if stone == 0:
        return count_single_stone_after_n_blinks(1, n - 1)
    
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        return count_single_stone_after_n_blinks(int(stone_str[:len(stone_str) // 2]), n - 1) + count_single_stone_after_n_blinks(int(stone_str[len(stone_str) // 2:]), n - 1)
    else:
        return count_single_stone_after_n_blinks(stone * 2024, n - 1)
    

def blink_n_times(stones, n):
    for _ in range(n):
        stones = blink(stones)
    return len(stones)

def count_stones_after_n_blinks(stones, n):
    res = 0
    for stone in stones:
        res += count_single_stone_after_n_blinks(stone, n)
    return res

def main():
    stones = parse()
    res = blink_n_times(stones, 25)
    print(f"Part 1: {res}")

    res = count_stones_after_n_blinks(stones, 75)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()