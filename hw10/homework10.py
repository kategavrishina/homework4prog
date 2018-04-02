#Вариант 7

import re

def searching():
    filename = input('Введите название файла с расширением: ')
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        r = re.search('ISO 639-3.+\n.+data-wikidata-external-id="(...)"', text)
        if r:
            string = r.group(1)
            print(string)
            with open('result.txt', 'a', encoding = 'utf-8') as g:
                g.write(string + '\n')
    
def main():
    return searching()

if __name__=='__main__':
    main()
