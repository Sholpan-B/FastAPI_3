# Standard American Convention
number = input("Введите натуральное число: ")

if not number.isdigit():
    print("Введите натуральное число!")
else:
    formatted_number = "{:,}".format(int(number))
    print(formatted_number)
