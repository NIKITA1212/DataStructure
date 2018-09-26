m = [[1, 0, 1, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1],
     [1, 1, 1, 1, 1]]
for x in m :
    print(x)
row = len(m)
col = len(m[0])
r = set()
c = set()
for x in range(row):
    for y in range(col):
         if m[x][y] == 0 :
             r.add(x)
             c.add(y)
#print(r ,c)
for x in r:
    for y in range(col):
        m[x][y] = 0
#print(m)

for x in range(row):
    for y in c:
        m[x][y] = 0
#print(m)

for x in m:
    print(x)