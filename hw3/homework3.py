word = list(input("Enter a word: "))
f = 0
l = len(word)
while (f < l):
    print (''.join(word[f:l]))
    f = f + 1
    l = l - 1
