import re
from hopcroftkarp import HopcroftKarp

f = open ('input', 'r')
ing = []
allerg = []
for line in f:
    if line == "<>":
        break
    line = line.replace('(', '')
    line = line.replace(')', '')
    line = line.strip()
    parse = re.split(' contains ', line)
    ing.append(re.split(' ', parse[0]))
    allerg.append(re.split(', ',parse[1]))

correl = {}
for i in range(len(ing)):
    for j in ing[i]:
        if j not in correl.keys():
            correl[j] = allerg[i]
        else:
            tmp = correl[j].copy()
            for k in allerg[i]:
                if k not in tmp:
                    tmp.append(k)
            correl[j] = tmp

for i in correl.keys():
    tmp = correl[i].copy()
    pop = []
    for j in correl[i]:
        for k in range(len(ing)):
            if j in allerg[k] and i not in ing[k]:
                pop.append(j)
    for j in set(pop):
        tmp.pop(tmp.index(j))
    correl[i] = tmp

matching = HopcroftKarp(correl).maximum_matching(keys_only=True) # if you want to do p2 at the same time

nonallerg = []
for i in correl.keys():
    if i not in matching.keys(): 
  # if correl[i] == []:           - if you want to get just p1
        nonallerg.append(i)

count = 0
for i in ing:
    for j in nonallerg:
        if j in i:
            count += 1
print(count)

# Part 2
print(matching)
# Just do it manually, you lazy animal. It's faster.
# eggs fish nuts peanuts sesame shellfish soy wheat
# dtb,zgk,pxr,cqnl,xkclg,xtzh,jpnv,lsvlx
