# Домашнее задание по теме "Логирование"
# Цель: получить опыт использования простейшего логирования совместно с тестами.
#
# Задача "Логирование бегунов":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное
# значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
# Уровень - INFO
# Режим - запись с заменой('w')
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
# "Неверная скорость для Runner".
# test_run:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте что-то кроме строки в name.
# В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
# "Неверный тип данных для объекта Runner".
# Пример результата выполнения программы:
# Пример полученного файла логов runner_tests.log:

import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            run1 = Runner('Вася', -7)
            for i in range(1, 11):
                run1.walk()
            self.assertEqual(run1.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            run2 = Runner(2, 10)
            for i in range(1, 11):
                run2.run()
            self.assertEqual(run2.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        r3 = Runner('Bob')
        r4 = Runner('Ted')
        for i in range(1, 11):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8')
