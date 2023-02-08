"""
Создайте программу выводящую информацию о системе вида:
Операционная система - ХХХ
Имя компьютера - ХХХ
Имя пользователя - ХХХ
"""

import os
import socket

print(os.name)
print(socket.gethostname())
print(os.getlogin())

