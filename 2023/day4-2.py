with open("./day4.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total_points = 0

# yeah so this was fun
# card #: (winning numbers, numbers, instances)
cards = {int(line.split(":")[0].strip()[5:]): ([num for num in line.split(":")[1].strip().split("|")[0].strip().split(" ") if num != ""], [num for num in line.split(":")[1].strip().split("|")[1].strip().split(" ") if num != ""]) for line in lines}
cards = {card: ([int(num) for num in cards[card][0]], [int(num) for num in cards[card][1]], 1) for card in cards}

i = 1
while True:
    for j in range(i, i + cards[i][2]):
        num_winning = 0

        winning_numbers = cards[i][0]
        numbers = cards[i][1]

        for num in numbers:
            if num in winning_numbers:
                num_winning += 1

        for k in range(i + 1, i + num_winning + 1):
            cards[k] = (cards[k][0], cards[k][1], cards[k][2] + 1)

    i += 1

    if not i < len(cards):
        break

total = 0
for card in cards:
    total += cards[card][2]

print(total)
