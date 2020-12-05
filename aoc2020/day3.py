f = open("day3.txt", "r")
data = f.read().split("\n")

def traverse(r, d):
    h = len(data)
    w = len(data[0])
    count = 0
    x, y = 0, 0

    while True:
        x = (x + r) % w
        y = y + d
        if y > h - 1:
            break
        if data[y][x] == "#":
            count += 1
    return count

total = 0
for i, j in [(1, 1), (3,1 ), (5, 1), (7, 1), (1, 2)]:
    if total == 0:
        total = traverse(i, j)
    else:
        total *= traverse(i, j)
    print(traverse(i, j))

print(total)