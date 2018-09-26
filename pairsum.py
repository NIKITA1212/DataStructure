from itertools import groupby
l = [3,2,6,2,0,5,3,8,7,10]
p = list()
'''
for x in l:
    if x not in p:
        p.append(x)'''
p = list(set(l))
p = sorted(p)
sum = 10

pair = list()
for x in p:
    if abs(sum-x) in p :
        p.remove(x)
        p.remove(abs(sum-x))
        y = (abs(sum-x),x)
        if y not in pair:
            pair.append(tuple(y))

print(pair)
print(p)
    