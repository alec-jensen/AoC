import re

with open("day2.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0

for line in lines:
    game_is_valid = True

    game_header, line = line.split(": ")
    game_number = int(game_header[5:])

    cubes = re.split(r"; |, ", line)
    
    for cube in cubes:
        num, cube = cube.split(" ")
        
        if int(num) > limits[cube]:
            game_is_valid = False
            break

    if game_is_valid:
        total += game_number

print(total)
    