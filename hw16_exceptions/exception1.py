def task1(l):
    for el in l:
        try:
            print(el / 3)
        except TypeError as e:
            print('Невозможно разделить')


lst = ["Максим",12,14,"Олег","100"]
task1(lst)

