with open("Extinct_languages.tsv", encoding="utf-8") as f:
    text = f.readlines()
    for line in text:
        line = line.split("\t")
    lang = input("Введите язык: ")
    while lang:
        for line in text:
            if lang == line[0]:
                print(line[0],"-",line[1],"-",line[2])
            else:
                print("Такого языка нет")
            lang = input("ВВедите язык: ")
    
