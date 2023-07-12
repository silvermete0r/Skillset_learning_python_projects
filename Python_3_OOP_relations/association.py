# Ассоциация - это отношение между классами, которое позволяет одному объекту использовать другой, как часть самого себя.

class Car:
    def __init__(self, engine):
        self.engine = engine
    
    def start(self):
        self.engine.start()

class Engine:
    def start(self):
        print("Запуск двигателя")

engine = Engine()
car = Car(engine)
car.start() # Запуск двигателя