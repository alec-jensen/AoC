with open("./day5.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [int(i) for i in lines[0].split(": ")[1].strip().split(" ")]

maps: dict[str, list[tuple[int, int, int]]] = {
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

mappings = {seed: [seed] for seed in seeds}

for seed in seeds:
    stop = False

    print(f"Seed {seed}:")
    for map in maps:
        mapped = False
        for smap in maps[map]:
            if smap[1] <= mappings[seed][-1] <= smap[1] + smap[2]:
                mappings[seed].append(mappings[seed][-1] + smap[0] - smap[1])
                print(f"{mappings[seed][-2]} -> {mappings[seed][-1]} {smap}")
                mapped = True
                break

        if not mapped:
            print(f"{mappings[seed][-1]} -> {mappings[seed][-1]}")
            mappings[seed].append(mappings[seed][-1])

print(mappings)

lowest = min([mappings[seed][-1] for seed in mappings])

print(f"Lowest: {lowest}")