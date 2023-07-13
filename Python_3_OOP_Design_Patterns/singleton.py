# Синглтон - это порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр,и предоставляет к нему глобальную точку доступа.

# Создаем класс Singleton
class Database:
    _instance = None

    def __init__(self):
        print('Loading database')
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Database()
        return cls._instance

if __name__ == '__main__':
    # Получение экземпляра класса Database
    db1 = Database.get_instance()
    db2 = Database.get_instance()

    # Проверка, что экземпляры одинаковые
    print(db1 is db2) 
    # True

