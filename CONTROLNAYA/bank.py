class Bank:
    def __init__(self, clientBase):
        self.clientBase = clientBase

    def addClient(self, client):
        self.clientBase.append(client)

    def showByMoney(self, money):
        if self.clientBase:
            for cl in self.clientBase:
                if cl.vklad > money:
                    print(cl)
        else:
            print('Пока вообще нет клиентов')

    def showByCode(self, code):
        for cl in self.clientBase:
            if cl.code == code:
                print(cl)
            # else:
            #     print('нет такого клиента')


    def showByProc(self, proc):
        for cl in self.clientBase:
            if cl.procent > proc:
                print(cl)
            else:
                print('нет такого клиента')

