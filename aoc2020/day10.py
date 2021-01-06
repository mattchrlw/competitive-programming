f = open("day10.txt", "r")
data = [int(i) for i in f.readlines()]

data = sorted(data)
data.insert(0, 0)
# print(data)

onej = 0
threej = 0

for i in range(len(data)-1):
    if data[i+1] - data[i] == 3:
        threej += 1
    else:
        onej += 1
threej += 1

# print(onej, threej, threej * onej)
curr = data[0]
# data.remove(0)
vals = [0] * len(data)
vals[0] = 1
idx = 0
while idx < len(data):
    for i in [1, 2, 3]:
        if idx+i < len(data) and data[idx+i] <= data[idx] + 3:
            vals[idx+i] += vals[idx]
    idx += 1

print(vals[len(data)-1])