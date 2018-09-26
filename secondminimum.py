

def secondmin(a):
    s = 1000
    f = 10000

    for x in range(len(a)):
        if a[x]<f :
            s = f
            f = a[x]


        elif a[x] <s and a[x] != f :
            s = a[x]
    return s

def secondmax(a):
    s = -1
    f = -1

    for x in range(len(a)):
        if a[x] > f:
            s = f
            f = a[x]
        elif a[x] > s and a[x] != f:
            s = a[x]
    return s

a = [1,0,8,3,6,11,7,21]
print("max",secondmax(a))
print("min",secondmin(a))