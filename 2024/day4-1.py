with open("2024/day4.txt") as f:
    data = f.read().strip().splitlines()

def search(x, y, dx, dy) -> list[tuple[int, int]] | None:
    word = "XMAS"
    for i, letter in enumerate(word):
        if x + i * dx < 0 or y + i * dy < 0:
            return None
        if x + i * dx >= len(data) or y + i * dy >= len(data[0]):
            return None
        if data[x + i * dx][y + i * dy] != letter:
            return None
    return [(x + i * dx, y + i * dy) for i in range(len(word))]

found: list[tuple[int, int]] = []
total = 0

for x, line in enumerate(data):
    for y, letter in enumerate(line):
        if (x, y) in found:
            continue

        if letter == "X":
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    results = search(x, y, dx, dy)
                    if results:
                        found.extend(results)
                        total += 1

print(total)

for x, line in enumerate(data):
    for y, letter in enumerate(line):
        if (x, y) in found:
            print(letter, end="")
        else:
            print(".", end="")
    print()