from math import *


# 1
result = 0
for i in range(16, 25):
    result += i
print(result)


# 2
num1 = int(input(' '))
num2 = int(input(' '))
print(num1 + num2)


# 3
def positive_to_negative(positive):
    print(255 - positive)

positive_to_negative(int(input()))


# 4
my_list = []
for i in range(0, 3):
    my_list.append(int(input()))
print(sum(my_list), max(my_list), min(my_list))


# 5
num1 = int(input())
num2 = int(input())
print(abs(num1 - num2))


# 6
rub_to_dollar = float(input())
dollar_to_euro = float(input())
print(round(1 / dollar_to_euro / rub_to_dollar, 2))


# 7
budget = 1572
price = int(input())
print(budget // price)


# 8
number = int(input())
print(number % 10 + (number // 10) % 10 + ((number // 10) // 10) % 10)


# 9
number = int(input())
print(number % 10)
print((number // 10) % 10)
print(((number // 10) // 10) % 10)


# 10
seconds = int(input())
print(seconds / (60 * 60 * 24 * 365))


# 11
kg = float(input())
height = float(input())
print(round(((kg / (height ** 2)) * 10000), 2))


# 12

s, l = float(input()), float(input())
plos = s * l
u = float(input())
v = int(input())
pro = int(input())
litr = (plos / u) * pro / 100 + plos / u
print(round(plos, 2))
print(round(litr, 2))
print(int(litr // v + 1))
print(round(v - (litr - int(litr)), 2))

