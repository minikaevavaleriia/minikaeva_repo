"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""

from multiprocessing import Process, Pipe
import time

def currency(conn, n):
    conn.send(n)
    conn.close()

if __name__ == '__main__':
    parent_conf, child_conf=Pipe()
    p1=Process(target=currency, args=(child_conf, 75))
    time.sleep(1)
    p1.start()
    print(parent_conf.recv())