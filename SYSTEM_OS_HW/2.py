"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""

import os

newpath = r'target'
if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in range(1, 11):
    if not os.path.exists(newpath + r'/' + str(i)):
        os.makedirs(newpath + r'/' + str(i))