import re
import collections

def first(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = re.sub('<text>.+?', ' ', text)
        with open('newtext.txt', 'w', encoding = 'utf-8') as g:
            g.write(text)

def second(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        a = re.findall('<w lemma=".+?" type="(.+?)">', text)
        d = collections.Counter()
        for word in a:
            d[word] += 1
        with open('newtext.txt', 'a', encoding = 'utf-8') as h:
            for word in d:
                line = word + '\t' + d[word] + '\n'
                h.append(line)

def main():
    return second('razm.xml')

if __name__=='__main__':
    main()
