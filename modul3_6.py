#  data_structure это данные, состоящие из:
#  [1, 2, 3] - Список(list)
#  {'a': 4, 'b': 5} - Словарь(dict)
#  (6, {'cube': 7, 'drum': 8}) Кортеж (Число(int) и словаря(diсt)
# "Hello" - строка(str)
# ((), [{(2, 'Urban', ('Urban2', 35))}]) \Cписок в котором: 1.параметр пустой кортеж
# 2. Список(list) из множества(set) кортежа(tuple), в котором: число(int),
# строка(str) и кортеж(в кортеже)(строки и число)
#  Складываем элементв во всех переданных объемных данных(списки кортежи и множетво)

def calculate_structure_sum(data_structure):
    result = 0
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            result += calculate_structure_sum(item)
    elif isinstance(data_structure, str):
        result += len(data_structure)
    elif isinstance(data_structure, int):
        result += data_structure
    elif isinstance(data_structure, dict):
        for key, values in data_structure.items():
            result += calculate_structure_sum(key) + calculate_structure_sum(values)
    return result


data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  'Hello', ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
