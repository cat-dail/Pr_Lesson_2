# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three


def is_prime(func):
    def wrapper(*nambers):
        sum_func = func(*nambers)
        if sum_func % 2 == 0:
            print("Составное")
        else:
            print("Простое")
        return sum_func
    return wrapper


@is_prime
def sum_three(*nambers):
    a = 0
    for i in nambers:
        a += i
    return a


result = sum_three(2, 3, 6)
print(result)
