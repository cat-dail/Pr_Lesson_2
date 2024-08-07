#  Задача "Счётчик вызовов"
calls = 0


def count_calls():  # счетчик
    global calls
    calls = calls + 1


def string_info(string):  # Преобразование строки в кортеж
    tuple1 = len(string), string.upper(), string.lower()
    count_calls()
    return tuple1


def is_contains(string, list_to_search):  # поиск слова в строке
    string = string.upper()
#  В списке все строки в верхний регстр (ф-ция map для всех элементов без иcпользования for)
    list_to_search = list(map(str.upper, list_to_search))
    count_calls()
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
