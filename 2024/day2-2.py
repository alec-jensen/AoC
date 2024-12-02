with open("2024/day2.txt") as f:
    data = f.read().strip().splitlines()

num_safe = 0

def check_safe(line):
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

    return safe

for line in data:
    line = [int(i) for i in line.split()]

    safe = check_safe(line)

    if not safe:
        for i in range(len(line)):
            temp = line.copy()
            temp.pop(i)
            safe = check_safe(temp)

            if safe:
                break

    num_safe += 1 if safe else 0

print(num_safe)