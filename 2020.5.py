import string

f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    line = line.replace('B','1')
    line = line.replace('R', '1')
    line = line.replace('F', '0')
    line = line.replace('L', '0')
    line = line.strip()
    ord = 0
    id = 0
    for j in range(len(line)):
        id += int(line[len(line)-j-1])*(2**ord)
        ord += 1
    inp.append(id)
print(max(inp)) #part 1 answer

for i in range(1024):
    if i not in inp and max(inp) - len(inp) < i < max(inp):
        print(i) #part 2 answer