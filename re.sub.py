import re

def changing(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        ch = {'а':'а','е':'е','ей':'ой','ам':'ам','ами':'ами','у':'у','ах':'ах','':'','ы':'ы'}
        for change in ch:
            text = re.sub('птиц' + change + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)','рыб' + ch[change] + '\\1',text)
            text = re.sub('Птиц' + change + '([ 0123456789\.,\?!…:;()\[\]\-_\|\/\"\'«»\*{}\<>@#\$%\^&№]|\n|\t)','Рыб' + ch[change] + '\\1',text)
    with open('birds_result.txt', 'w', encoding = 'utf-8') as g:
        g.write(text)

def main():
    return changing("birds.txt")

if __name__=='__main__':
    main()     
