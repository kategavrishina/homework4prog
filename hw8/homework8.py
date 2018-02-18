import random

def words(filename):
    d = {}
    with open(filename,'r',encoding = 'utf-8') as f:
        for line in f:
            word, d[word] = line.strip().split(',')
    return d

def game(d):
    y = []
    n = []
    with open('true.txt','r',encoding = 'utf-8') as yes:
        for line in yes:
            y.append(line.strip())
    with open('false.txt','r',encoding = 'utf-8') as no:
        for line in no:
            n.append(line.strip())
    print('Вам будет предложена подсказка в виде прилагательного,\nк которому надо подобрать существительное.\n')
    start = input('Если хотите сыграть, нажмите Enter.')
    while start == '':
        key = random.choice(list(d))
        print(d[key], '...')
        answer = input('Ваш ответ: ')
        if answer.lower() == key.lower():
            print(random.choice(y), '\n')
            start = input('Если хотите сыграть, нажмите Enter.')
        else:
            while answer.lower() != key.lower():
                print(random.choice(n))
                answer = input('Ваш ответ: ')
                if answer.lower() == key.lower():
                    print(random.choice(y), '\n')
                    start = input('Если хотите сыграть, нажмите Enter.')

def main():
    print(game(words('words.csv')))

if __name__ == '__main__':
    main()
