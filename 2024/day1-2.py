with open("2024/day1.txt") as f:
    data = f.read().strip().splitlines()

left_list = []
right_list = []

for line in data:
    left_list.append(int(line.split()[0]))
    right_list.append(int(line.split()[1]))

score = 0

for i in left_list:
    score += i * right_list.count(i)

print(score)