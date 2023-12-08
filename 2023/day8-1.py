with open("./day8.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

instructions = lines.pop(0)

dests = {}

for line in lines:
    dest = line.split(" = ")[0]
    gotos = line.split(" = ")[1]
    gotos = gotos.removeprefix("(").removesuffix(")").split(", ")

    dests[dest] = gotos

curr = "AAA"
length = 0

stop = False
while not stop:
    for ch in instructions:
        if ch == "R":
            curr = dests[curr][1]
        elif ch == "L":
            curr = dests[curr][0]

        length += 1
        if curr == "ZZZ":
            stop = True
            break

print(length)