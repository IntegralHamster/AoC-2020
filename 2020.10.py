f = open ('input','r')
inp = [0]
for line in f:
    if line == "<>":
        break
    inp.append(int(line.strip()))
inp.append(max(inp)+3)
inp.sort()
count1 = 0
count3 = 0
for j in range(len(inp)-1):
    if inp[j+1] - inp[j] == 1:
        count1 += 1
    elif inp[j+1] - inp[j] == 3:
        count3 += 1
print(count1*count3)

adj_matrix = [[0]*len(inp) for i in range(len(inp))]
for i in range(len(inp)):
    for j in range(len(inp)):
        if 1 <= inp[i] - inp[j] <= 3:
            adj_matrix[i][j] = inp[i] - inp[j]
ways = [1]
for i in range(1,len(inp)):
    count_ways = 0
    for j in range(i):
        if adj_matrix[i][j] > 0:
            count_ways += ways[j]
    ways.append(count_ways)
print(ways[len(inp)-1])
