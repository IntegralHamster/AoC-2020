f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    inp.append(line.strip())
i = 0
acc = 0
check = [0]
while True:
    if inp[i][:3] == 'nop':
        i += 1
    elif inp[i][:3] == 'acc':
        acc += int(inp[i][3:])
        i += 1
    elif inp[i][:3] == 'jmp':
        i += int(inp[i][3:])
    if i in check:
        break
    check.append(i)
print(acc)
for j in range(len(inp)):
    inp2 = inp.copy()
    i = 0
    acc = 0
    flag = 0
    check = [0]
    if inp2[j][:3] == 'nop':
        inp2[j] = 'jmp' + inp2[j][3:]
    elif inp2[j][:3] == 'jmp':
        inp2[j] = 'nop' + inp2[j][3:]
    while True:
        if inp2[i][:3] == 'nop':
            i += 1
        elif inp2[i][:3] == 'acc':
            acc += int(inp2[i][3:])
            i += 1
        elif inp2[i][:3] == 'jmp':
            i += int(inp2[i][3:])
        if i in check:
            break
        elif i >= len(inp):
            flag = 1
            break
        check.append(i)
    if flag == 1:
        break
print(acc)
