f = open("day4.txt", "r")
data = f.read().split("\n\n")
new_data = []
count = 0
for i in data:
    new_lbl = [tuple(j.split(":")) for j in i.replace("\n", " ").split(" ")]
    mapping = dict(new_lbl)
    conditions = 0
    if not all(item in mapping.keys() for item in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        continue
    if int(mapping["byr"]) >= 1920 and int(mapping["byr"]) <= 2002:
        conditions += 1
    if int(mapping["iyr"]) >= 2010 and int(mapping["iyr"]) <= 2020:
        conditions += 1
    if int(mapping["eyr"]) >= 2020 and int(mapping["eyr"]) <= 2030:
        conditions += 1
    if "cm" in mapping["hgt"] and int(mapping["hgt"].split("cm")[0]) >= 150 and int(mapping["hgt"].split("cm")[0]) <= 193:
        conditions += 1
    if "in" in mapping["hgt"] and int(mapping["hgt"].split("in")[0]) >= 59 and int(mapping["hgt"].split("in")[0]) <= 76:
        conditions += 1
    if mapping["hcl"][0] == "#" and all(mapping["hcl"].split("#")[1][i] in "0123456789abcdef" for i in range(6)):
        conditions += 1
    if mapping["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        conditions += 1
    if len(mapping["pid"]) == 9 and mapping["pid"].isnumeric():
        conditions += 1
        
    if conditions == 7:
        count += 1

print(count)