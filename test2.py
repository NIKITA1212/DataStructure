# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    right = 0
    left = 0
    # write your code in Python 3.6
    for x in S:
        if x == "(":
            left = left + 1
        if x == ")":
            right = right + 1

    return (max(right, left))