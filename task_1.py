# Стоимость строки:

while True:
    text = input("Введите текст для подсчета стоимости: ")
    line_cost = len(text) * 60
    rubles = line_cost // 100
    coins = line_cost % 100

    print(f"Результат: {rubles} p. {coins} коп.")

