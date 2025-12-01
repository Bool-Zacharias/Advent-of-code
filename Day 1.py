file = open("input.txt","r") 

content = file.read()

goal = 0
start = 50

for line in file:
    if line[0] == "L":
        left +=1
    elif line[0] =="R":
        right +=1

print("L:", left)
print("L:", right)

file.close()