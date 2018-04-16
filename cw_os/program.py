import os

def cleaning(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        text = f.read()
    sym = "0123456789.,?!…:;()[]-_|/\"'«»*{}<>@#$%^&№"
    s = []
    text = text.strip().split()
    for word in text:
        s.append(word.strip(sym))
    return s

def cut(s):
    if len(s) > 2000:
        parts = (len(s) // 2000) + 3
        for i in range(parts):
            words = ' '.join(s[0+(i-1)*2000:i*2000])
            filename = str(i) + '.txt'
            with open (filename, 'w', encoding = 'utf-8') as g:
                g.write(words)

def main():
    return cut(cleaning("text.txt"))

if __name__=='__main__':
    main()  

