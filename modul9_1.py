# Домашнее задание по теме "Введение в функциональное программирование"
# Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции
# для вызова.


def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        my_res = func(int_list)
        results.update({func.__name__: my_res})
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
