import re

def reading(filename):
    sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
    s = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                s.append(word.strip(sym))
    return s

def searching(s):
    for word in s:
        r = re.search('^([цкнгшщзхфвпрлджчсмтб]([аяэеыиуюо])([цкнгшщзхфвпрлджчсмтб]\\2)+)$', word)
        if r:
            string = r.group()
            print(string)

def main():
    print(searching(reading('text.txt')))

if __name__=='__main__':
    main()
