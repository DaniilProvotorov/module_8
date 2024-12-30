class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, __vin, __numbers, ):
        self.model = model
        self.__vin = __vin
        if self.__is_valid_vin() == False:
            raise IncorrectVinNumber()
        self.__numbers = __numbers
        if self.__is_valid_numbers() == False:
            raise IncorrectVinNumber()




    def __is_valid_vin(self):

        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
            return False
        if self.__vin < 1000000 or self.__vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
            return False
        else: return True

    def __is_valid_numbers(self):
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            return False
        if len(self.__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
            return False
        else: return True


try:
    first = Car('m1', 1001000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else: print(f'{first.model} успещно создан')

try:
    second = Car('m2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else: print(f'{second.model} успещно создан')

try:
    third = Car('m2', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else: print(f'{third.model} успещно создан')