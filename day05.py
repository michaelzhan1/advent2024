from collections import defaultdict, deque

def parse():
    with open('day05.in', 'r') as f:
        all_lines = f.read()
        all_rules, all_pages = all_lines.split('\n\n')
        rules = all_rules.splitlines()
        pages = all_pages.splitlines()

        rules = [list(map(int, rule.split('|'))) for rule in rules]
        pages = [list(map(int, page.split(','))) for page in pages]
        return rules, pages
        
def check_page(page, rule_graph):
    for i in range(len(page) - 1):
        for j in range(i + 1, len(page)):
            if page[i] in rule_graph[page[j]]:
                return False
    return True

def get_valid_page_middles(rules, pages):
    rule_graph = defaultdict(set)
    for a, b in rules:
        rule_graph[a].add(b)
    
    res = 0
    for page in pages:
        if check_page(page, rule_graph):
            res += page[len(page) // 2]
    return res

def fix_page(page, rule_graph):
    used_vals = set(page)

    small_graph = defaultdict(set)
    for a in rule_graph:
        if a in used_vals:
            for b in rule_graph[a]:
                if b in used_vals:
                    small_graph[a].add(b)

    in_deg = {}
    for val in used_vals:
        in_deg[val] = 0
    for a in small_graph:
        for b in small_graph[a]:
            in_deg[b] += 1
    
    queue = deque()
    seen = set()
    for val in used_vals:
        if in_deg[val] == 0:
            queue.append(val)
            seen.add(val)

    res = []
    while queue:
        cur = queue.popleft()
        res.append(cur)
        for next_val in small_graph[cur]:
            in_deg[next_val] -= 1
            if in_deg[next_val] == 0:
                queue.append(next_val)
                seen.add(next_val)
    return res
        

def fix_invalid_page_middles(rules, pages):
    rule_graph = defaultdict(set)
    for a, b in rules:
        rule_graph[a].add(b)
    
    pages = [page for page in pages if not check_page(page, rule_graph)]
    res = 0
    for page in pages:
        new_page = fix_page(page, rule_graph)
        res += new_page[len(new_page) // 2]
    return res


def main():
    rules, pages = parse()
    res = get_valid_page_middles(rules, pages)
    print(f"Part 1: {res}")

    res = fix_invalid_page_middles(rules, pages)
    print(f"Part 2: {res}")


if __name__ == "__main__":
    main()