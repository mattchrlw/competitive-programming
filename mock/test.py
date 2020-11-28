from collections import Counter

a = "rasp"
b = "spar"

al = Counter()
bl = Counter()

al.update(a)
bl.update(b)

print(al, bl)