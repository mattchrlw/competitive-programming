import time

f = open("day9.txt", "r")
data = [int(i) for i in f.readlines()]
preamble = 25

for i in range(preamble, len(data)):
    sumnum = data[i-preamble:i]
    solved = False
    for j in sumnum:
        for k in sumnum:
            if j + k == data[i] and j != k:
                solved = True
                break
    if solved == False:
        print(data[i])

start = time.time()
total = 36845998
for length in range(2, len(data)):
    for i in range(len(data) - length):
        if sum(data[i:i+length]) == total:
            print(min(data[i:i+length]) + max(data[i:i+length]))
            break

end = time.time()
print(end - start)