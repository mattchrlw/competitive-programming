from pprint import pprint

f = open("day7.txt", "r")
data = [i for i in f.readlines()]

def part1():
    dic = {}
    total = 0

    for i in data:
        bag, others = i.replace("\n", "").replace(".", "").replace(" bags", "").replace(" bag", "").split(" contain ")
        others = [" ".join(i.split(" ")[1:]) for i in others.split(", ")]
        if others == ["other"]:
            dic[bag] = []
        else:
            dic[bag] = others
        print(bag, others)

    def dfs(visited, graph, node):
        if node not in visited:
            if node == 'shiny gold':
                global total
                total += 1
                # print(total)
            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited, graph, neighbour)

    for i in dic.keys():
        visited = set() # Set to keep track of visited nodes.
        print(i, dic[i])
        dfs(visited, dic, i)

    return total - 1

def part2():
    dic = {}
    total = 0

    for i in data:
        bag, o = i.replace("\n", "").replace(".", "").replace(" bags", "").replace(" bag", "").split(" contain ")
        others = [(int(i.split(" ")[0] if i.split(" ")[0].isnumeric() else '0'), " ".join(i.split(" ")[1:])) for i in o.split(", ")]
        if others == [(0, "other")]:
            dic[bag] = []
        else:
            dic[bag] = others

    def bfs(visited, graph, node):
        global total
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s) 

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour[1])
                    for i in range(neighbour[0]):
                        queue.append(neighbour[1])
                        total += 1

    visited, queue = [], []
    bfs(visited, dic, "shiny gold")

    return total

print(part1(), part2())