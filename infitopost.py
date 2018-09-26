#anagram sort
words = ['abc', 'cab', 'cafe', 'goo', 'face']
from itertools import groupby

print(sorted(words))

print([list(group) for key,group in groupby(sorted(words),sorted)])
print([list(key) for key,group in groupby(sorted(words, key=sorted),sorted)])

