
def stacksort(l):
    temp = list()
    while len(l) != 0:
        p = l.pop()
        while len(temp) != 0 and  p < (temp[-1]):
            x = temp.pop()
            l.append(x)


        temp.append(p)
    return  temp
a = [1,4,15,7,17,9]

print(stacksort(a))

