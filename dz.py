import math

print("1 задание")

a = int(input("первое число: "))
b = int(input("второе число: "))
c = int(input("третье число: "))

def stitch(a,b,c):
    return min(a,b,c)
print("минимальное число:", stitch(a,b,c))

print("2 задание")

x = int(input("ввод числа: "))

def stitch(x):
    number = 0
    while x > 0:
        number = number + 1
        x = x // 10
    return (number)
print("количество цифр:", stitch(x))

print("3 задание")

N = int(input("ввод числа N: "))

def stitch(N):
    if N == 1:
        return 1
    return N + stitch(N - 1)
print("сумма:", stitch(N))

print("4 задание")

w = int(input("ввод числа: "))

def stitch(w):
    if w == 0:
        return 1
    return stitch(w - 1) * w
print("факториа числа:", w, "равен:", stitch(w))