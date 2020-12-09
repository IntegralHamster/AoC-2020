f = open ('input','r')
inp = []
for line in f:
    if line == "<>":
        break
    inp.append(int(line.strip()))
for j in range(25, len(inp)):
    flag = 0
    for i in range(25):
        if inp[j] - inp[j-i] in inp[j-25:j-1] and inp[j] - inp[j-i] != inp[j-i]:
            flag = 1
            break
    if flag == 0:
        print(inp[j])   #part1
        answer = inp[j]
        break
for i in range(len(inp)):
    if inp[i] != answer:
        test = []
        tot = 0
        j = i
        while True:
            test.append(inp[j])
            tot += inp[j]
            if tot >= answer:
                break
            j += 1
        if tot == answer:
            print(min(test)+max(test)) #part2
            break
