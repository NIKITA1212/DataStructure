a = [1,2,3,3,8,8,8,9]
p2=1
p1=1
while p1 != (len(a)):
    if a[p1] != a[p1-1] :
        a[p2] = a[p1]
        p2 +=1
    p1+=1

print(a[0:p2])