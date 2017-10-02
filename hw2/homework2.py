##Вариант 2
x = 0
while x == 0:
    print ("Введите слово на русском:")
    a = input().lower()
    cyrlet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    for letter in a:
        if not (letter in cyrlet):
            print ("Напишите по-русски")
            x = 0
            break
        else:
            x = 1
need = 'опе'
y = 0
for i in range (len(a)):
    if (i % 2 == 0) and (a[i] in need):
            print (a[i])
            y = 1
if y == 0:
    print ("Нет букв, удовлетворяющих условию")
            
