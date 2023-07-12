# Композиция - это когда один объект включает в себя другой объект, и при этом первый объект не может существовать без второго.

class CPU:
    def __init__(self, model):
        self.model = model
    def __str__(self):
        return f'CPU model: {self.model}'

class RAM:
    def __init__(self, memory):
        self.memory = memory
    def __str__(self):
        return f'RAM memory: {self.memory}'

class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def __str__(self):
        return f'Computer: {self.cpu} {self.ram}'
    
cpu = CPU('Intel Core i7')
ram = RAM(16)
computer = Computer(cpu, ram)
print(computer) 
# Computer: CPU model: Intel Core i7 RAM memory: 16
