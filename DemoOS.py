#DemoOS.py
#os.path를 사용하는 데모
from os.path import *
import os

fName= "c:\\python310\\python.exe"
print(abspath("python.exe"))
print(basename(fName))

if exists(fName):
    print(fName, "존재합니다.")
    print("파일크기:", getsize(fName))
else:
    print(fName,"존재하지 않습니다.")

print("운영체제명:", os.name)
os.system("notepad.exe")

import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))


import glob
print("파일리스트")
print(glob.glob("*.py"))
for item in glob.glob("*.py"):
    print(item)
    