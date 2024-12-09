# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
#
# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователей.
#
#
#
# Пример результата выполнения программы:
# Выполняемый код:
# # Код из предыдущего задания
# # Удаление пользователя с id=6
# # Подсчёт кол-ва всех пользователей
# # Подсчёт суммы всех балансов
# print(all_balances / total_users)
# connection.close()
#
# Вывод на консоль:
# 700.0
import sqlite3

# Подключение к итоговой базе из предыдущего задания 14_1:
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute(" SELECT SUM(balance) FROM Users ")
all_balances = cursor.fetchone()[0]
cursor.execute(" SELECT COUNT (*) FROM Users")
total_users = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
