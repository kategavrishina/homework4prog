numbers = []
sum = 0
amount = 0
num = input("Введите число: ")
if num.isdigit():
    while num != "":
        list = ''
        list += num
        numbers.append(int(list))
        num = input("Введите число: ")
    for element in numbers:
        amount += 1
        sum += element
    middle = sum/amount
    print ("Среднее арифметическое: ", round(middle,2),\
           "\nМинимальное: ", min(numbers),\
           "\nМаксимальное: ", max(numbers))
    
else:
    print("Вы не ввели число")
