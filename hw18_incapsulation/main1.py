from hw18_incapsulation.task1 import Account


def main():
    account = Account('lera', 700, '123456', 'qwerty')
    account.set_passport('098765', 'lol')
    account.set_passport('098765', 'qwerty')
    account.change_balance(300)
    account.change_balance(-5000)
    try:
        account.del_passport('qwerty')
    except:
        print('Паспорт был удален!!!')


main()
