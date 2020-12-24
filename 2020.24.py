f = open('input', 'r')
tiles = []
for line in f:
    if line == '<>':
        break
    line = line.strip()
    coord = [0, 0, 0]
    i = 0
    while i < len(line):
        if line[i] == 'e':
            coord[0] += 1
            coord[2] -= 1
            i += 1
        elif line[i] == 'w':
            coord[0] -= 1
            coord[2] += 1
            i += 1
        elif line[i] == 'n':
            if line[i+1] == 'e':
                coord[0] += 1
                coord[1] -= 1
            elif line[i+1] == 'w':
                coord[1] -= 1
                coord[2] += 1
            i += 2
        elif line[i] == 's':
            if line[i+1] == 'e':
                coord[1] += 1
                coord[2] -= 1
            elif line[i+1] == 'w':
                coord[0] -= 1
                coord[1] += 1
            i += 2
    if coord not in tiles:
        tiles.append(coord)
    else:
        tiles.pop(tiles.index(coord))
print(len(tiles))


def adj_check (inp_grid):
    out_grid = {}
    x0 = []
    y0 = []
    z0 = []
    for m in inp_grid.keys():
        x0.append(m[0])
        y0.append(m[1])
        z0.append(m[2])
    for x in range(min(x0) - 1, max(x0) + 2):
        for y in range(min(y0) - 1, max(y0) + 2):
            for z in range(min(z0) - 1, max(z0) + 2):
                if x + y + z == 0:
                    adj = 0
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):
                                if dx == 0 and dy == 0 and dz == 0:
                                    continue
                                elif inp_grid.get((x + dx, y + dy, z + dz), False) and (x + dx) + (y + dy) + (z + dz) == 0:
                                    adj += 1
                    if (inp_grid.get((x, y, z), False) and adj in (1,2)) or (not inp_grid.get((x, y, z), False) and adj == 2):
                        out_grid[(x, y, z)] = True
    return out_grid


grid = {}
for i in tiles:
    grid[i[0], i[1], i[2]] = True
for i in range(100):
    grid = adj_check(grid)
    if i % 10 == 9:
        print(len(grid.keys()))