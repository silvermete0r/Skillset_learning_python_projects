# Полиморфизм - это способность объекта использовать методы производного класса, который не существует на момент создания базового класса. 

class Instrument:
    def play(self):
        raise NotImplementedError("Необходимо переопределить метод play() в дочернем классе")

class Kobyz(Instrument):
    def play(self):
        print("Играет қобыз...")

class Jetigen(Instrument):
    def play(self):
        print("Играет жетіген...")

class Dombyra(Instrument):
    def play(self):
        print("Играет домбыра...")

instruments = [Kobyz(), Jetigen(), Dombyra()]

for instrument in instruments:
    instrument.play()
# Играет қобыз...
# Играет жетіген...
# Играет домбыра...


