f = open ('input','r')
inp = []
inp_c = []
c = 0
a = " "
for line in f:
    if line == "<>":
        break
    a = a + line.strip()
    c += 1
    if line == "\n":
        inp.append(a.strip())
        a = ""
        c -= 1
        inp_c.append(c)
        c = 0
inp.append(a.strip())
inp_c.append(c)
count = 0
for i in range(len(inp)):
    count += len(set(inp[i]))
    print(inp[i])
    print(inp_c[i])
    print(set(inp[i]))
print(count)
count2 = 0
for i in range(len(inp)):
    for j in set(inp[i]):
        if inp[i].count(j) == inp_c[i]:
            count2 += 1
print(count2)
