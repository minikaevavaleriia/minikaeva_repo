"""
Напишите программу которая автоматически собирает ваше расписание в Элжуре. и сохраняет в json файл в виде:
{день недели: {Предмет: Аудитория}
"""
import json

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

binary = FirefoxBinary('/home/sirius/.mozilla/firefox/gwi6uqpe.Default')
options = Options()
driver = webdriver.Firefox(firefox_binary=binary)


url = 'https://class.sirius.ru/authorize'
driver.get(url)

content = driver.find_element(by='inputiyfemonOI-S').text
parsed_json = json.loads(content)
print(parsed_json)