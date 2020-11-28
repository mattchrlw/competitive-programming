n = int(input())

x1, y1 = tuple([int(i) for i in input().split()])
x2, y2 = tuple([int(i) for i in input().split()])

s = [int(input()) for i in range(n)]

m = sum([i//2 for i in s])
l = sum([i % 2 for i in s])

if (m > x1 or m > x2):
    print("No")
    return

if (m + l > y1 or m + l > y2):
    print("No")
    return





print("Yes")
