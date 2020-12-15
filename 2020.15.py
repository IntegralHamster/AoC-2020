import re

numbers = {}
f = open ('input', 'r')
inp = re.split(',', f.readline())
for i in range(len(inp)):
    numbers[int(inp[i])] = i + 1

i = len(inp) - 1
lastnumber = int(inp[-1])
flag = 0

while i < 30000000:
    i += 1
    if flag == 0:
        nextnumber = 0
    else:
        nextnumber = i - numbers[lastnumber]
    numbers[lastnumber] = i
    if nextnumber in numbers.keys():
        flag = 1
    else:
        flag = 0
    lastnumber = nextnumber
    if i == 30000000-1:
        print(lastnumber)
