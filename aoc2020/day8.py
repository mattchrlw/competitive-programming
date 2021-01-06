f = open("day8.txt", "r")
data = [i for i in f.readlines()]

def part1():
    index = 0
    value = 0
    seen = []

    while index < len(data):
        op, arg = data[index].split(" ")
        arg = int(arg.replace("\n", ""))
        if index in seen:
            break
        seen.append(index)
        # print(index, seen)
        
        if op == "acc":
            value += int(arg)
            index += 1
        elif op == "jmp":
            index += int(arg)
        else:
            index += 1
    print(value)

def part2():
    for iteration in range(len(data)):
        index = 0
        value = 0
        seen = []
        instr = deepcopy(data)
        instr[iteration] = instr[iteration].replace("nop", "jmp")
        inf = False

        while index < len(data):
            op, arg = instr[index].split(" ")
            arg = int(arg.replace("\n", ""))
            if index in seen:
                # print("NOPE", end=" ")
                inf = True
                break
            seen.append(index)
            if op == "acc":
                value += int(arg)
                index += 1
            elif op == "jmp":
                index += int(arg)
            else:
                index += 1
        if not inf:
            print(value, " ")
        # print(instr)

    for iteration in range(len(data)):
        index = 0
        value = 0
        seen = []
        instr = deepcopy(data)
        instr[iteration] = instr[iteration].replace("jmp", "nop")
        inf = False

        while index < len(data):
            op, arg = instr[index].split(" ")
            arg = int(arg.replace("\n", ""))
            if index in seen:
                inf = True
                break
            seen.append(index)
            if op == "acc":
                value += int(arg)
                index += 1
            elif op == "jmp":
                index += int(arg)
            else:
                index += 1
        if not inf:
            print(value, " ")
        # print(instr)