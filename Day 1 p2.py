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
    number = line[1:]
    value = int(number)

    if direction == 'R':
        temp_value = total_value + value
        if temp_value >= 100:
            pass_zero += temp_value // 100 # Help from Reddit (had +=1)
        total_value = temp_value
    elif direction == 'L':
        temp_value = total_value - value
        if temp_value < 0:
            pass_zero += (abs(temp_value) // 100) + 1 # Help from Reddit (had +=1)
        total_value = temp_value
    # Mododulus
    total_value = total_value % 100

    if total_value == goal:
        amount += 1
print(pass_zero)
print(amount)

file.close()