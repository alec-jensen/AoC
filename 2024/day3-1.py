import re

with open("2024/day3.txt") as f:
    data = f.read().strip().splitlines()

total = 0

for line in data:
    for match in re.finditer(r"mul\([0-9]+,[0-9]+\)", line):
        nums = re.findall(r"[0-9]+", match.group())
        total += int(nums[0]) * int(nums[1])

print(total)