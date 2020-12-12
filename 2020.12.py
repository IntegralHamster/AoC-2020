f = open ('input', 'r')
inp = []
for line in f:
    if line == "<>":
        break
    inp.append(line.strip())
# ang = ['E', 'S', 'W', 'N']
# x = 0
# y = 0
# point = 0
# for i in range(len(inp)):
#     if inp[i] == 'R90' or inp[i] == 'L270':
#         point += 1
#     elif inp[i] == 'R180' or inp[i] == 'L180':
#         point += 2
#     elif inp[i] == 'L90' or inp[i] == 'R270':
#         point -= 1
#     else:
#         if inp[i][0] == 'F':
#             inp[i] = ang[point%4] + inp[i][1:]
#         if inp[i][0] == 'E':
#             x += int(inp[i][1:])
#         elif inp[i][0] == 'W':
#             x -= int(inp[i][1:])
#         elif inp[i][0] == 'N':
#             y += int(inp[i][1:])
#         elif inp[i][0] == 'S':
#             y -= int(inp[i][1:])
# print(abs(x)+abs(y))
x = 0
y = 0
waypoint_x = 10
waypoint_y = 1
for i in range(len(inp)):
    if inp[i] == 'R90' or inp[i] == 'L270':
        tmp = waypoint_x
        waypoint_x = waypoint_y
        waypoint_y = -tmp
    elif inp[i] == 'R180' or inp[i] == 'L180':
        waypoint_x = -waypoint_x
        waypoint_y = -waypoint_y
    elif inp[i] == 'L90' or inp[i] == 'R270':
        tmp = waypoint_x
        waypoint_x = -waypoint_y
        waypoint_y = tmp
    else:
        if inp[i][0] == 'F':
            x += int(inp[i][1:])*waypoint_x
            y += int(inp[i][1:])*waypoint_y
        if inp[i][0] == 'E':
            waypoint_x += int(inp[i][1:])
        elif inp[i][0] == 'W':
            waypoint_x -= int(inp[i][1:])
        elif inp[i][0] == 'N':
            waypoint_y += int(inp[i][1:])
        elif inp[i][0] == 'S':
            waypoint_y -= int(inp[i][1:])
print(abs(x)+abs(y))