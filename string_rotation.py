"""
def is_rotation(str1, str2):
    return(len(str1) == len(str2) and str1 in str2*2)
"""

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    for index in range(len(str1)):
        if str2.startswith(str1[index:]) and str2.endswith(str1[:index]):
            return True

    return False
"""
def is_rotation(s1,s2):
    for x in s1:
        s2.index(x)
        break 
"""

print(is_rotation("waterbottle","erbottlewat"))
print(is_rotation("hello","llohx"))