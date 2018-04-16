import os

lst = os.listdir()#можно ('C:/User')
print(type(lst))

os.path.join(dirname, filename) #ставит \ или /
lst = os.listdir(dir1 + os.sep + dir2)
for fn in lst:
    if os.path.isfile(fn):
        f = open(fn)

import shutil

shutil.move(source, destination)
shutil.copy(source, destination)
shutil.remove()
shutil.rmtree() # стереть безвозвратно все содержимое папки
