
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()   # без параметров выводятся по умолчанию значения функции
print_params(b=25)
print_params(c=[1, 2, 3])
print_params([1, 2, 3])  # без распаковки - список  вместо 1 параметра
print_params(*[1, 2, 3])  # с распаковкой замена всех параметров в функции


values_list = [1.25, False, {'a'+'b', 1-3, 'бабах'}]
print_params(*values_list)
values_dict = {'a': True, 'b': [17, 31, 64], 'c': 2.1/7}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print_params(*values_list_2)  # 3 взят по умолчанию из функции


def print_params1(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print_params(**values_dict)
