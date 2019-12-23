"""
Вивести слова, які мястять хоча б одну велику букву

"""

string = input()
string = string.split(' ')
list = []
for i in range(len(string)):
   if string[i].lower() != string[i]:
        list.append(string[i])
print(str(list))
exit = input()
