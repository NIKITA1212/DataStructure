# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
   # x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    q = ''.join(S.split())
    p = [d for d in q]

    # print(p)
    a = list()
    for s in p:
        if s.isdigit():
            a.append(s)

    n = ''.join(a)
    print(n)

    return ('-'.join(n[i:i + 3] for i in range(0, len(n), 3)))

print(solution("0 - 22 1985--324"))
'''
RUNTIME ERROR  (tested program terminated with exit code 1) 

Example test:    '0 - 22 1985--324' 
Output (stderr):
Invalid result type, string expected, <class 'NoneType'> found.
Output:
0221985324
022-198-532-4
RUNTIME ERROR  (tested program terminated with exit code 1) 

Example test:    '555372654' 
Output (stderr):
Invalid result type, string expected, <class 'NoneType'> found.
Output:
555372654
555-372-654
RUNTIME ERROR  (tested program terminated with exit code 1) 

Producing output might cause your solution to fail performance tests.
You should remove code that produces output before you submit your solution. 

Detected some errors.

'''