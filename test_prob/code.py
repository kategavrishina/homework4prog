import re

def searching(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        a = re.findall('title="([а-яА-Я]+?швили),', text)
        b = re.findall('title="([а-яА-Я]+?дзе),', text)
        c = re.findall('title="([а-яА-Я]+?ия),', text)
        if len(a)>len(b):
            print('"...швили" в ', round(len(a)/len(b), 2), 'раза больше, чем "...дзе"')
        elif len(a)==len(b):
            print('Их поровну')
        else:
            print('"...дзе" в ', round(len(b)/len(a), 2), 'раза больше, чем "...швили"')
        print('Количество "...ия": ', len(c))

def changing(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = re.sub('>([А-Я]......+?)( [А-Я].+? [а-яА-Я]+?дзе<)', '>Галактион\\2', text)
        text = re.sub('>([А-Я]......+?)( [А-Я].+? [а-яА-Я]+?швили<)', '>Галактион\\2', text)
    with open('result.html', 'w', encoding = 'utf-8') as g:
        g.write(text)

def main():
    return searching('georgia.html'), changing('georgia.html')

if __name__=='__main__':
    main()
