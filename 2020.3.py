f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    inp.append(line.strip())
x = 0
count = 0
for i in range(len(inp)):
    if inp[i][x] == '#':
        count += 1
    x += 7
    if x >= len(inp[i]):
        x %= len(inp[i])
print(count)
x = 0
y = 0
count = 0
while y < len(inp):
    if inp[y][x] == '#':
        count += 1
    y += 2
    x += 1
    if x >= len(inp[i]):
        x %= len(inp[i])
print(count)