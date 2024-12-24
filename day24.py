from collections import defaultdict, deque
import heapq

def parse():
    with open('day24.in') as f:
        data = f.read()

        preset, instr = data.split('\n\n')
        preset = preset.split('\n')
        for i in range(len(preset)):
            preset[i] = preset[i].split(': ')
            preset[i][1] = int(preset[i][1])
        
        instr = instr.split('\n')
        for i in range(len(instr)):
            a, op, b, _, c = instr[i].split()
            instr[i] = (a, op, b, c)
        
        return preset, instr
    
def topo_sort(preset, instr):
    """Sort the instructions topologically so that we can execute. a and b must exist for c to be evaluated."""
    graph = defaultdict(list)
    degrees = defaultdict(int)
    idx = {}

    for i, (a, _, b, c) in enumerate(instr):
        graph[a].append(c)
        graph[b].append(c)
        degrees[c] += 2
        idx[c] = i
    
    queue = deque([node for node, _ in preset])
    order = []
    while queue:
        cur = queue.popleft()
        for neigh in graph[cur]:
            degrees[neigh] -= 1
            if degrees[neigh] == 0:
                queue.append(neigh)
        if cur in idx:
            order.append(idx[cur])
    
    return [instr[i] for i in order]
    
def find_z_output(preset, instr):
    instr = topo_sort(preset, instr)

    vals = {}
    for name, val in preset:
        vals[name] = val
    
    for a, op, b, c in instr:
        match op:
            case 'AND':
                vals[c] = vals[a] & vals[b]
            case 'OR':
                vals[c] = vals[a] | vals[b]
            case 'XOR':
                vals[c] = vals[a] ^ vals[b]
            case _:
                print('Invalid operation')
    
    z_vals = []
    for name in vals:
        if name[0] == 'z':
            z_vals.append((name, vals[name]))
    z_vals.sort(reverse=True)
    output_bin = ''.join(map(str, [val for _, val in z_vals]))
    return int(output_bin, 2)

def find_wrong_adders(instr):
    op2wire = {}
    wire2op = {}

    for a, op, b, c in instr:
        op2wire[(a, op, b)] = c
        op2wire[(b, op, a)] = c
        wire2op[c] = (a, op, b)

    def swap_wires(out1, out2):
        wire1 = wire2op[out1]
        wire2 = wire2op[out2]

        wire1_alt = wire1[::-1]
        wire2_alt = wire2[::-1]

        wire2op[out1], wire2op[out2] = wire2, wire1
        op2wire[wire1], op2wire[wire2] = out2, out1
        op2wire[wire1_alt], op2wire[wire2_alt] = out2, out1

    swaps = []
    bit = 0
    cur_carry = None

    while True:
        x = f'x{bit:02d}'
        y = f'y{bit:02d}'
        z = f'z{bit:02d}'

        and_key = (x, 'AND', y)
        xor_key = (x, 'XOR', y)

        if bit == 0:
            carry = op2wire[and_key]
        else:
            xor_wire = op2wire[xor_key]
            and_wire = op2wire[and_key]

            carry_xor_key = (xor_wire, 'XOR', carry)
            if carry_xor_key not in op2wire:
                swaps.append(xor_wire)
                swaps.append(and_wire)
                swap_wires(xor_wire, and_wire)
                bit = 0
                continue

            carry_xor_wire = op2wire[carry_xor_key]
            if carry_xor_wire != z:
                swaps.append(carry_xor_wire)
                swaps.append(z)
                swap_wires(carry_xor_wire, z)
                bit = 0
                continue
            
            carry_and_wire = op2wire[(xor_wire, 'AND', carry)]
            carry = op2wire[(and_wire, 'OR', carry_and_wire)]
        bit += 1
        if bit >= 45:
            break
    return ','.join(sorted(swaps))

        

def main():
    preset, instr = parse()
    res = find_z_output(preset, instr)
    print(f'Part 1: {res}')

    res = find_wrong_adders(instr)
    print(f'Part 2: {res}')


if __name__ == "__main__":
    main()