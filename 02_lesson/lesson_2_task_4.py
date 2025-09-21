def fizz_buzz(n):
    for i in range(1, n+1):
        if (i % 5 == 0) and (i % 3 == 0):
            print("FizzBuzz")
        elif (i % 5 == 0):
            print("Buzz")
        elif (i % 3 == 0):
            print("Fizz")
        else:
            print(i)


try:
    chislo = int(input("Введите целое число больше 1: "))
    if (chislo > 1):
        fizz_buzz(chislo)
    else:
        print("Число введено неверно.")
except ValueError:
    print("Число введено неверно.")
