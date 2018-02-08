def reading():
    with open("81A.tab.txt", 'r', encoding='utf-8') as f:
        d = []
        for line in f:
            line = line.split("\t")
            d.append(line[3])
    return d

def dictionary(word_order):
    d = {}
    for word in word_order:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def main(d):
    for word in sorted(d, key = d.get, reverse = True):
        #for key, value in dictionary.items():
            print(word,"\t", d[word])

if __name__ == '__main__':
    main(dictionary(reading()))


    

