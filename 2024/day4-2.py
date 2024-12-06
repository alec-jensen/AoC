from typing import Any
import numpy as np

with open("2024/day4.txt") as f:
    data = f.read().strip().splitlines()

kernel = [
    ["M", Any, "M"],
    [Any, "A", Any],
    ["S", Any, "S"]
]

all_rotations = []
for _ in range(4):
    all_rotations.append(kernel)
    kernel = np.rot90(kernel)

total = 0

for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        for rot in all_rotations:
            found = True
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if rot[x + 1][y + 1] != Any and rot[x + 1][y + 1] != data[i + x][j + y]:
                        found = False
                        break
                if not found:
                    break
            if found:
                total += 1
                break

print(total)