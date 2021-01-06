from collections import defaultdict

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            if '"' in neighbour:
                print(neighbour)
            if '|' in neighbour:
                print(neighbour)
            dfs(visited, graph, neighbour)

f = open("day19.txt", "r")
data = f.read()
match = defaultdict()
rules, texts = data.split("\n\n")
rules = rules.split("\n")
texts = texts.split("\n")

for i in rules:
    idx, rule = i.split(": ")
    match[idx] = rule.split(" ")

for i in rules:
    for j in match[idx]:
        visited = set()
        dfs(visited, match, j)

print(match)