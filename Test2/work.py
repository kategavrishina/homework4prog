import re
import collections

def first(filename):
    lines = 0
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = re.sub('<text>.+?', ' ', text)
        for line in text:
            lines += 1
        with open('result.txt', 'w', encoding = 'utf-8') as g:
            g.write(lines)
            

def second(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        a = re.findall('<w lemma=".+?" type="(.+?)">', text)
        d = collections.Counter()
        for word in a:
            d[word] += 1
# не знаю, как записать словарь в файл, так что просто принт
        print(dict(d))
        

def third(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        a = re.findall('type="f.h.+?">(.+?)</w>', text)
        a = ', '.join(a)
        with open('result.txt', 'a', encoding = 'utf-8') as h:
            h.write(a)

def main():
    return first('razm.xml'), second('razm.xml'), third('razm.xml')

if __name__=='__main__':
    main()
        
