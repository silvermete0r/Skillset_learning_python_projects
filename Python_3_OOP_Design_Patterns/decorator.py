# Декоратор - это функция, которая принимает функцию и возвращает функцию.

# Создаем декоратор
def uppercase_decorator(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper


@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"


# Вызов функции с применением декоратора
result = greet("Alikhan")
print(result)  # "HELLO, ALIKHAN!"

