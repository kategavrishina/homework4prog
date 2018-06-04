import re

sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
pattern = re.compile(r'([А-Я]((т.п.|т.д.|пр.|г.)|[^?!.\(]|\([^\)]*\))*[.?!])')

def sents(filename):
    sents = []
    res = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
        text = text.replace('\n',' ')
        for _,sent in enumerate(pattern.findall(text)):
            sents.append('{}'.format(sent[0]))
        for sent in sents:
            sent_new = re.sub('[0-9]|[\.,\?!…:;—\"\()\/]|( -)','',sent)
            res.append(sent_new)
    return res

def words(res):
    d = {}
    r = {}
    i = 1
    for sent in res:     
        words = sent.lower().split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1   
        r = {k:v for k, v in d.items() if v > 1}
        if r:
            print("Предложение: \"" + sent + "\"")
            for key, value in r.items():
                print('{}{:^15}'.format(key,value))
        dict.clear(d)
        dict.clear(r)

def main():
    words(sents('text1.txt'))

if __name__=='__main__':
    main()
        
