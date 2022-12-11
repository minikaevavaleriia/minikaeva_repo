import re


# 1
str1 = input()
str2 = input()
print(str1 + str2)


# 2
num = int(input())
print('r' * num)


# 3
str1 = input()
print(str1[::-1])


# 4
str0 = input(' ')
answer = str0.split(' ')
print(answer[1], answer[0])


# 5
str0 = input(' ')
print(str0.split('@')[0])


# 6
str0 = input()
print(str0.split('+7')[1][0:3])


# 7
full_name = input()
print(full_name.split(' ')[0] + ' ' + full_name.split(' ')[1][0:1] + '. ' + full_name.split(' ')[1][0:1] + '.')


# 8 (1 решение - крейзи мод)
# test string  - исторический процесс атлантический океан динамическая приколюха


def make_correct_sentence(str0):
    word_list = str0.split(' ')
    result = {}
    result_to_string = ''
    substr1 = 'ический'
    substr2 = 'ическая'
    for i in range(len(word_list)):
        if word_list[i].endswith(substr1) or word_list[i].endswith(substr2):
            result[i] = word_list[i][0:len(word_list[i]) - len(substr1)] + '.'
        else:
            result[i] = word_list[i]
    for i in range(len(result)):
        result_to_string += result[i] + ' '
    print(result_to_string)


make_correct_sentence(input())


# 8 (2 решение - find + replace мод)
str0 = input()
result = ''
substr1 = 'ический'
substr2 = 'ическая'
if (str0.find(substr1) == -1) and (str0.find(substr2) == -1):
    buffer = str0
if str0.find(substr1) != -1:
    buffer = str0.replace(substr1, '.')
if buffer.find(substr2) != -1:
    result = buffer.replace(substr2, '.')
print(result)

#9
# test string - --исторический процесс -- атлан--тический океан-- --динамическа--я приколюха--
str0 = input()
print(str0.replace('--', '—'))

# 10
# test string - 8(999)-123-12-12
def no_symbols(number):
    prohibited_list = [' ', '-', '(', ')']
    for symbol in number:
        if symbol in prohibited_list:
            number = number.replace(symbol, '')
    print(number)


no_symbols(input())


# 11
number = input()
sample = '<a href="tel:"></a>'
index1 = sample.find('">')
index2 = sample.find('</a>')
result = sample[:index1] + number + sample[index1:index2] + number + sample[index2:]
print(result)


# 12
str0 = input()
result = re.findall(r'\d+', str0)
new_str = ''
for i in range(len(result)):
    new_str += result[i]
change_last_character = int(new_str) + 1
print(change_last_character)


# 13
# test string - djkfhsjd jfb@ejfbw 34.23 4fjbj wdc GUJJB jbj minikaeva@mail.ru kcfds JBk. !! @@
str0 = input()
result = re.findall(r'\b\w+@\w+\.\w+\b', str0)
print(result)

