with open("./daythree.txt", "r") as f:
    data = [line.strip() + "." for line in f.readlines()]

symbols = []

for line in data:
    for char in line:
        if not char.isnumeric() and char != ".":
            if not char in symbols:
                symbols.append(char)

part_numbers = []

for i, line in enumerate(data):
    j = 0

    while j < len(line):
        if line[j].isnumeric():
            start = j
            end = None

            print(f"{line[j]} @ ({i}, {j})")
            print(f"start: {start}")
            for _, char in enumerate(line[j:]):
                if not char.isnumeric():
                    end = j + _
                    break
            print(f"end: {end}")

            if end is None:
                j += 1
                continue

            # Check if number is touching a symbol

            curr_index = start
            stop = False

            print(f"Checking {line[start:end]}")

            while curr_index < end:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        # Check if out of bounds

                        if i + y > len(data) - 1:
                            continue

                        if curr_index + x > len(data[i + y]):
                            continue

                        if curr_index + x < 0:
                            continue

                        if i + y < 0:
                            continue

                        #print(f"Checking {data[i + y][curr_index + x]} at ({i+y}, {curr_index+x}) for {line[start:end]}")
                        if data[i + y][curr_index + x] in symbols:
                            print(f"Found symbol {data[i + y][curr_index + x]} at {curr_index + x}, {i + y} for {line[start:end]}")
                            part_numbers.append(line[start:end])
                            stop = True
                            break

                    if stop:
                        break

                curr_index += 1

                if stop:
                    break

            j += end - start

        else:
            j += 1

print(part_numbers)

sum = 0

for num in part_numbers:
    sum += int(num)

print(sum)