# Задача "Developer - не только разработчик":
class House:
    def __init__(self, name, number_of_floors):
        self.name = 'ЖК Эльбрус'
        self.number_of_floors = 30
        self.name = name
        self.number_of_floors = number_of_floors
        self.say_info()

    def say_info(self):
        print(f'Название: {self.name}, этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
