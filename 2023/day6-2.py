with open("./day6.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

races: list[tuple[int, int]] = []

times = [i for i in lines[0].removeprefix("Time: ").replace(" ", "").split(" ") if i != ""]
distances = [i for i in lines[1].removeprefix("Distance: ").replace(" ", "").split(" ") if i != ""]

for i in range(len(times)):
    races.append((int(times[i]), int(distances[i])))

total = 1

for race in races:
    time = race[0]
    record = race[1]

    winning_times = []

    for time_held in range(0, time + 1):
        speed = 0

        speed = time_held

        distance = speed * (time - time_held)

        if distance > record:
            winning_times.append(time_held)
        elif len(winning_times) > 0:
            break

    total *= len(winning_times)

print(f"Total: {total}")
