import re

file = open("Day 2 input.txt", "r")
invalid_id = []
content = file.read()
pattern = r"(\d+)[,]\1"
res = re.findall(r'\d+', content)
for i in res:
    match = re.fullmatch(pattern, i)
    if match:
        invalid_id.append(i)

print("results: " + str(len(invalid_id)))
file.close()


