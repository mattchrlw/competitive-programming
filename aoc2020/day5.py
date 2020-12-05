f = open("day4.txt", "r")
data = [i for i in f.readlines()]
maximum = 0
ids = []

for i in data:
    ids.append(int(i.replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1"), 2))

print(max(ids))

highest = 128 * 8 + 8

for i in range(highest):
    if i not in ids and i-1 in ids and i+1 in ids:
        print(i)

# def part1():
#     f = open("day4.txt", "r")
#     data = [i for i in f.readlines()]
#     maximum = 0
#     ids = []

#     for i in data:
#         first7, last3 = i[:7], i[-3:]
#         ran = [0, 127]
#         iteration = 1
#         for j in first7:
#             iteration *= 2
#             if j == "F":
#                 ran = [ran[0], ran[1] - 128 //iteration]
#             else:
#                 ran = [ran[0] + 128//iteration, ran[1]]
#         row = ran[0]
#         ran = [0, 7]
#         iteration = 1
#         for j in last3:
#             iteration *= 2
#             if j == "L":
#                 ran = [ran[0], ran[1] - 8//iteration]
#             else:
#                 ran = [ran[0] + 8//iteration, ran[1]]
#         col = ran[0]
#         print(row, col, row * 8 + col, sep="\t")
#         maximum = max(maximum, row * 8 + col)
#     return maximum