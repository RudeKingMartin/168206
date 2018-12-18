def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

list=[45,15,24,48]
print(sum(list))