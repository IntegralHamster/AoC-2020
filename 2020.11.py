import copy

f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    line = line.strip()
    seats = []
    for a in line:
        seats.append(a)
    inp.append(seats)


def adj_check(arr, dist):
    sum_full = 0
    tmp = copy.deepcopy(arr)
    while True:
        flag = 0
        inp2 = copy.deepcopy(tmp)
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                count_full = 0
                for ang in [[-1, 0], [-1, -1], [-1, 1], [1, 0], [1, -1], [1, 1], [0, -1], [0, 1]]:
                    k = 1
                    while True:
                        if 0 <= i + k * ang[0] <= len(tmp) - 1 and 0 <= j + k * ang[1] <= len(tmp[i]) - 1:
                            if tmp[i + k * ang[0]][j + k * ang[1]] == '#':
                                count_full += 1
                                break
                            elif tmp[i + k * ang[0]][j + k * ang[1]] == 'L':
                                break
                        else:
                            break
                        if dist == 5:
                            k += 1
                        elif dist == 4:
                            break
                if tmp[i][j] == 'L' and count_full == 0:
                    inp2[i][j] = '#'
                    sum_full += 1
                    flag = 1
                elif tmp[i][j] == '#' and count_full >= dist:
                    inp2[i][j] = 'L'
                    sum_full -= 1
                    flag = 1
        tmp = copy.deepcopy(inp2)
        if flag == 0:
            break
    return sum_full

print(adj_check(inp, 4))
print(adj_check(inp, 5))
