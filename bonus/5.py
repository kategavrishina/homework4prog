cons = "bcdfghjklmnpqrstvwxz"
rus = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
while 1:
    print ()
    word = input ("Введите слово на английском: ")
    for i in word:
        if i in rus:
            print ("Слово на русском, исправьте.")
            break
        else:
            if i in cons:
                i = i + "aig"
                print (i, end = "")
            else:
                print (i, end = "")
