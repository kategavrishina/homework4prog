#Вариант 7
#Папки и с кирилиическими, и с латинскими символами в названии

import os
import re

def searching():
    need = []
    file_list = os.listdir()
    for name in file_list:
        if os.path.isdir(name):
            if re.search('([А-Яа-я]+.+?[A-Za-z]+)|([A-Za-z]+.+?[А-Яа-я]+)', name):
                need.append(name)
    print('Количество искомых папок:', len(need))
    print('Список искомых папок:', end = '\n')
    print('\n'.join(need))

def main():
    return searching()

if __name__=='__main__':
    main()  

