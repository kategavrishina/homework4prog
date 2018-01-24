#Вариант 7
#Танка вида:
#Рыжий мальчишка
#Начеркал свой первый стих:
#И в тёмном лесу,
#Где конь бы заплутал,
#Олень благородный кричит.
import random

def noun1():
    f = open("noun1.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1]

def adj1(word):
    f = open("adj1.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1] + " " + word

def verb_transitive(obj):
    f = open("verb_tr.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1] + " " + "свой" + " " + obj

def adj2():
    f = open("adj2.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1]

def noun2(adj):
    f = open("noun2.txt", "r", encoding="utf-8")
    return adj + " " + random.choice([line for line in f])[:-1]

def adj3():
    f = open("adj3.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1]

def noun3(adj):
    f = open("noun3.txt", "r", encoding="utf-8")
    return adj + " " + random.choice([line for line in f])[:-1]

def subj1():
    f = open("subj1.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1]

def verb1(subj):
    f = open("verb1.txt", "r", encoding="utf-8")
    return subj + " бы " + random.choice([line for line in f])[:-1]


def adj4():
    f = open("adj4.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1]

def subj2(adj):
    f = open("subj2.txt", "r", encoding="utf-8")
    return random.choice([line for line in f])[:-1] + " " + adj

def verb2(subj):
    f = open("verb2.txt", "r", encoding="utf-8")
    return subj + " " + random.choice([line for line in f])[:-1]

def random_sentence():
    sentence = adj1(noun1()) + "\r\n" + verb_transitive(noun2(adj2())) + ":" + "\r\n" + "И в " + noun3(adj3()) + "," + "\r\n" + "Где" + " " + verb1(subj1()) + "," + "\r\n" + verb2(subj2(adj4())) + "."
    return sentence

print(random_sentence())
