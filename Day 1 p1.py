file = open("input.txt", "r")

left = 0
right = 0
goal = 0
amount = 0
start = 50
total_value = 50

for line in file:
    if line[0] == "L":
        left += 1
    elif line[0] == "R":
        right += 1

    direction = line[0]
    number = line[1:]
    value = int(number)

    if direction == 'R':
        total_value += value
    elif direction == 'L':
        total_value -= value
    
    # Modulus
    total_value = total_value % 100

    if total_value == goal:
        amount += 1
print(amount)

file.close()