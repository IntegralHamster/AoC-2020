def adj_check (inp_grid):
    out_grid = {}
    x0 = []
    y0 = []
    z0 = []
    t0 = []
    for m in inp_grid.keys():
        x0.append(m[0])
        y0.append(m[1])
        z0.append(m[2])
        t0.append(m[3])
    for x in range(min(x0) - 1, max(x0) + 2):
        for y in range(min(y0) - 1, max(y0) + 2):
            for z in range(min(z0) - 1, max(z0) + 2):
                for t in range(min(t0) - 1, max(t0) + 2):
                    adj = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                for dt in range(-1,2):
                                    if dx == 0 and dy == 0 and dz == 0 and dt == 0:
                                        continue
                                    elif inp_grid.get((x + dx, y + dy, z + dz, t + dt), False):
                                        adj += 1
                    if (inp_grid.get((x, y, z, t), False) and adj in (2,3)) or (not inp_grid.get((x, y, z, t), False) and adj == 3):
                        out_grid[(x, y, z, t)] = True
    return out_grid


f = open('input', 'r')
grid = {}
j = 0
for line in f:
    if line == "<>":
        break
    line = line.strip()
    for i in range(len(line)):
        grid[(i,j,0,0)] = line[i] == '#'
    j += 1

for i in range(6):
    grid = adj_check(grid)
    print(sum(grid.values()))







