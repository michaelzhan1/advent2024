def parse():
    with open("day02.in", "r") as file:
        lines = file.readlines()
        return [list(map(int, line.split())) for line in lines]
    
def check_safe(arr):
    if arr[0] == arr[1]:
        return False
    if arr[0] < arr[1]:
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1] or abs(arr[i] - arr[i + 1]) > 3 or abs(arr[i] - arr[i + 1]) < 1:
                return False
    else:
        for i in range(len(arr) - 1):
            if arr[i] <= arr[i + 1] or abs(arr[i] - arr[i + 1]) > 3 or abs(arr[i] - arr[i + 1]) < 1:
                return False
    return True

def check_safe2(arr):
    if check_safe(arr):
        return True
    for i in range(len(arr)):
        if check_safe(arr[:i] + arr[i + 1:]):
            return True
    return False

def main():
    lines = parse()
    res = 0
    for line in lines:
        if check_safe(line):
            res += 1
    print(f"Part 1: {res}")

    res = 0
    for line in lines:
        if check_safe2(line):
            res += 1
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()