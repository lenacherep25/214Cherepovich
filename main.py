import math
print("1 - сложение")
print("2 - умножение")
print("3 - деление")
print("4 - вычитание")
print("5 - квадратное уравнение")

number = int(input())
if number == 1:
    print("введите первое число")
    y = int(input())
    print("введите второе число")
    z = int(input())
    print("результат:")
    print(y+z)
else:
    if number == 2:
        print("введите первое число")
        y = int(input())
        print("введите второе число")
        z = int(input())
        print("результат:")
        print(y * z)
    else:
        if number == 3:
            print("введите первое число")
            y = int(input())
            print("введите второе число")
            z = int(input())
            print("результат:")
            print(y / z)
        else:
            if number == 4:
                print("введите первое число")
                y = int(input())
                print("введите второе число")
                z = int(input())
                print("результат:")
                print(y - z)
            else:
                print('(a*x**2)+(b*x)+c=0')
                print("введите a")
                a = int(input())
                print("введите b")
                b = int(input())
                print("введите c")
                c = int(input())
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




