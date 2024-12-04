def parse():
    with open("day04.in", 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def count_xmas(lines):
    n = len(lines)
    m = len(lines[0])

    res = 0
    for i in range(n):
        for j in range(m):
            if i < n - 3:
                if lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
                    res += 1
            if j < m - 3:
                if lines[i][j] == 'X' and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
                    res += 1
            if i < n - 3 and j < m - 3:
                if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
                    res += 1
            if i < n - 3 and j >= 3:
                if lines[i][j] == 'X' and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
                    res += 1
            if i >= 3 and j < m - 3:
                if lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
                    res += 1
            if i >= 3 and j >= 3:
                if lines[i][j] == 'X' and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
                    res += 1
            if i >= 3:
                if lines[i][j] == 'X' and lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
                    res += 1
            if j >= 3:
                if lines[i][j] == 'X' and lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
                    res += 1
    return res

def check_kernel(arr):
    if len(arr) != 3 or len(arr[0]) != 3:
        return False
    if arr[1][1] != 'A':
        return False
    if not (arr[0][0] == 'M' and arr[2][2] == 'S') and not (arr[0][0] == 'S' and arr[2][2] == 'M'):
        return False
    if not (arr[0][2] == 'M' and arr[2][0] == 'S') and not (arr[0][2] == 'S' and arr[2][0] == 'M'):
        return False
    return True

def count_x_mas2(lines):
    n = len(lines)
    m = len(lines[0])

    res = 0
    for i in range(n - 2):
        for j in range(m - 2):
            kernel = [
                [lines[i][j], lines[i][j+1], lines[i][j+2]],
                [lines[i+1][j], lines[i+1][j+1], lines[i+1][j+2]],
                [lines[i+2][j], lines[i+2][j+1], lines[i+2][j+2]]
            ]
            if check_kernel(kernel):
                res += 1
    return res

def main():
    lines = parse()
    res = count_xmas(lines)
    print(f"Part 1: {res}")
    res = count_x_mas2(lines)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()