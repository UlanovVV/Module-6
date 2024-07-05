""" Создаем родительские классы животных и растений"""
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

""" Создаем классы наследников , где животные будут есть растения"""

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name) #Позволяет использовать родительские классы
       
    def eat(self, food): #""" Логика для еды. Если растение съедобное то меняем статус на накормелен, иначе умираем"""
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб.")

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f"{self.name} съел {food.name}")
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name} и погиб.")


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

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
