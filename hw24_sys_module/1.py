import sys

input_ = sys.argv

if not '--name' in input_:
    print('Привет мир')
else:
    name = ''
    for i in input_:
        if i == '--name':
            name = input_[input_.index(i) + 1]
    print(f'Привет, {name}')

