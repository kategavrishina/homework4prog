phrase = input ("Введите слово или фразу на английском: ")
phrase = phrase.lower().split()
end = "ay"
#для слов на гласную (по правилу)
extraend = "way"
vowels = ['a','e','i','o','u','y']
for word in phrase:
    first = word[0]
    if first in vowels:
        word = word + extraend
        print (word, end = " ")
    else:
        word = word[1:] + first + end
        print (word, end = " ")

        
