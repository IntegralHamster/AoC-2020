import sys
import re

f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    inp.append(line.strip())
count = 0
count2 = 0
for i in range(len(inp)):
    password = re.split('-|:|\s', inp[i])
    if int(password[0]) <= password[4].count(password[2]) <= int(password[1]):
        count += 1
    if (password[4][int(password[0])-1] == password[2]) != (password[4][int(password[1])-1] == password[2]):
        count2 += 1
print(count,count2)
