import math


def square(a):
    return a**2


b = input("Введите дилну стоороны квадрата: ")
try:
    b = math.ceil(float(b))
    result = square(b)
    print(f"Площадь квадрата со стороной {b} = {result}")
except ValueError:
    print("Введено неверное число.")
