import os
import re
import csv

doc_id = []
title = []
author = []
created = []
topic = []
tagging = []

def first_0():
    new_lines = []
    d = {}
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path,'r') as f:
                for line in f.readlines():
                    if re.search('content="(.+?)"', line):
                       new_lines.append(line)
                    r = re.search('<title>(.+?)</title>',line)
                    if r:
                        title.append(r.group(1))
    print(title)
    return new_lines

def first_1(new_lines):
    for line in new_lines:
        r = re.search('content="(.+?)" name="docid"', line)
        if r:
            string = r.group(1)
            doc_id.append(string)
        r = re.search('content="(.+?)" name="author"', line)
        if r:
            string = r.group(1)
            author.append(string)
        r = re.search('content="(.+?)" name="created"', line)
        if r:
            string = r.group(1)
            created.append(string)
        r = re.search('content="(.+?)" name="topic"', line)
        if r:
            string = r.group(1)
            topic.append(string)
        r = re.search('content="(.+?)" name="tagging"', line)
        if r:
            string = r.group(1)
            tagging.append(string)
    print(doc_id,author,created,topic,tagging)

def second():
    abbr = []
    big_text = []
    c = {}
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path,'r') as f:
                text = f.readlines()
                for line in text:
                    r = re.search('lex="(.+?)"', line)
                    if r:
                        string = r.group(1)
                        if string.isupper():
                            if string in c:
                                c[string] += 1
                            else:
                                c[string] = 1   
    print(c)
   #не знаю, почему получается словарь только для одного файла         
        
    
def main():
    return first_1(first_0()), second()

if __name__=='__main__':
    main()       

    



        

                        





                         

