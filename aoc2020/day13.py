from sympy.ntheory.modular import crt

f = open("day13.txt", "r")
data = f.readlines()
timestamp = int(data[0])
ids = [int(i) for i in data[1].split(",") if i != 'x']

def part1():
    buses = []
    for i in ids:
        num = 0
        while num < timestamp + 100:
            num += i
            buses.append([num, i])
    bus = sorted([i for i in buses if i[0] > timestamp], key=lambda i: i[0])[0]
    return (bus[0] - timestamp) * bus[1]

def part2():
    ids_2 = [int(i) if i.isnumeric() else i for i in data[1].split(",")]
    ts = [-idx for idx, i in enumerate(ids_2) if i != 'x']
    print(ids, ts)
    # ids are moduli (the ms)
    # ts are residuals (the as)
    # negate residuals because for example in 7,13,x,x,59,x,31,19
    # you want 13 to be 1 *ahead*, 59 to be 4 ahead etc.
    # so you need them to be = -1 % ids[1], -4 % ids[2] etc.
    return crt(ids, ts)[0]

print(part1(), part2())