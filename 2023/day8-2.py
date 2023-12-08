with open("./day8.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

instructions = lines.pop(0)

dests = {}

starts = []
ends = []

for line in lines:
    dest = line.split(" = ")[0]
    gotos = line.split(" = ")[1]
    gotos = gotos.removeprefix("(").removesuffix(")").split(", ")

    dests[dest] = gotos

    if dest.endswith("A"):
        starts.append(dest)

    if dest.endswith("Z"):
        ends.append(dest)

# wip