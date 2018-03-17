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
        r = re.search('(18[0-9][0-9])|([12]?[1-9] (ян|фев|ма|апреля|авгу|ию|сент|окт|ноя|дек)[а-я]+ [12][0-9][0-9][0-9])', sent)
        if r:
            string = r.group()
            print(string)

def main():
    print(searching(sentences('text.txt')))

if __name__=='__main__':
    main()
