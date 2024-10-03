class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model: str, vin: int, number: str):
        self.model = model
        self.__vin = vin
        self.__number = number
        self.__is_valid_vin(vin)
        self.__is_valid_numbers(number)

    @staticmethod
    def __is_valid_vin(vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if vin > 9999999 or vin < 1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin

    @staticmethod
    def __is_valid_numbers(number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return number


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
