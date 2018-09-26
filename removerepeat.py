a = [1,2,3,3,6,8,19,19,19,21]
x = set(a)
print(list(x))


final = list()
c = 0
while( c <len(a)):
  if len(final) == 0:
      final.append(a[c])
      c +=1
  if final[c-1] != a[c]:
      final.append(a[c])
      c +=1
print(final)

