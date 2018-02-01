#чистка файла
def reading(filename):
    sym = "0123456789.,?!:;()[]-_|/\"'«»*{}<>@#$%^&№"
    s = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                s.append(word.strip(sym))
    return s

#создание списка, состоящего только из слов с нужной приставкой
def selection(s, pre):
    t = []
    for word in s:
        if word.startswith(pre):
            t.append(word)
    return t

#подсчет количества слов с данной приставкой, которые длиннее заданной цифры
def selection_2(t, num):
    long = 0
    for word in t:
        if len(word) > num:
            long += 1
    return long

#подсчет процента этих длинных слов среди всех слов с нужной приставкой
def percent(s1, s2):
    perc = round((s1 / s2)*100, 2)
    return perc


def main(text, pre):
    num = int(input("Введите ограничитель: "))
    print ("Всего слов с данной приставкой:", len(selection(reading(text), pre)), "\nПроцент длинных слов с данной приставкой:", percent(selection_2(selection(reading(text), pre), num), len(selection(reading(text),pre))), '%')


main('Pride_and_Prejudice.txt', 'un')
