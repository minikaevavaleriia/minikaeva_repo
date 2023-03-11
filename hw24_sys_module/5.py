"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import sys

input_ = sys.stdin

with open(str(input_), 'w+') as f:
    for i in f.readlines():
        sys.stdin