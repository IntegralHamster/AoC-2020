import re

f = open ('input', 'r')
start = int(f.readline())
bus_t = re.split(',',f.readline())
bus = []
for i in bus_t:
    if i.isnumeric():
        bus.append(int(i))
print(bus)
minutes = 1
flag = 0
while flag == 0:
    for j in bus:
        if (start + minutes) % j == 0:
            flag = 1
            print(j*minutes)
    minutes += 1
bus_delay = [[0]*2 for i in range(len(bus))]
k = 0
multi = 1
for i in range(len(bus_t)):
    if bus_t[i].isnumeric():
        bus_delay[k][0] = int(bus_t[i])
        multi *= int(bus_t[i])
        bus_delay[k][1] = i % bus_delay[k][0]
        k += 1
hugenumber = 0
for i in bus_delay:
    hugenumber += i[1]*(multi//i[0])*pow(multi//i[0], i[0]-2, i[0])
print(multi - hugenumber % multi)
