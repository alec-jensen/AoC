with open("2024/day2.txt") as f:
    data = f.read().strip().splitlines()

num_safe = 0

for line in data:
    line = [int(i) for i in line.split()]

    decreasing = line[0] > line[1]
    safe = True

    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            safe = False
            break

        if decreasing:
            if line[i] < line[i + 1]:
                safe = False
                break
        else:
            if line[i] > line[i + 1]:
                safe = False
                break

        if abs(line[i] - line[i + 1]) < 1 or abs(line[i] - line[i + 1]) > 3:
            safe = False
            break

    if safe:
        num_safe += 1

print(num_safe)