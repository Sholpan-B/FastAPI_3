# Переворот числа:

number = input("Введите пятизначное или шестизначное натуральное число: ")

if len(number) < 5 or len(number) > 6:
    print("Число должно быть пятизначным или шестизначным!")
elif len(number) == 6:
    reverse_number = number[:-6:-1]
    print(f"{number[0]}{reverse_number}")
else:
    reverse_number = number[:-6:-1]
    print(reverse_number)


