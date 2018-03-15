import re

def sentences(filename):
    s = []
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        sents = text.split('. ')
        for sent in sents:
            s.append(sent)
    return s

def searching(a):
    for sent in a:
        if re.search('(18[0-9][0-9])|( [0-9][0-9] (я|ф|м|а|и|с|о|н|д))',sent):
            print(sent,'\n')

def main():
    print(searching(sentences('war.txt')))

if __name__=='__main__':
    main()
