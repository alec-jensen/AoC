with open("./day4.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total_points = 0

for line in lines:
    line = line.split(":")[1].strip()
    winning_numbers = [num for num in line.split("|")[0].strip().split(" ") if num != ""]
    numbers = [num for num in line.split("|")[1].strip().split(" ") if num != ""]
    points = 0

    for num in numbers:
        if num in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

    total_points += points

print(total_points)
