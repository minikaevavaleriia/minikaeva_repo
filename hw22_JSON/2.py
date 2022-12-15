"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: ***
"""
import json

task_ = ["oleg",24,["Belarus","Russia"]]

s = ['name', 'age', 'countries']
def task2(task):

    d = {}
    for i in range(len(task)):
        d[s[i]] = task[i]
    encoded = json.dumps(d, indent=4)

    with open('/home/sirius/minikaeva_repo/hw22_JSON/minikaeva_2.json', 'w+') as f:
        f.write(encoded)


task2(task_)