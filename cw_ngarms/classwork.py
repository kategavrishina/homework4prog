def reading(filename):
    sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
    s = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                s.append(word.strip(sym))
    return s

def ngrams(s):
    ngrams = []
    n = int(input('Введите число от 2 до 4: '))
    for i in range(len(s) - 1):
        if n == 2:
            gram = str(s[i]) + ' ' + str(s[i+1])
            ngrams.append(gram)
        elif n == 3:
            gram = str(s[i]) + ' ' + str(s[i+1]) + ' ' + str(s[i+2])
            ngrams.append(gram)
        elif n == 4:
            gram = str(s[i]) + ' ' + str(s[i+1]) + ' ' + str(s[i+2]) + ' ' + str(s[i+3])
            ngrams.append(gram)
    return ngrams
    
def dictionary(ngrams):
    d = {}
    for gram in ngrams:
        if gram in d:
            d[gram] += 1
        else:
            d[gram] = 1
    return d

def main(d):
    lst = []
    with open('result.txt', 'w', encoding = 'utf-8') as g:
        for word in sorted(d, key = d.get, reverse = True):
            lst.append(word + "\t" + str(d[word]))
        g.write('\n'.join(lst))

if __name__=='__main__':
    main(dictionary(ngrams(reading('text.txt'))))
