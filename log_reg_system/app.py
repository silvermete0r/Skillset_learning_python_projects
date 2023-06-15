import tkinter as tk
from tkinter import messagebox
import json

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

# Присвоение данных пользователей в словарь
users = load_users()

# Функция для открытия окна регистрации
def open_registration_window():
    registration_window = tk.Toplevel(window)
    registration_window.title("Registration")
    registration_window.geometry("300x200")
    registration_window.configure(bg="#F0F0F0")

    # Метки и поля ввода для формы регистрации
    label_name = tk.Label(registration_window, text="FullName:", bg="#F0F0F0")
    label_name.pack()
    entry_name = tk.Entry(registration_window)
    entry_name.pack()

    label_age = tk.Label(registration_window, text="Age:", bg="#F0F0F0")
    label_age.pack()
    entry_age = tk.Entry(registration_window)
    entry_age.pack()

    label_username = tk.Label(registration_window, text="Username:", bg="#F0F0F0")
    label_username.pack()
    entry_username = tk.Entry(registration_window)
    entry_username.pack()

    label_password = tk.Label(registration_window, text="Password:", bg="#F0F0F0")
    label_password.pack()
    entry_password = tk.Entry(registration_window, show="*")
    entry_password.pack()

    # Функция для регистрации нового пользователя
    def register():
        name = entry_name.get()
        age = entry_age.get()
        username = entry_username.get()
        password = entry_password.get()

        if name and age and username and password:
            if username in users:
                messagebox.showerror("Error", "The username already exists!")
            else:
                users[username] = {
                    'name': name,
                    'age': age,
                    'password': password
                }
                messagebox.showinfo("Success", "Registration was successful!")
                registration_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all the fields!")

    btn_register = tk.Button(registration_window, text="Register", command=register, width=15, bg="#007BFF", fg="white")
    btn_register.pack(pady=10)

# Функция для открытия окна входа
def open_login_window():
    login_window = tk.Toplevel(window)
    login_window.title("Login")
    login_window.geometry("300x150")
    login_window.configure(bg="#F0F0F0")

    label_username = tk.Label(login_window, text="Username:", bg="#F0F0F0")
    label_username.pack()
    entry_username = tk.Entry(login_window)
    entry_username.pack()

    label_password = tk.Label(login_window, text="Password:", bg="#F0F0F0")
    label_password.pack()
    entry_password = tk.Entry(login_window, show="*")
    entry_password.pack()

    # Функция для выполнения входа
    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username and password:
            if username in users and users[username]['password'] == password:
                messagebox.showinfo("Success", "Successfully logged in!")
                login_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid username or password!")
        else:
            messagebox.showerror("Error", "Please enter both your username and password!")

    btn_login = tk.Button(login_window, text="Login", command=login, width=15, bg="#DC3545", fg="white")
    btn_login.pack(pady=10)

# Функция для выхода из программы
def exit_program():
    save_users(users)
    window.destroy()

# Создание главного окна Tkinter
window = tk.Tk()
window.title("Login & Registration System")
window.geometry("300x150")
window.configure(bg="#F0F0F0")

# Кнопки для открытия окон регистрации и входа
btn_registration = tk.Button(window, text="Registration", command=open_registration_window, width=15, bg="#28A745", fg="white")
btn_registration.pack(pady=10)

btn_login = tk.Button(window, text="Login", command=open_login_window, width=15, bg="#007BFF", fg="white")
btn_login.pack(pady=10)

# Кнопка для выхода из программы
btn_exit = tk.Button(window, text="Exit", command=exit_program, width=15, bg="#6C757D", fg="white")
btn_exit.pack(pady=10)

# Запуск цикла событий Tkinter
window.mainloop()