from collections import defaultdict

def parse():
    with open('day23.in') as f:
        lines = f.read().splitlines()
        graph = defaultdict(set)
        for line in lines:
            a, b = line.split('-')
            graph[a].add(b)
            graph[b].add(a)
    
        return graph
    
def count_t_groups(graph):
    seen = set()
    res = 0
    for node, neighs in graph.items():
        neighs = list(neighs)
        for i in range(len(neighs)):
            for j in range(i + 1, len(neighs)):
                if neighs[i] in graph[neighs[j]]:
                    key = tuple(sorted([node, neighs[i], neighs[j]]))
                    if key not in seen:
                        seen.add(key)
                        if node[0] == 't' or neighs[i][0] == 't' or neighs[j][0] == 't':
                            res += 1
    return res

    
def main():
    graph = parse()
    res = count_t_groups(graph)
    print(f'Part 1: {res}')


if __name__ == "__main__":
    main()