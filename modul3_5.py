# Самостоятельная работа по уроку "Рекурсия"
def get_multipiied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        first = first * get_multipiied_digits(int(str_number[1:]))
        if first == 0:
            return 1
        else:
            return first


result = get_multipiied_digits(40203)
print(result)
