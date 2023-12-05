import sys
from collections import defaultdict


with open("./day5.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [int(i) for i in lines[0].split(": ")[1].strip().split(" ")]

mappings = []

new_mapping = False
mapping = None
for line in lines[1:]:
    if not line:
        new_mapping = True
    elif new_mapping:
        new_mapping = False
        mappings.append([])
    else:
        [dest, source, range] = [int(x) for x in line.split(' ')]
        mappings[-1].append((source, dest, range))

for mapping in mappings:
    mapping.sort()


start = None
ranges = []
for i, seed_number in enumerate(seeds):
    if i % 2 == 0:
        start = seed_number
    else:
        ranges.append((start, start + seed_number - 1))


ranges.sort()

for it, mapping in enumerate(mappings):
    i = 0
    j = 0
    new_ranges = []

    range = None
    while ranges or range:
        if not range:
            range = ranges.pop(0)

        range_start = range[0]
        range_end = range[1]

        if j >= len(mapping):
            new_ranges.append((range_start, range_end))
            range = None
            i += 1
            continue

        mapping_start = mapping[j][0]
        mapping_end = mapping[j][0] + mapping[j][2] - 1

        mapping_shift = mapping[j][1] - mapping[j][0]

        if range_start < mapping_start and range_end < mapping_start:
            new_ranges.append((range_start, range_end))
            range = None
            i += 1
        elif range_start >= mapping_start and range_end <= mapping_end:
            new_ranges.append((range_start + mapping_shift, range_end + mapping_shift))
            range = None
            i += 1
        elif range_start <= mapping_start and range_end <= mapping_end:
            if range_start < mapping_start:
                new_ranges.append((range_start, mapping_start - 1))
            new_ranges.append((mapping_start + mapping_shift, range_end + mapping_shift))
            range = None
            i += 1
        elif range_start <= mapping_start and range_end >= mapping_end:
            if range_start < mapping_start:
                new_ranges.append((range_start, mapping_start - 1))
            new_ranges.append((mapping_start + mapping_shift, mapping_end + mapping_shift))
            if range_end > mapping_end:
                ranges = [(mapping_end + 1, range_end)] + ranges
            range = None
        elif range_start <= mapping_end and range_end > mapping_end:
            new_ranges.append((range_start + mapping_shift, mapping_end + mapping_shift))
            ranges = [(mapping_end + 1, range_end)] + ranges
            range = None
        else:
            j += 1

    ranges = new_ranges
    ranges.sort()

print(min(ranges)[0])