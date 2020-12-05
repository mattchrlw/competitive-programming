from math import sqrt

def sieve(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    primes[4::2] = [False] * len(primes[4::2])
    for i in range(3, int(sqrt(n))+1, 2):
        if primes[i]:
            primes[i*i::2*i] = [False] * len(primes[i*i::2*i])
        # j = i*i
        # while j < n:
        #     primes[j] = False
        #     j = j+2*i
    return set([x for x in range(n) if primes[x] == True])

n = int(input())
for i in range(n):
    a, b, kay = [int(i) for i in input().split()]
    primes = sieve(b+1)
    count = 0
    for j in range(a, b+1):
        primacity = 0
        for k in primes:
            if j % k == 0:
                primacity += 1
            # tiny speedup
            if primacity > kay:
                continue
        if primacity == kay:
            count += 1
    print("Case #", i+1, ": ", count, sep="")
