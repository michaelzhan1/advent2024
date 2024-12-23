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

def bors_kerbosch(R, P, X, graph, res):
    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            res.append(sorted(R))
        return
    
    d, pivot = max([(len(graph[v]), v) for v in P.union(X)])

    for v in P.difference(graph[pivot]):
        bors_kerbosch(R.union(set([v])), P.intersection(graph[v]), X.intersection(graph[v]), graph, res)
        P.remove(v)
        X.add(v)


def find_largest_clique(graph):
    res = []
    bors_kerbosch(set(), set(graph.keys()), set(), graph, res)

    largest = sorted(res, key=len, reverse=True)[0]
    return ','.join(largest)

    
def main():
    graph = parse()
    res = count_t_groups(graph)
    print(f'Part 1: {res}')

    res = find_largest_clique(graph)
    print(f'Part 2: {res}')


if __name__ == "__main__":
    main()