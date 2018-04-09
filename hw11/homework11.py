#Вариант 7
#Замена птиц на рыб
#Не знала, в каком файле это надо делать, поэтому прикладываю и txt, и html

import re

def changing(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        # вариант 'и' - для аналогов в болгарском и македонском
        rg = ['а','е','ы','ам','у','','ами','ах','и']
        for regexp in rg:
            text = re.sub(r'птиц' + regexp + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)',\
                          r'рыб' + regexp + '\\1', text)
            text = re.sub(r'Птиц' + regexp + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)',\
                          r'Рыб' + regexp + '\\1', text)
            # я не придумала, как заменять этот вариант более компактно
            text = re.sub(r'птицей' + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)',\
                          r'рыбой' + '\\1', text)
            text = re.sub(r'Птицей' + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)',\
                          r'Рыбой' + '\\1', text)
            text = re.sub(r'Пти́ц' + regexp + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)',\
                          r'Ры́б' + regexp + '\\1', text)
        with open('fish.txt', 'w', encoding = 'utf-8') as g:
            g.write(text)


def main():
    return changing("birds.html")

if __name__=='__main__':
    main()          
    
