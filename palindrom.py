list = ['madam', 'chair','malayalam','tiger']

for index , x in enumerate(list):
    if x == x[::-1]:
        list[index] ="True"
    else:
        list[index] = "False"

print(list)

