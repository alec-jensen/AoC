# this code sucks and probably doesnt work but i dont care
# cope harder
# (untested)

with open("./day5.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [int(i) for i in lines[0].split(": ")[1].strip().split(" ")]

# group seeds by 2

seeds = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]

print(seeds)

maps: dict[str, set[tuple[int, int, int]]] = {
    "seed-to-soil map:": [],
    "soil-to-fertilizer map:": [],
    "fertilizer-to-water map:": [],
    "water-to-light map:": [],
    "light-to-temperature map:": [],
    "temperature-to-humidity map:": [],
    "humidity-to-location map:": [],
}

# im sorry for anyone who has to read this

lines = lines[2:]

for i, key in enumerate(maps.keys()):
    start = lines.index(key)
    try:
        end = lines.index("")
    except ValueError:
        end = len(lines)

    maps[key] = [
        tuple([int(j) for j in line.split(" ")])
        for line in lines[start + 1 : end]
    ]

    lines = lines[end + 1 :]

print(maps)

lowest = float("inf")

for seed1 in seeds:
    for seed in range(seed1[0], seed1[0] + seed1[1] + 1):
        mapping = [seed]

        stop = False

        for map in maps:
            for smap in maps[map]:
                if smap[1] <= mapping[-1] <= smap[1] + smap[2]:
                    mapping.append(mapping[-1] + smap[0] - smap[1])
                    break

            else:
                mapping.append(mapping[-1])

        if mapping[-1] < lowest:
            lowest = mapping[-1]

print(f"Lowest: {lowest}")