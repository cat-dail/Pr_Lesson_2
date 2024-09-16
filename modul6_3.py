# Цель: закрепить знания множественного наследования в Python.
# Задача "Мифическое наследование":
##При конструировании объекта(__init__) можно(иногда нужно) не указывать аттрибуты, которым далее
##будут присвоены конкретные значения (self.x_distance, self.sound)
# Примечания:
# Будьте внимательней, когда вызываете методы классов родителей
# в классе наследнике при множественном наследовании: при обращении через super()
# методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
# Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat",
# т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.Horse
class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):  # - где dx и dy
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
       return ((self.x_distance),(self.y_distance))

    def voice(self):
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
