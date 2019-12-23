"""
Вхідні дані:  -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
Результат: список слів (у нижньому регістрі), що містить кожне друге слово та кількість його повторів 
Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Виклик функції: find_most_frequent('Hello, Hello, my dear Mom! I want play and play and football')
Повертає: [ [Hello,2] , [dear,1] , [I,1] , [play,2] ,[ football,1] ]

"""

import re

re_patern = re.compile("\w+")


def validator_1(patern, prompt):
    value = input(prompt)
    while not bool((patern.match(value))):
        value = input(prompt)
    return value
def validator_2(prompt):
    value = validator_1(re_patern, prompt)
    return value

our_input_data = validator_2("Enter string:")

our_input_data = list(our_input_data.split())
print(our_input_data)

def find_most_frequent(patern):
    new_list = []
    counter = 0
    for j in range(len(patern) - 1):
        for i in range(len(patern) - 1):
            if patern[j] == patern[i]:
                new_list.append(patern[j])
                counter += 1
        new_list.append(list[patern[j], counter])

    return new_list

print(find_most_frequent(our_input_data))
