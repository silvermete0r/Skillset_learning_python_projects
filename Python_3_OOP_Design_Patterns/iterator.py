# Итератор - это поведенческий паттерн проектирования, который даёт возможность последовательно обходить элементы составных объектов, не раскрывая их внутреннего представления.

# Создаем класс итератора
class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result
    
if __name__ == '__main__':
    # Тестовый список
    fruits = ['cherry', 'banana', 'grapes', 'pear']
    # Создание итератора для списка данных
    my_iter = Iterator(fruits)
    # Итерация по элементам итератора
    for it in my_iter:
        print(it)
    # cherry banana grapes pear


