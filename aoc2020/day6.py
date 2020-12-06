f = open("day6.txt", "r")
data = [i for i in f.read().split("\n\n")]
counts = 0
everyone = 0

for i in data:
    letters = set()
    for j in i:
        if j == "\n":
            continue
        letters.add(j)
    counts += len(letters)

for i in data:
    j = i.split("\n")
    curr = j[0]
    for k in j:
        curr = set(curr).intersection(k)
    everyone += len(curr)

print(counts, everyone)