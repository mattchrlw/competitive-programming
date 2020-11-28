import sys

def bruh():
    sys.stdin = open("lostcow.in", "r")
    sys.stdout = open("lostcow.out","w")

    dist = 1
    x, y = [int(i) for i in input().split()]
    pos = x
    travelled = 0
    delta = 1
    
    while True:
        for _ in range(dist):
            pos += delta
            travelled += 1
            if pos == y:
                return travelled
        for _ in range(dist):
            pos -= delta
            travelled += 1
            if pos == y:
                return travelled
        delta *= -1
        dist *= 2

print(bruh())