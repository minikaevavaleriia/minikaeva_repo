from CONTROLNAYA.bank import Bank
from CONTROLNAYA.client import Client


def main():
    client1 = Client('101', 'Vitya', '2022-10-10', 20000, 10)
    client2 = Client('102', 'Anya', '2022-10-08', 10000, 8)
    client3 = Client('103', 'Lera', '2022-10-12', 15000, 12)
    client4 = Client('104', 'lol', '2022-10-05', 25000, 5)

    bank = Bank([client1, client2, client3])

    bank.showByProc(8)
    print('-------------------------------------------------------')
    bank.showByMoney(14500)
    print('-------------------------------------------------------')
    bank.showByCode('102')
    print('-------------------------------------------------------')
    bank.addClient(client4)

    print(bank.clientBase[-1])


main()
