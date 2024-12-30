def personal_sum(numbers):
    results = 0
    incorrect_data = 0
    try:
        for i in numbers:
            results += i
    except TypeError as exc:
        incorrect_data += 1
    return ((results, incorrect_data))

def calculate_average(numbers):
    personal_sum(numbers)
    try:
        x = personal_sum(numbers)[0]
        print(x/len(numbers))
    except ZeroDivisionError as exc:
        print(f'нас пытались обмануть, но мы знаем, что проблема в: {exc}')
    except TypeError as val:
        print('В numbers записан некорректный тип данных')





print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
