f = open("day12.txt", "r")
data = [i.strip("\n") for i in f.readlines()]

dirr = 0
pos = [0, 0]
for i in data:
    dir, val = i[0], int(i[1:])
    if dir == "N":
        pos[1] -= val
    if dir == "S":
        pos[1] += val
    if dir == "E":
        pos[0] += val
    if dir == "W":
        pos[0] -= val
    if dir == "L":
        dirr = (dirr + val) % 360
    if dir == "R":
        dirr = (dirr - val) % 360
    if dir == "F":
        if dirr == 90:
            pos[1] -= val
        if dirr == 180:
            pos[0] -= val
        if dirr == 270:
            pos[1] += val
        if dirr == 0:
            pos[0] += val

print(pos, abs(pos[0]) + abs(pos[1]))

pos = [0, 0]
wp = [10, -1]

for i in data:
    dir, val = i[0], int(i[1:])
    if dir == "N":
        wp[1] -= val
    if dir == "S":
        wp[1] += val
    if dir == "E":
        wp[0] += val
    if dir == "W":
        wp[0] -= val
    if dir == "L":
        if val == 90:
            wp[0], wp[1] = wp[1], -wp[0]
        if val == 180:
            wp[0], wp[1] = -wp[0], -wp[1]
        if val == 270:
            wp[0], wp[1] = -wp[1], wp[0]
    if dir == "R":
        if val == 90:
            wp[0], wp[1] = -wp[1], wp[0]
        if val == 180:
            wp[0], wp[1] = -wp[0], -wp[1]
        if val == 270:
            wp[0], wp[1] = wp[1], -wp[0]
    if dir == "F":
        pos[0] += val * wp[0]
        pos[1] += val * wp[1]

print(pos, abs(pos[0]) + abs(pos[1]))