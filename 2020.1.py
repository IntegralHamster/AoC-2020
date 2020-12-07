import sys

f = open('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    line = line.strip()
    inp.append(int(line))

for i in range(len(inp)):
    for j in range(len(inp)):
        for k in range(len(inp)):
            if inp[i]+inp[j]+inp[k] == 2020 and i != j and j != k and i != k:
                print(inp[i]*inp[j]*inp[k])
                break