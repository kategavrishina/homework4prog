f = open("text1.txt", "r", encoding = "utf-8")
lines = 0
longlines = 0
for line in f:
    lines += 1
    words = line.split()
    line_length = len(words)
    if line_length > 5:
        longlines += 1
f.close()
if lines == 0:
    print ("Пустой файл")
else:
    print (round (longlines/lines * 100, 2),"%")
