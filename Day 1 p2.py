file = open("input.txt", "r")

left = 0
right = 0
goal = 0
amount = 0
pass_zero = 0
start = 50
total_value = 50

for line in file:
    if line[0] == "L":
        left += 1
    elif line[0] == "R":
        right += 1

    direction = line[0]
    value = int(line[1:])

    if direction == 'R':
        current = total_value // 100
        total_value += value
        new_hundreds = total_value // 100
        pass_zero += (new_hundreds - current)

    elif direction == 'L':
        shifted = (total_value - 1) // 100
        total_value -= value
        new_hundreds = (total_value - 1) // 100
        pass_zero += (shifted - new_hundreds)

    total_value = total_value % 100

    if total_value == goal:
        amount += 1
print(pass_zero)
file.close()