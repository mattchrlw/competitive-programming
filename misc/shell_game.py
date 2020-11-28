import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out","w")

num_swaps = int(input())
scores = [0, 0, 0]
shells = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

for i in range(num_swaps):
    a, b, g = [int(i) for i in input().split()]
    for j in range(3):
        temp = shells[j][a-1]
        shells[j][a-1] = shells[j][b-1]
        shells[j][b-1] = temp
        if shells[j][g-1] == 1:
            scores[j] += 1

print(max(scores))
