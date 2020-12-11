f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    inp.append(line.strip())
sum_full = 0
tmp = inp.copy()
while True:
    flag = 0
    inp2 = inp.copy()
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            count_full = 0
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if k == l == 0:
                        continue
                    elif 0 <= i + k <= len(inp) - 1 and 0 <= j+l <= len(inp[i])-1:
                        if inp[i+k][j+l] == '#':
                            count_full += 1
            if inp[i][j] == 'L' and count_full == 0:
                inp2[i] = inp2[i][:j] + '#' + inp2[i][j+1:]
                sum_full += 1
                flag = 1
            elif inp[i][j] == '#' and count_full >= 4:
                inp2[i] = inp2[i][:j] + 'L' + inp2[i][j + 1:]
                sum_full -= 1
                flag = 1
        # print(inp2[i])
    inp = inp2.copy()
    # print()
    if flag == 0:
        break
print(sum_full)
inp = tmp.copy()
sum_full = 0
while True:
    flag = 0
    inp2 = inp.copy()
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            count_full = 0
            for ang in [[-1,0],[-1,-1],[-1,1],[1,0],[1,-1],[1,1],[0,-1],[0,1]]:
                k = 1
                while True:
                    if 0 <= i + k*ang[0] <= len(inp) - 1 and 0 <= j + k*ang[1] <= len(inp[i]) - 1:
                        if inp[i + k*ang[0]][j + k*ang[1]] == '#':
                            count_full += 1
                            break
                        elif inp[i + k*ang[0]][j + k*ang[1]] == 'L':
                            break
                    else:
                        break
                    k += 1
            if inp[i][j] == 'L' and count_full == 0:
                inp2[i] = inp2[i][:j] + '#' + inp2[i][j+1:]
                sum_full += 1
                flag = 1
            elif inp[i][j] == '#' and count_full >= 5:
                inp2[i] = inp2[i][:j] + 'L' + inp2[i][j + 1:]
                sum_full -= 1
                flag = 1
        # print(inp2[i])
    inp = inp2.copy()
    # print()
    if flag == 0:
        break
print(sum_full)
