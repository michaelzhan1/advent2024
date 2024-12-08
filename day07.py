from functools import cache

def parse():
    with open('day07.in') as f:
        lines = f.read().splitlines()
        target = []
        nums = []
        for line in lines:
            line = line.split(':')
            target.append(int(line[0]))
            nums.append(list(map(int, line[1].strip().split())))
        return target, nums
    
def check_valid_row_mult_sum(target, nums):
    @cache
    def _helper(i, cur):
        if i == len(nums):
            return cur == target
        return _helper(i + 1, cur + nums[i]) or _helper(i + 1, cur * nums[i])
    
    return _helper(1, nums[0])


def sum_valid_rows(target, nums):
    n = len(target)
    res = 0
    for i in range(n):
        if check_valid_row_mult_sum(target[i], nums[i]):
            res += target[i]
    return res

def check_valid_row_mult_sum_concat(target, nums):
    @cache
    def _helper(i, cur):
        if i == len(nums):
            return cur == target
        return _helper(i + 1, cur + nums[i]) or _helper(i + 1, cur * nums[i]) or _helper(i + 1, int(str(cur) + str(nums[i])))
    
    return _helper(1, nums[0])

def sum_valid_rows_2(target, nums):
    n = len(target)
    res = 0
    for i in range(n):
        if check_valid_row_mult_sum_concat(target[i], nums[i]):
            res += target[i]
    return res
    

def main():
    target, nums = parse()
    res = sum_valid_rows(target, nums)
    print(f"Part 1: {res}")

    res = sum_valid_rows_2(target, nums)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()