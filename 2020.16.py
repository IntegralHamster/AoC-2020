iimport re

f = open ('input', 'r')
ranges = []
data = []
ticket = []
test_tickets = []
flag = 0
for line in f:
    if line == "<>":
        break
    line = line.strip()
    if line == 'your ticket:':
        flag = 1
    elif line == 'nearby tickets:':
        flag = 2
    elif flag == 0:
        parse = re.split(': | or |-',line)
        data.append(parse[0])
        ranges.append([int(parse[1]), int(parse[2])])
        ranges.append([int(parse[3]), int(parse[4])])
    elif flag == 1:
        parse = re.split(',',line)
        for i in parse:
            ticket.append(int(i))
    elif flag == 2:
        parse = re.split(',',line)
        ticket_o = []
        for i in parse:
            ticket_o.append(int(i))
        test_tickets.append(ticket_o)

invalid = []
getrid = []
for i in test_tickets:
    flag2 = 0
    for j in i:
        flag = 0
        for l in ranges:
            if l[0] <= j <= l[1]:
                flag = 1
        if flag == 0:
            flag2 = 1
            invalid.append(j)
    if flag2 == 1:
        getrid.append(test_tickets.index(i))
print(sum(invalid))

possible_positions_tot = []
for i in range(len(test_tickets)):
    if i not in getrid:
        possible_pos = []
        for j in test_tickets[i]:
            possibilities = []
            for l in range(len(ranges)):
                if ranges[l][0] <= j <= ranges[l][1]:
                    possibilities.append(l // 2)
            possible_pos.append(possibilities)
        possible_positions_tot.append(possible_pos)

possible_names = []
for i in range(len(ranges)//2):
    name = []
    for j in range(len(possible_positions_tot[0])):
        flag = 0
        for k in possible_positions_tot:
            if i not in k[j]:
                flag = 1
                break
        if flag == 0:
            name.append(j)
    possible_names.append(name)

fix_pos_alr = []
while True:
    fix_pos = -1
    for i in possible_names:
        if len(i) == 1 and i[0] not in fix_pos_alr:
            fix_pos = i[0]
    if fix_pos == -1:
        break
    else:
        for i in possible_names:
            if fix_pos in i and len(i) != 1:
                i.pop(i.index(fix_pos))
        fix_pos_alr.append(fix_pos)

ans2 = 1
for i in range(6):
    ans2 *= ticket[possible_names[i][0]]
print(ans2)
