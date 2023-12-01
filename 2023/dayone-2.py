with open("dayone.txt", "r") as f:
    lines = f.readlines()

replace = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0

for line in lines:
    line = line.strip()

    br = False
    for i in range(len(line)):
        if line[i].isnumeric(): break
        for key in replace.keys():
            if line[i:].startswith(key):
                line = line[:i] + replace[key] + line[i+len(key):]
                br = True
                break
        if br: break

    br = False
    for i in range(len(line))[::-1]:
        if line[i].isnumeric(): break
        for key in replace.keys():
            if line[:i+1].endswith(key):
                line = line[:i+1-len(key)] + replace[key] + line[i+1:]
                br = True
                break
        if br: break

    num = ""
    for char in line:
        if char.isnumeric():
            num += char
            break

    for char in line[::-1]:
        if char.isnumeric():
            num += char
            break

    if num != "":
        total += int(num)

print(total)    