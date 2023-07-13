class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'{self.name} - {self.price}'

# Агрегация: Order содержит список объектов Dish в качестве своей части
class Order:
    def __init__ (self):
        self.dishes = []
        self.total_cost = 0

    def add_dish(self, dish):
        self.dishes.append(dish)
        self.total_cost += dish.price

    def remove_dish(self, dish):
        self.dishes.remove(dish)
        self.total_cost -= dish.price
    
    def __str__(self):
        return f'{self.dishes} - {self.total_cost}'

# Композиция: Table владеет объектом Order в качестве своей части
class Table:
    def __init__(self, number):
        self.number = number
        self.current_order = None

    def create_order(self):
        self.current_order = Order()

    def add_dish_to_order(self, dish):
        if self.current_order:
            self.current_order.add_dish(dish)

    def remove_dish_from_order(self, dish):
        if self.current_order:
            self.current_order.remove_dish(dish)    
    
    # Ассоциация: Table имеет возможность получить информацию о своем заказе
    def display_order(self):
        print(f'Table {self.number}:')
        print(' - Dishes: ', end='')
        if self.current_order:
            print()
            for dish in self.current_order.dishes:
                print(f'     {dish.name}: {dish.price}$')
        else:
            print('No order')
        print(' - Total cost: ' + (str(self.current_order.total_cost) if self.current_order else 'No order'))

    def __str__(self):
        return f'{self.number} - {self.current_order}'

# Агрегация: Restaurant содержит список объектов Table в качестве своих частей
class Restaurant:
    def __init__(self):
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def __str__(self):
        return f'{self.tables}'

# Создание объектов и установка связей между ними
dish1 = Dish('Burger', 10)
dish2 = Dish('Pizza', 15)

table1 = Table(1)
table2 = Table(2)
restaurant = Restaurant()

restaurant.add_table(table1)
restaurant.add_table(table2)

table1.create_order()
table1.add_dish_to_order(dish1)
table1.add_dish_to_order(dish2)

# Вывод информации о заказах в ресторане
for table in restaurant.tables:
    table.display_order()

