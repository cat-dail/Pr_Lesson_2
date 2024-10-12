# Цель: понять как работают потоки на практике, решив задачу
#
# Задача "Потоковая запись в файлы":
# Необходимо создать функцию write_words(word_count, file_name), где word_count -
# количество записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
# с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
# 10, example1.txt
# 30, example2.txt
# 200, example3.txt
# 100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 10, example5.txt
# 30, example6.txt
# 200, example7.txt
# 100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков.
# Как это сделать рассказано в лекции к домашнему заданию.
#
# Пример результата выполнения программы:
# Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# # Взятие текущего времени
# # Создание и запуск потоков с аргументами из задачи
# # Взятие текущего времени
# # Вывод разницы начала и конца работы потоков
# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
#
# Записанные данные в файл должны выглядеть так:
#
#
# Примечания:
# Не переживайте, если программа выполняется долго, учитывая кол-во слов,
# максимальное время выполнения в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
# Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt,
# т.к. потоки работали почти одновременно.


from threading import Thread
from datetime import datetime
from time import sleep


# time_start = datetime.now()


def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1} \n')
        sleep(0.1)
    file.close()
    print(f'"Завершилась запись в файл {file_name}".')


time_start = datetime.now()
a1 = write_words(10, 'example1.txt')
a2 = write_words(30, 'example2.txt')
a3 = write_words(200, 'example3.txt')
a4 = write_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'Суммарное время {time_res}')

time_start1 = datetime.now()
t_first = Thread(target=write_words, args=(10, 'example5.txt'))
t_thr = Thread(target=write_words, args=(200, 'example7.txt'))
t_sek = Thread(target=write_words, args=(30, 'example6.txt'))
t_quv = Thread(target=write_words, args=(100, 'example8.txt'))


t_sek.start()
t_thr.start()
t_first.start()
t_quv.start()


t_first.join()
t_sek.join()
t_thr.join()
t_quv.join()
time_end1 = datetime.now()

time_res1 = time_end1 - time_start1
print(f'Работа потоков {time_res1}')

#
