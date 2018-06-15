import re

def reading(filename):
    with open (filename, 'r', encoding = 'utf-8') as f:
        text = f.readlines()
        return text

def first(t):
        length = 0
        words = 0
        for line in t:
            r = re.search('<w>', line)
            if r:
                words += 1
                lst = re.findall(r'ana', line)
                length += len(lst)
        print('Среднее количество разборов на слово:', round(length/words, 2))

def second(t):
    d = {}
    for line in t:
        r = re.search('gr=\"([A-Z]+)', line)
        if r:
            word = r.group(1)
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    print("\nЧастотный словарь частей речи:")
    for word in sorted (d, key = d.get, reverse = True):
        print('{}\t{}'.format(word, d[word]))
    

def third(t):
    print("\nСписок слов в творительном падеже с контекстом:\n")
    new_text = []
    allwords = []
    abl = []
    for line in t:
        r = re.search('gr=\"([A-Z]+)', line)
        if r:
            new_text.append(line)
    for line in new_text:
        l = re.search('/>([А-Яа-яёЁ]+)<', line)
        if l:
            string = l.group(1)
            allwords.append(string)
            if re.search('твор', line) and re.search('\"S,', line):
                abl.append(string)
    for word in abl:
        i = allwords.index(word)
        print(' '.join(allwords[i-3:i]), word, ' '.join(allwords[i+1:i+4]))

def main():
    first(reading('karenina.xml'))
    second(reading('karenina.xml'))
    third(reading('karenina.xml'))

if __name__ =="__main__":
    main()
            
