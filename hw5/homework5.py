#Вариант7
#Демонстрация результата в конце
print("Введите 8 слов, разделив их пробелом:")
words = input()
list = words.split(" ")
if len(list)>8 or len(list)<8:
    print("Введите РОВНО 8 слов")
else:
    with open("result.txt", "w", encoding="utf-8") as f:
        i=1;
        for words in list:
            f.write(words)           
            if i % 2 == 0 and i != 8:
                f.write("\n")
            i=i+1
    with open("result.txt", "r", encoding="utf-8") as s:
        result = s.read()
        print(result)
        s.close
