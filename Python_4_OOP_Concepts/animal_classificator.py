class Animal:
    def __init__(self, name):
        self.name = name

    def get_type(self):
        return "Животное"

    def get_info(self):
        return f"Это {self.get_type()}. Имя: {self.name}"


class Mammal(Animal):
    def get_type(self):
        return "Млекопитающее"

    def get_info(self):
        return f"Это {self.get_type()}. Имя: {self.name}. Они дают молоко."


class Bird(Animal):
    def get_type(self):
        return "Птица"

    def get_info(self):
        return f"Это {self.get_type()}. Имя: {self.name}. Они могут летать."


class Reptile(Animal):
    def get_type(self):
        return "Рептилия"

    def get_info(self):
        return f"Это {self.get_type()}. Имя: {self.name}. Они имеют чешуйки."


animals = [Mammal("Лев"), Bird("Орел"), Reptile("Крокодил")]

for animal in animals:
    print(animal.get_info())
