#  Задача: "Рассылка писем"
def send_email(message, recipient, sender='university.help@gmail.com'):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    a = False
    i = 0
    list_ = (".com", ".ru", ".net")
    for i in range(len(list_)):
        if recipient.endswith(list_) and sender.endswith(list_):
            a = True
    if a is True and '@' in sender and recipient:
        if sender != 'university.help@gmail.com':
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с  адреса", sender,
                  f"на адрес", recipient)
            return
        print(f"Письмо успешно отправлено с адреса ", sender, f"на адрес", recipient)
        return
    else:
        print(f"Невозможно отправить письмо с адреса", sender, f"на адрес", recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
