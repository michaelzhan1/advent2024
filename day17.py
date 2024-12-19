from functools import cache

def parse():
    with open('day17.in') as f:
        a = int(f.readline().strip().split()[-1])
        b = int(f.readline().strip().split()[-1])
        c = int(f.readline().strip().split()[-1])

        f.readline()
        operations = list(map(int, (f.readline().split()[-1].split(','))))
        return a, b, c, operations
    
def get_combo(operand, a, b, c):
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    if operand == 7:
        raise ValueError("Invalid operand")


def evaluate(a, b, c, ops):
    # literal: same number

    # combo map:
    # 0, 1, 2, 3: 0, 1, 2, 3 (literals)
    # 4: register A
    # 5: register B
    # 6: register C
    # 7: never

    # op map:
    # 0: reg A // 2 ** combo -> reg A
    # 1: B ^ literal -> B
    # 2: combo % 8 -> B
    # 3: jump to literal if A != 0 else nothing
    # 4: B ^ C -> B (ignore operand)
    # 5: print(combo % 8), csv if multiple prints
    # 6: reg A // 2 ** combo -> reg B
    # 7: reg A // 2 ** combo -> reg C

    res = []

    i = 0
    while i < len(ops):
        operator, operand = ops[i], ops[i + 1]
        match operator:
            case 0:
                a >>= get_combo(operand, a, b, c)
            case 1:
                b ^= operand
            case 2:
                b = get_combo(operand, a, b, c) & 7
            case 3:
                if a != 0:
                    i = operand
                    continue
            case 4:
                b ^= c
            case 5:
                res.append(get_combo(operand, a, b, c) & 7)
            case 6:
                b = a >> get_combo(operand, a, b, c)
            case 7:
                c = a >> get_combo(operand, a, b, c)
        i += 2

    return res

def try_a_registers(a, b, c, ops):
    def find(a, i):
        output = evaluate(a, b, c, ops)
        if output == ops:
            return a
        
        elif output == ops[-i:] or not i:
            # build most significant bits first
            for n in range(8):
                temp = find(8 * a + n, i + 1)
                if temp is not None:
                    return temp
        
        return None

    return find(0, 0)


def main():
    a, b, c, ops = parse()
    res = evaluate(a, b, c, ops)
    print(f"Part 1: {','.join(map(str, res))}")

    res = try_a_registers(a, b, c, ops)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()