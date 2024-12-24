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


def main():
    preset, instr = parse()
    res = find_z_output(preset, instr)
    print(f'Part 1: {res}')


if __name__ == "__main__":
    main()