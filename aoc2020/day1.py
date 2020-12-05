f = open("day1.txt", "r")
nums = []

for i in [int(j) for j in f.readlines()]:
    nums.append(i)

for i in nums:
    for j in nums:
        if i + j == 2020:
            print(i * j)
            break

for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                print(i * j * k)
                break