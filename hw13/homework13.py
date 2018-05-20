#Вариант 7

import os
import re

def obhod():
    d = {}
    path = '.'
    for root, dirs, files in os.walk(path):
        d[root] = len(files)
    num = max(d.values())
    print('Папка(-и) с наибольшим кол-вом файлов:')
    for root in sorted(d, key = d.get, reverse = True):
        r = re.search('\\\(\w+)$', root)
        if d[root] == num and r:
            string = r.group(1)
            print(string + '(' + str(d[root]) + ')')
        elif root == '.' and d[root] == num:
            print('Начальная папка' + '(' + str(d[root]) + ')')

def main():
    return obhod()

if __name__=='__main__':
    main()
