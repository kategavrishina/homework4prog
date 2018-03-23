#Вариант 7 (сидеть)

import re

def reading(filename):
    sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
    s = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                s.append(word.strip(sym))
    return s

def searching(a):
    b = []
    for word in a:
        if re.search('^си(жу|(д((е(ть|л(а|и|о)?|вш))|(я(т|ч|щ)?)|(и(м|т|шь)?))))',\
                     word) and word not in b:
            b.append(word)
    print(' '.join(b))
        
def main():
    print(searching(reading('sit.txt')))

if __name__=='__main__':
    main()
