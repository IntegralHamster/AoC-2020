import re
import string

f = open ('input','r')
inp = []
a = " "
for line in f:
    if line == "<>":
        break
    a = a + line.strip() + " "
    if line == "\n":
        inp.append(a.strip())
        a = " "
inp.append(a.strip())
print(inp)
count = 0
for i in range(len(inp)):
    if ("byr" in inp[i]) and ("iyr" in inp[i]) and ("eyr" in inp[i]) and ("hgt" in inp[i]) and ("hcl" in inp[i]) and ("ecl" in inp[i]) and ("pid" in inp[i]):
        count+=1
print(count)
count2 = 0
for i in range(len(inp)):
    check = re.split(':|\s', inp[i])
    check_count = 0
    for j in range(len(check)):
        if j % 2 == 0 and len(check) >= 14:
            if check[j] == "byr" and ("1920" <= check[j+1] <= "2002" and check[j+1].isdecimal):
                check_count += 1
            if check[j] == "iyr" and ("2010" <= check[j+1] <= "2020" and check[j+1].isdecimal):
                check_count += 10
            if check[j] == "eyr" and ("2020" <= check[j+1] <= "2030" and check[j+1].isdecimal):
                check_count += 100
            if check[j] == "ecl" and check[j+1] in ("amb","blu","brn","gry","grn","hzl","oth"):
                check_count += 1000
            if check[j] == "pid" and (len(check[j+1]) == 9 and check[j+1].isdecimal):
                check_count += 10000
            if check[j] == "hcl":
                flag = 0
                for letter in check[j+1][1:]:
                    if letter not in string.hexdigits:
                        flag = 1
                if flag != 1 and check[j+1][0] == "#":
                    check_count += 100000
            if check[j] == "hgt" and ((len(check[j+1]) == 5 and "150" <= check[j+1][:3] <= "193" and check[j+1][3:] == "cm") or
                                          (len(check[j + 1]) == 4 and "59" <= check[j + 1][:2] <= "76" and check[j + 1][2:] == "in")):

                check_count += 1000000
    if check_count == 1111111:
        count2 += 1
    if len(check) >= 14 and check_count != 1111111:
        print(check)
        print(check_count)
print(count2)