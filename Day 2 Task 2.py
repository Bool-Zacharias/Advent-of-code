import re

file = open("Day 2 input.txt", "r")
content = file.read()
pattern = re.compile(r'^(\d+)\1+$')
ranges = content.split(",")
invalid_id = []
for i in ranges:
    parts = i.split("-")
    if len(parts) == 2:
        start = int(parts[0])
        end = int(parts[1])
        for num in range(start, end+1):
            x = str(num)
            if pattern.match(x):
                invalid_id.append(num)

print("results: " + str(sum(invalid_id)))
file.close()

