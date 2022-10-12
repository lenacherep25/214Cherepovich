import math
def sun(a, b, c, d, e):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
sun("1 - сложение",
    "2 - умножение",
    "3 - деление",
    "4 - вычитание",
    "5 - квадратное уравнение" )

x = int(input("ввод первого числа: "))
y = int(input("ввод второго числа: "))
number = int(input("ввод операции: "))

while True:
    if number == 1:
        f = x + y
        print(f)
    elif number == 2:
        f = x * y
        print(f)
    elif number == 3:
        f = x / y
        print(f)
    elif number == 4:
        f = x - y
        print(f)
    elif number == 5:
        print('(a*x**2)+(b*x)+c=0')
        a = int(input())
        b = int(input())
        c = int(input())
        def stay(a, b, c):
            print(a)
            print(b)
            print(c)
            D = b**2 - 4 * a * c
            print("дискриминант:")
            print(D)
            if D > 0:
                x1 = (- b + math.sqrt(D)) / (2 * a)
                x2 = (- b - math.sqrt(D)) / (2 * a)
                print("x1,x2:")
                print(x1,x2)
            else:
                if D == 0:
                    x1 = -b / 2 * a
                    print("x1:")
                    print(x1)
                else:
                    print("корней нет")
        continue
    else:
        break

