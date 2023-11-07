# Зодиак:

year = int(input("Введите год: "))

animals = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]

animal_index = (year - 2000) % 12
animal = animals[animal_index]

print(animal)
