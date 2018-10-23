n = 0.625
l = ["0."]
m = ["0."]
def realToBinary(n):

    if n >=1 or n <=0 :
        return "Error"
    while n > 0 :

        if len(l) >= 32:
            return "Error"
        r = n * 2
        if r >=1 :
            l.append(1)
            n = r-1
        else:
            l.append(0)
            n = r
    return l

def rToB(n):
    if n >=1 or n<=0:
        return "Error"
    frac = 0.5
    while n>0:
        if len(m)>=32:
            return "Error"
        if n >= frac:
            m.append(1)
            n = n-frac
        else:
            m.append(0)

        frac /= 2
    return m
print(" Binary of {} is {}.".format(n,"".join((str(x) for x in realToBinary(0.625)))))
print(" Binary of {} is {}.".format(n,"".join((str(x) for x in realToBinary(0.72)))))
print(" Binary of {} is {}.".format(n,"".join((str(x) for x in rToB(0.625)))))
print(" Binary of {} is {}.".format(n,"".join((str(x) for x in rToB(0.72)))))