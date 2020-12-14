import re
import random

f = open ('input', 'r')
out = [0]*36
flag = 'Part 1'
address = {}
for line in f:
    if line == "<>":
        break
    parse = re.split(' = ', line)
    if parse[0] == 'mask':
        mask = parse[1]
    else:
        index = int(parse[0][4:len(parse[0]) - 1])
        if flag == 'Part 1':
            inp0 = bin(int(parse[1]))[2:].zfill(36)
            for i in range(36):
                if mask[i] != 'X':
                    out[i] = mask[i]
                else:
                    out[i] = inp0[i]
            ord = 0
            out_tot = 0
            for j in range(len(out)):
                out_tot += int(out[len(out)-j-1])*(2**ord)
                ord += 1
            address[index] = out_tot
        elif flag == 'Part 2':
            inp0 = bin(index)[2:].zfill(36)
            inp1 = int(parse[1])
            for i in range(36):
                if mask[i] == '0':
                    out[i] = inp0[i]
                else:
                    out[i] = mask[i]
            out_unmasked = []
            num_x = out.count('X')
            while len(out_unmasked) < 2**num_x:
                out2 = out.copy()
                for i in range(36):
                    if out2[i] == 'X':
                        out2[i] = str(random.randint(0,1))
                test = 0
                ord = 0
                for j in range(len(out2)):
                    test += int(out2[len(out2) - j - 1]) * (2 ** ord)
                    ord += 1
                if test not in out_unmasked:
                    out_unmasked.append(test)
            for i in out_unmasked:
                address[i] = inp1
print(sum(address.values()))
