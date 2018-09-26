
import math

# pascals_tri_formula = [] # don't collect in a global variable.

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop,
    # while count <= rows: # can avoid initializing and incrementing
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1):
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(combination(count, element))
        result.append(row)
        # count += 1 # avoidable
    return result

# now we can print a result:
for row in pascals_triangle(3):
    print(row)
print("----------------")

#n=int(input("Enter number of rows: "))
n = 5
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    #if(n!=0):
    a[i].append(1)
for i in range(n):
    #print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()

print("---------------")

def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result
print(triangle(8))