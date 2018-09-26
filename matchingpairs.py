#a = "ABbb"
#a="ABbCca"
a = "ABbba"
l = list(a)
new = [l[0]]
x = 1
while len(new) != 0 and x <len(l):
    if l[x].isupper() == True :
        new.append(l[x])
        x +=1
    elif new[-1] == l[x].upper():
            new.pop()
            x +=1

    else:
        break
print(x-1)