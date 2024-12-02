def extrapolate_history(history):
    # Generate a sequence of differences
    diff = []
    for i in range(len(history)):
        if i < len(history) - 1:
            diff.append(history[i + 1] - history[i])

    # Check if all elements in the sequence are zero
    if all(x == 0 for x in diff):
        return None

    # Repeat the process until we reach a sequence with only zeros
    else:
        return extrapolate_history(diff)

# Read the input data from a file
with open("./day9.txt", "r") as f:
    histories = [[int(x) for x in line.split()] for line in f.readlines()]

# Extrapolate the next value for each history
next_values = []
for history in histories:
    next_value = extrapolate_history(history)
    if next_value is not None:
        next_values.append(next_value)

print(sum(next_values))