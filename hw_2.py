""" a, b = input().split()
a, b = map(float, (a, b))
if b != 0:
    print(a / b)
else:
    print('На ноль делить нельзя') """

""" cost = float(input())
if cost > 20:
    print(round(cost * 0.65, 2), cost - round(cost * 0.65, 2))
else:
    print(cost)"""

num = int(input())
if num not in range(1, 13):
    print('Введите номер месяца')
elif num == 1:
    print('Зима, Январь')
elif num == 2:
    print('Зима, Февраль')
elif num == 3:
    print('Весна, Март')
elif num == 4:
    print('Весна, Апрель')
elif num == 5:
    print('Весна, Май')
elif num == 6:
    print('Лето, Июнь')
elif num == 7:
    print('Лето, Июль')
elif num == 8:
    print('Лето, Август')
elif num == 9:
    print('Осень, Сентябрь')
elif num == 10:
    print('Осень, Октябрь')
elif num == 11:
    print('Осень, Ноябрь')
elif num == 12:
    print('Зима, Декабрь')