with open("Extinct_languages.tsv", encoding="utf-8") as f:
    text = f.readlines()
    #1
    for line in text:
        l = len(line)
        if l > 35:
            print(line, "(",l,")", sep = '')
    #2
    num = 0
    for line in text:
        if "Critically endangered" in line:
            num += 1
    print(num)

            
