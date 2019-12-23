"""
Порахувати суму усіх парних та непарних чисел у заданому списку

"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
sum_paired = 0
sum_unpaired = 0
for i in range(len(list)):
    if list[i] % 2 == 0:
        sum_paired += list[i]
    else:
        sum_unpaired += list[i]
print("Sum of paired", sum_paired)
print("Sum of unpaired", sum_unpaired)
