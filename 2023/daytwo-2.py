import re

with open("daytwo.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total = 0

for line in lines:
    game_is_valid = True

    game_header, line = line.split(": ")
    game_number = int(game_header[5:])

    cubes = re.split(r"; |, ", line)

    num_of_cubes = {
        "red": [],
        "green": [],
        "blue": []
    }
    
    for cube in cubes:
        num, cube = cube.split(" ")
        
        num_of_cubes[cube].append(int(num))

    num_of_cubes["red"].sort()
    num_of_cubes["green"].sort()
    num_of_cubes["blue"].sort()

    total += num_of_cubes["red"][-1] * num_of_cubes["green"][-1] * num_of_cubes["blue"][-1]
    
print(total)
