with open("day1.txt", "r") as f:
    lines = f.readlines()

nums = []

for line in lines:
    num = ""
    for char in line:
        if char.isnumeric():
            num += char
            break

    for char in line[::-1]:
        if char.isnumeric():
            num += char
            break

    if num != "":
        nums.append(int(num))

total = 0
for i in nums:
    total += i

print(total)    