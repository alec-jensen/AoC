with open("./day3.txt", "r") as f:
    data = [line.strip() + "." for line in f.readlines()]

gear_ratios = []

data_modified = [list(line) for line in data]

# This approach collates the numbers, and adds a prefix so that we know each number is unique
prefix = 0

for i, line in enumerate(data):
    j = 0

    while j < len(line):
        if line[j].isnumeric():
            start = j
            end = None

            for _, char in enumerate(line[j:]):
                if not char.isnumeric():
                    end = j + _
                    break

            if end is None:
                j += 1
                continue

            j += end - start

            for x in range(start, end):
                data_modified[i][x] = f"{prefix}_{line[start:end]}"

        else:
            j += 1

        prefix += 1

print(data_modified)

# Now, for each *, find collated numbers next to it. Using the prefixes, we can filter duplicates
for i, line in enumerate(data_modified):
    for j, char in enumerate(line):
        if char == "*":
            nums = []

            for x in range(-1, 2):
                for y in range(-1, 2):
                    if i + y > len(data_modified) - 1:
                        continue

                    if j + x > len(data_modified[i + y]) - 1:
                        continue

                    if i + y < 0:
                        continue

                    if j + x < 0:
                        continue

                    if not data_modified[i + y][j + x] in nums:
                        nums.append(data_modified[i + y][j + x])

                    print(f"{data_modified[i + y][j + x]} ({i + y}, {j + x})")

            nums = [num.split("_")[1] for num in nums if len(num.split("_")) > 1]

            print(nums)

            if len(nums) == 2:
                gear_ratios.append(nums)

print(gear_ratios)

sum = 0
for gear in gear_ratios:
    t = 1
    for n in gear:
        t *= int(n)

    sum += t

print(sum)