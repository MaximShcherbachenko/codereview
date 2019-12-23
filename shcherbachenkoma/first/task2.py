"""
Порахувати кількість порожніх списків у заданому списку

"""

list = [1, 2, [], 3, 4, []]
sum = 0
for i in range(len(list)):
    if list[i] == []:
        sum += 1
print(sum)
