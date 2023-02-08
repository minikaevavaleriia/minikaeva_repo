""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

new_folder = 'task4'
file_name = 'answer.txt'

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

os.system('echo я выполнил задание > task4/answer.txt')
