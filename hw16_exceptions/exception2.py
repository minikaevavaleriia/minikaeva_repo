def task2(a, b):
    try:
        if type(a) == int and type(b) == int:
            print(a + b)
        else:
            print(a + b)
    except TypeError as e:
        print(e)
        print(str(a) + str(b))


task2(3, '7354')
