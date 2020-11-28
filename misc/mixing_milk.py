fin = open("mixmilk.in", "r")
fout = open("mixmilk.out","w")

buckets = [0, 0, 0]
capacities = [0, 0, 0]
inputlines = fin.readlines()
for idx, i in enumerate(inputlines):
    capacities[idx], buckets[idx] = [int(i) for i in i.split()]
output = ""

for i in range(100):
    pour_source = i % 3
    pour = min(buckets[pour_source], capacities[(pour_source + 1) % 3] - buckets[(pour_source + 1) % 3])
    buckets[pour_source] -= pour
    buckets[(pour_source + 1) % 3] += pour

fin.close()
fout.write("\n".join([str(i) for i in buckets]))
fout.close()