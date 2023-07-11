# Наследование - это способность класса наследовать методы и атрибуты другого класса.

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")
    
    def send_message(self, phone_number, message):
        print(f"Sending {message} to {phone_number}...")

class Smartphone(Phone):
    def __init__(self, brand, model, color, os):
        super().__init__(brand, model)
        self.color = color
        self.os = os
    
    def browser_internet(self, url):
        print(f"Browsing {url}...")
    
    def play_music(self, song):
        print(f"Playing {song}...")

# Создаем экземпляры классов
phone = Phone("Nokia", "1100")
smartphone = Smartphone("Apple", "iPhone 12", "black", "iOS")

# Вызываем методы классов
phone.make_call("+123456789") # Calling +123456789...
smartphone.make_call("+123456789") # Calling +123456789...

phone.send_message("+123456789", "Hello!") # Sending Hello! to +123456789...
smartphone.send_message("+123456789", "Hello!") # Sending Hello! to +123456789...

smartphone.browser_internet("https://skillset.edu.kz") # Browsing https://skillset.edu.kz...
smartphone.play_music("Қайрат Нұртас: Universe") # Playing Қайрат Нұртас: Universe

