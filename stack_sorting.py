s1 = []
s2 = []


def push_and_sort(element):
    if s1 == []:
        s1.append(element)
    else:
        while( s1 != [] and element < s1[-1]):
                s2.append(s1.pop())
        s1.append(element)

        while (s2 != []):
            s1.append(s2.pop())


push_and_sort(5)
push_and_sort(10)
push_and_sort(0)
push_and_sort(15)
push_and_sort(7)
push_and_sort(2)
print(s1)
