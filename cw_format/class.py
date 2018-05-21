'''
# comprehensions
a = [1, 2, 4 ,6]
b = [i*2 for i in a]
b = [i*2 for i in a if i > 3]

o = []
x = 15
for _ in range(x):
    o.append(0)
# _, а не i, потому что значение переменной нас не интересует

o = [o for _ in range(x)]

s.upper() a -> A
s.lower() b -> B
s.capitalize() name -> Name

words = ['Анна', 'Brother', 'Moscow', 'Калуга']

d = {'a':1, 'b':2}
d1 = {k:v for k,v in enumerate(words)}
--> {'1':'Анна', '2':'Brother'...}

s1 = 'I lo'
s2 = 've linguistics'

# t.format()
t = '{}{}'
print(t.format(s1,s2)) или ('{}{}'.format(s1,s2))
Работает с числами!
print('{1}{0}'.format(s1,s2)) - индексы наоборот

a = [1, 100, 28]
t = 'Возраст: {:>10}' - выравнвиание справа
# {:<10} - выравнивание слева, {:^} - выравнивание посередине
# {:+>10} заполнить строку плюсами
for i in a:
    print(t.format(i))

'{:.2f}'.format(pi) - 2 знака после запятой
'{:.2}' - 2 символа, как срез

import re

def wrds():
    words = ['Анна', 'Brother', 'Moscow', 'Калуга']
#только те, которые латиницей + к нижнему регистру
    new = [word.lower() for word in words if re.search('^[A-Za-z]+$', word)]
    print(', '.join(new))

'''

def reading(filename):
    sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
    s = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                s.append(word.strip(sym))
    return s

def main(s):
    i = 1
    for word in s:
        print('{}. {:>10}'.format(i, word))
        i += 1
        
if __name__=='__main__':
    main(reading('text.txt'))









    
