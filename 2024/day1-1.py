with open("2024/day1.txt") as f:
    data = f.read().strip().splitlines()

left_list = []
right_list = []

for line in data:
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[1]))

left_list.sort()
right_list.sort()

total = 0

for i in range(len(left_list)):
    diff = abs(left_list[i] - right_list[i])
    total += diff

print(total)