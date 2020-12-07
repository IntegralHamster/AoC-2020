import re

f = open ('input2','r')
inp = []
bags = []
for line in f:
    if line == "<>":
        break
    line = line.strip()
    line = line.replace('.','')
    line = line.replace(' bags','')
    line = line.replace(' bag','')
    parse = re.split(' contain |, ', line)
    for j in range(len(parse)):
        if j == 0:
            bag = parse[0]
        else:
            if parse[j] != 'no other':
                bag = parse[j][2:]
        if bag not in bags:
            bags.append(bag)
    print(parse)
    inp.append(line.strip())
adj_matrix = [[0]*len(bags) for i in range(len(bags))]
for i in range(len(inp)):
    parse = re.split(' contain |, ', inp[i])
    if parse[1] != 'no other':
        ind = bags.index(parse[0])
        for j in range(len(parse)-1):
            ind2 = bags.index(parse[j+1][2:])
            adj_matrix[ind][ind2] = int(parse[j+1][0])

def bag_count(i):
    count = ''
    flag = 0
    for j in range(len(adj_matrix[i])):
        if adj_matrix[j][i] > 0:
            flag = 1
            count += bags[j] + '@' + bag_count(j)
    if flag == 0:
        count += bags[i] + '@'
    return count

print(len(set(re.split('@',bag_count(bags.index('shiny gold'))[:-1]))))

def bag_count2(i):
    count = 0
    flag = 0
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] > 0:
            flag = 1
            count += adj_matrix[i][j] * (bag_count2(j)+1)
    if flag == 0:
        count = 1
    return count

def bag_count3(i):
    count = 0
    flag = 0
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] > 0:
            flag = 1
            count += adj_matrix[i][j] * (bag_count3(j))
    if flag == 0:
        count = 1
    return count

print(bag_count2(bags.index('shiny gold')) - bag_count3(bags.index('shiny gold')))