
#sum of integer represent as a string
from itertools import groupby
l = ["niki","shreyas","unna","binjal","dashan","kirtan","yogi","tilak"]


print(int("123")+int("456"))

for x in sorted(l):
    print(x ,end=",")

a = "abc - def -1"
print(a.split("-"))


def recursive(n):
    if n<=0 :
        return n
    else:
        o = recursive(n-1)
        return o

print(recursive(2))

p = "003- 5435-323 2 4 6"
a = [1,2,3,4,5,6,7,8,9,0]
w = "".join(p.split())
x = list("".join(w.split("-")))
s = len(x)-4
t = "".join(x[:s])
q = "".join(x[s:])
p1 = '-'.join(t[i:i+3] for i in range(0,len(t),3)) +"-"

p2 = '-'.join(q[i:i+2] for i in range(0,len(q),2))

print("".join(p1+p2))
#print('-'.join(a[x:x+3] for x in range(0,len(a),3)))


a = [1,2]
print(len(a))
if ((len(a)==0) == False):
    print("condition true")
else:
    print("condition false")

from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(list(d.items()))
print("=====")

s = "1234567"
print (type(s[17%8]))
print ("1"+"2")
source=[]
if source: # if source is not null or not empty
    print(1)
else:
    print(0)

print("======")

s = "my name is Nikita."
t = list(s)
l = list()
for x in t:
    if x == " ":
        l.append("%20")
    else:
        l.append(x)
print("".join(l))
print(s.replace(" ","%20"))

s = [[1,2,3],[4,5,6],[7,8,9]]
print(s)
for t in zip(*s):
    print (t)
    print(list(reversed(t)))
new = [list(reversed(t)) for t in zip(*s)]
print(new)
#for row in new:
 #   print(row)
