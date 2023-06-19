# Подключение необходимых модулей и зависимостей
from flask import Flask, render_template, request, redirect
import json
import requests

# Инициализация Flask на данный модуль
app = Flask(__name__)

# Функция для загрузки данных пользователей из JSON файла
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
# Функция для сохранения данных новых пользователей в JSON файл
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file) 

# Словарь - временное хранилище данных пользователей + форматирование для JSON файла
users = load_users()

# Endpoint (Точка подключения) ссылка по умолчанию ведет на web-страницу: login.html
@app.route('/')
def index():
    return render_template('login.html')

# Endpoint: ссылка '/register' ведет к: register.html
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        phone = request.form.get('phone')

        if username and password:
            if username not in users:
                data = {"fullname": fullname, "email": email, "phone": phone, "password": password}
                users[username] = data
                save_users(users)
                return redirect('/login')
            else:
                error = 'Username already exists!'
                return render_template('register.html', error=error)

    return render_template('register.html')

# Endpoint: ссылка '/login' ведет к: register.html
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            if username in users and users[username]['password'] == password:
                url = 'https://api.chucknorris.io/jokes/random'
                response = requests.get(url)
                data = response.json()
                joke = data['value']
                return render_template('welcome.html', username=username, fullname=users[username]['fullname'], email=users[username]['email'], phone=users[username]['phone'], joke=joke)
            else:
                error = 'Invalid username or password!'
                return render_template('login.html', error=error)

    return render_template('login.html')

# Запуск приложения на локальном сервере (по умолчанию: http://127.0.0.1:5000/)
if __name__ == '__main__':
    app.run(debug=True)
