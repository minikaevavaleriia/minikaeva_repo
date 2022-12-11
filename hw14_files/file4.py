import string
"""
Разработайте программу, которая будет показывать слово (или слова),
чаще остальных встречающееся в текстовом файле(файл для проверки можно ручками создать). Сначала пользователь
должен ввести имя файла для обработки. После этого вы должны открыть
файл и проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в файле вам стоит игнорировать регистры
"""


def remove_symbols_in_file():
    str_punc = string.punctuation
    name_1 = input('Enter first file name: ')
    full_name1 = '/home/sirius/text_files_for_hw/' + name_1
    stack = []

    with open(full_name1, 'r+') as f1:
        for line in f1:
            line_ready = line.split('\n')       # создаю строку без переноса строки
            for words in line_ready:            # в строке без переноса удаляю все пробелы в каждом слове, слова в список
                stack.extend(words.split(' '))

    for i in stack:
        if i == '':
            stack.remove('')    # удаляю остатки от '/n'

    for word in stack:
        for i in range(0, len(str_punc)):
            if word.find(str_punc[i]) != -1:
                correct_word = (stack[stack.index(word)]).replace(str_punc[i], '')  # удаляю пунктуацию
                stack[stack.index(word)] = correct_word

    return stack


def count_same_words(words):
    d = {}

    for w in range(0, len(words)):
        words[w] = words[w].lower()         # все слова делаю с маленькой буквы
        d[words[w]] = words.count(words[w]) # считаю вхождение каждого слова, добавляю в словарь слово-ключ, цифру-значение

    print('Топ повторяющихся слов: ')

    for key, value in d.items():
        if value >= 5:
            print(key, ':', value)  # вывожу топ слов, если слово 5 и более раз встретилось в тексте


count_same_words(remove_symbols_in_file())

