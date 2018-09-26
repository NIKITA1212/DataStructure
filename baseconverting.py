def toStr(n,base):
   convertString16 = "0123456789ABCDEF"
 #  print(convertString16[::-1])
   convertString8 = "01234567"
   convertString2 = "01"
   if n < base:
      return convertString8[n]
   else:
      return toStr(n//base,base) + convertString2[n%base]

print(toStr(25,2))


from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))
