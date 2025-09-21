def is_year_leap(year):
    return False if year % 4 else True


try:
    year = int(input("Введите год: "))
    result = is_year_leap(year)
    print(f"Год {year}: {result}")
except ValueError:
    print("Год введён неверно.")
