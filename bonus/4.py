rusvow = "аеёиоуэюя"
while 1:
    print ()
    word = input ("Введите слово: ")
    for i in word:
        if i in rusvow:
            i = i + "с" + i
            print (i, end = "")
        else:
            print (i, end = "")
