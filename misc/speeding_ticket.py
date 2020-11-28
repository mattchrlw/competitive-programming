fin = open("speeding.in", "r")
fout = open("speeding.out","w")

output = ""

speed = []
limit = []

n, m = [int(i) for i in fin.readline().split()]
for i in range(n):
    l, s = [int(i) for i in fin.readline().split()]
    for _ in range(l):
        limit.append(s)
for i in range(m):
    l, s = [int(i) for i in fin.readline().split()]
    for _ in range(l):
        speed.append(s)

fin.close()
fout.write(str(max(0, max([speed[i] - limit[i] for i in range(len(limit))]))))
fout.close()