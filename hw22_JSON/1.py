import json
import re


def task1(path):
    with open(path, 'r+') as f:
        data = f.read()
    json_string = json.loads(data)

    # вывожу имя и планету
    print(json_string['name'] + '\n' + json_string['origin']['name'])

    # вывожу все эпизоды с участием рика (ура, регулярки!!!))
    print(f'Эпизоды с участием:')

    for i in json_string["episode"]:
        match = re.findall(r'\d+', i)
        print(match[0])


task1('/home/sirius/minikaeva_repo/hw22_JSON/character.json')
