"""
The deletion distance between two strings is the minimum sum of ASCII values of characters that you need to delete in the two
strings in order to have the same string.The deletion distance between cat and at is 99, because you can just delete the first character of cat and the ASCII value of 'c' is 99. The deletion distance between cat and bat is 98 + 99, because you need to delete the first character of both words.Of course, the deletion distance between two strings can't be greater than the sum of their total ASCII values, because you can always just delete both of the strings entirely. Implement an efficient function to find the deletion distance between two strings. You can refer to the Wikipedia article on the algorithm for edit distance if you want to. The algorithm there is not quite the same as the algorithm required here, but it's similar.


Test
Input
Expected
Result
Result
Log
"at", "cat"
99
99
running
code
Execution
done in 0.059235818
s.
"boat", "got"
298
298
"thought", "sloughs"
674
674

"""
def ascii_deletion_distance(s1, s2):
    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    result = sum(map(ord, s1 + s2)) - dp[l1][l2] * 2
    return result

print(ascii_deletion_distance("cat","at"))