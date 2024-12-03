import re

def parse():
    with open("day03.in", "r") as file:
        lines = file.readlines()
    return lines


def eval_mul(s):
    s = s[4:-1]
    a, b = s.split(",")
    return int(a) * int(b)

def find_muls(lines):
    res = 0
    for line in lines:
        matches = re.findall("mul\(\d+,\d+\)", line)
        for match in matches:
            res += eval_mul(match)
    return res

def find_muls2(lines):
    res = 0
    toggle = True
    for line in lines:
        matches = re.findall("(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
        for match in matches:
            if match == "do()":
                toggle = True
            elif match == "don't()":
                toggle = False
            elif toggle:
                res += eval_mul(match)
    return res



def main():
    lines = parse()
    res = find_muls(lines)
    print(f"Part 1: {res}")
    
    res = find_muls2(lines)
    print(f"Part 2: {res}")

if __name__ == "__main__":
    main()