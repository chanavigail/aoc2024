def is_correct(pages, rules):
    check = True
    for page in pages:
        if not check: break
        elif page not in rules: continue
        else: rule = rules[page]
        for i in range(pages.index(page)):
            if pages[i] in rule: 
                check = False
                break
    return check

def dfs(adj, visited, stack, node):
    visited[node] = 1
    neighbours = adj[node]
    for neighbour in neighbours:
        if visited[neighbour]: continue
        else:
            adj, visited, stack = dfs(adj, visited, stack, neighbour)
    stack.append(node)
    return adj, visited, stack

def part_one(rows):
    parse_rules = True
    rules = {}
    correct = []
    for row in rows:
        row = row.rstrip()
        if row == "": 
            parse_rules = False
        elif parse_rules:
            a, b = row.split("|")
            if a in rules:
                rules[a].append(b)
            else: rules[a] = [b]
        else:
            pages = row.split(",")
            if is_correct(pages, rules): correct.append(pages)
    ans = 0
    for c in correct:
        ans += int(c[len(c) // 2])
    return ans
                
## change to topo sort in the future
def part_two(rows):
    parse_rules = True
    rules = {}
    incorrect = []
    for row in rows:
        row = row.rstrip()
        if row == "": 
            parse_rules = False
            
        elif parse_rules:
            a, b = row.split("|")
            if a in rules:
                rules[a].append(b)
            else: rules[a] = [b]
        else:
            pages = row.split(",")
            check = True
            for page in pages:
                if page not in rules: rules[page] = []
                else: rule = rules[page]
                for i in range(pages.index(page)):
                    if pages[i] in rule: 
                        check = False
                        break
            if not check: incorrect.append(pages)
    ans = 0
    for i in incorrect:
        # i.sort(reverse=True, key=lambda x: len(rules[x]))
        while not is_correct(i, rules):
            for j in range(len(i) - 1):
                if i[j] in rules[i[j + 1]]: i[j], i[j + 1] = i[j + 1], i[j]
                if is_correct(i, rules): break
        ans += int(i[len(i) // 2])

        # visited = [0] * len(i)
        # stack = []
        # for j in range(len(i)):
        #     _, visited, stack = dfs(rules, visited, stack, j)
        # ans += int(stack[len(i) // 2])
        
    return ans