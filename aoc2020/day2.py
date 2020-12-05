f = open("day2.txt", "r")
data = [j for j in f.readlines()]
valid = 0

## Part 1
for i in data:
    ran, letter, password = i.split(" ")
    minn, maxx = [int(i) for i in ran.split("-")]
    letter = letter[0]
    count = 0
    for j in password:
        if letter == j:
            count += 1
    if count >= minn and count <= maxx:
        valid += 1

print(valid)
valid = 0

## Part 2
for i in data:
    ran, letter, password = i.split(" ")
    minn, maxx = [int(i) for i in ran.split("-")]
    count = 0
    letter = letter[0]
    if password[minn - 1] == letter:
        count += 1
    if password[maxx - 1] == letter:
        count += 1
    if count == 1:
        valid += 1

print(valid)