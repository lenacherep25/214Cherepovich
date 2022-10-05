from random import randint

spisok = []
min = 0
plus = 0
x = 0
while x < 15:
    x = x + 1
    y = randint(-100, 100)
    if y == 0:
        while y == 0:
            y = randint(-100, 100)
    if y < 0:
        min = min + y
    else:
        plus = plus + y
    spisok.append(y)
print("15 случайных чисел:", spisok)
print("сумма отрицательных:", min)
print("сумма положительных:", plus)