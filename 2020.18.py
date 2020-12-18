def find_bracket (str):
    br_count = 1
    for i in range(len(str)):
        if str[i] == '(':
            br_count += 1
        elif str[i] == ')':
            br_count -= 1
        if br_count == 0:
            return i


def calculate (str):
    if str[0] != '(':
        i = 0
        result = int(str[0])
    else:
        length = find_bracket(str[1:])
        result = calculate(str[1:length+1])
        i = length + 1
    while i < len(str) - 1:
        if str[i+2] == '(':
            length = find_bracket(str[i+3:])
            tmp_result = calculate(str[i+3:i+3+length])
            if str[i+1] == '+':
                result += tmp_result
            elif str[i+1] == '*':
                result *= tmp_result
            i += 3+length
        else:
            if str[i+1] == '+':
                result += int(str[i+2])
            elif str[i+1] == '*':
                result *= int(str[i+2])
            i += 2
    return result


def calculate2_electric_boogaloo(arr):
    if arr[0] != '(':
        i = 0
    else:
        length = find_bracket(arr[1:])
        arr[0] = calculate2_electric_boogaloo(arr[1:length+1])
        del arr[1:length+2]
        i = 0
    while arr.count('+') > 0:
        if arr[i + 2] != '(':
            if arr[i + 1] == '+':
                arr[i] = int(arr[i])+int(arr[i+2])
                del arr[i+1:i+3]
            else:
                i += 2
        else:
            if arr[i + 1] == '+':
                length = find_bracket(arr[i + 3:])
                tmp_result = calculate2_electric_boogaloo(arr[i + 3:i + 3 + length])
                arr[i] = int(arr[i]) + tmp_result
                del arr[i + 1:i + 4 + length]
            else:
                length = find_bracket(arr[i + 3:])
                arr[i+2] = calculate2_electric_boogaloo(arr[i + 3:i + 3 + length])
                del arr[i + 3:i + 4 + length]

    i = 0
    while arr.count('*') > 0:
        if arr[i + 1] == '*':
            if arr[i+2] != '(':
                arr[i] = int(arr[i])*int(arr[i+2])
                del arr[i+1:i+3]
            else:
                length = find_bracket(arr[i+3:])
                tmp_result = calculate2_electric_boogaloo(arr[i+3:i+3+length])
                arr[i] = int(arr[i]) * tmp_result
                del arr[i+1:i+4+length]
        else:
            i += 2
    if len(arr) == 1:
        return arr[0]


f = open ('input', 'r')
ans = 0
ans2 = 0
for line in f:
    if line == "<>":
        break
    line = line.strip()
    line = line.replace(' ', '')
    ans += calculate(line)
    inp2 = []
    for i in line:
        inp2.append(i)
    ans2 += calculate2_electric_boogaloo(inp2)
print(ans)
print(ans2)

