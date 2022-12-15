"""
Сохраните данные из списка в json файл(Имя файла - ваша фамилия и номер задания) с отступом 4, формата:
name: ***
age: ***
countries: [
{
name:***
time:***
cities:***
}
]
"""
import json

task = ["oleg",24,["Belarus","Russia"],(24,1),["Moscow","Vladikavkaz",'Krasnodar',"Rostov","Nalchik"]]
s = ['name', 'age', 'countries', 'name', 'time', 'cities']

d = {}
for i in range(2):
    d[s[i]] = task[i]

d[s[2]] = {}

k = 0
for i in range(3, 6):
    d[s[2]][s[i]] = task[i - 1]



print(d)
encoded = json.dumps(d, indent=4)

with open('/home/sirius/minikaeva_repo/hw22_JSON/minikaeva_3.json', 'w+') as f:
    f.write(encoded)

