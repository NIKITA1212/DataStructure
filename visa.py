
def data(a,b):
    x = a
    y = b
    while x != y :
        if x>y:
            x = x-y
        else:
            y = y-x

    return x
a = 2437
b= 875
print(data(a,b))
import math
def numberofways(n):
    k = 0
    num = 1
    while n>=3:
        n = n-3
        k = k+1
        if n == 0:
            return num +1
        else:
            combination = math.factorial(n+k)/(math.factorial(k)*math.factorial(n))
            num = num +int(combination)
    return num

print(numberofways(1))
print(numberofways(2))
print(numberofways(3))
print(numberofways(4))
print(numberofways(5))
print(numberofways(6))
print(numberofways(7))
print(numberofways(8))
print(numberofways(9))
print(numberofways(10))


