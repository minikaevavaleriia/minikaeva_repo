class Client:
    def __init__(self, code, name, date, vklad, procent):
        self.code = code
        self.name = name
        self.date = date
        self.vklad = vklad
        self.procent = procent

    def __str__(self):
        return f'client: {self.name}\n' \
               f'открыл вклад на {self.vklad} под {self.procent}%\n' \
               f'дата: {self.date}\n' \
               f'код: {self.code}\n'
