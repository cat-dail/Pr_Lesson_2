# Домашнее задание по теме "Зачем нужно наследование"
# Цель: применить базовые знания о наследовании классов для решения задачи
# Примечания:
# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться
# к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.
class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.ebidle is False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

        if food.ebidle is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    ebidle = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    ebidle = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
