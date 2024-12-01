from collections import Counter

def parse():
    col1 = []
    col2 = []
    with open("day01.in") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split()
            col1.append(int(data[0]))
            col2.append(int(data[1]))
    return col1, col2

def main():
    c1, c2 = parse()
    c1.sort()
    c2.sort()
    res = 0
    for i in range(len(c1)):
        res += abs(c1[i] - c2[i])
    print(f"Part 1: {res}")

    count = Counter(c2)

    res = 0
    for n in c1:
        res += count[n] * n
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()