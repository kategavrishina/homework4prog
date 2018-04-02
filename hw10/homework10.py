#Вариант 7
#Прости, что не прикладываю сайты, вместе с ними скачивается множество других файлов, прилагающихся к HTML

import re

def searching():
    filename = input('Введите название файла с расширением: ')
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            r = re.search('data-wikidata-external-id="(...)" data-wikidata-property-id="P220"', line)
            if r:
                string = r.group(1)
                with open('result.txt', 'a', encoding = 'utf-8') as g:
                    g.write(string + '\n')
    
def main():
    print(searching())

if __name__=='__main__':
    main()
