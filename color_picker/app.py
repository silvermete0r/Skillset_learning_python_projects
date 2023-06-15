import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor(title="Select Color")
    if color[1]:
        selected_color_label.config(text=f"Selected Color: {color[1]}", fg=color[1])

def copy_hash():
    color_hash = selected_color_label.cget("fg")
    window.clipboard_clear()
    window.clipboard_append(color_hash)

def copy_rgb():
    color_rgb = selected_color_label.cget("fg")
    rgb_values = tuple(int(color_rgb[i:i+2], 16) for i in (1, 3, 5))
    rgb_string = f"RGB: {rgb_values}"
    window.clipboard_clear()
    window.clipboard_append(rgb_string)

def exit_program():
    window.destroy()

# Создание главного меню
window = tk.Tk()
window.title("Color Picker")
window.geometry("400x250")  # Настройка размеров
window.resizable(True, True)  # Разрешить менять размер окна

# Настройка кнопки выбора цвета
button_frame = tk.Frame(window)
button_frame.pack(pady=20)
pick_color_button = tk.Button(button_frame, text="Pick Color", command=choose_color, font=("Arial", 14), bg="#72d8fe", fg="black")
pick_color_button.pack(padx=10, pady=10)

# Настройка текста выбранного цвета
label_frame = tk.Frame(window)
label_frame.pack()
selected_color_label = tk.Label(label_frame, text="Selected Color:", font=("Arial", 16))
selected_color_label.pack(pady=10)

# Настройка кнопки копирования хэш цвета и RGB цвета
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
copy_hash_button = tk.Button(button_frame, text="Copy Hash", command=copy_hash, font=("Arial", 12), bg="#55fd8f", fg="black")
copy_hash_button.pack(side=tk.LEFT, padx=5)
copy_rgb_button = tk.Button(button_frame, text="Copy RGB", command=copy_rgb, font=("Arial", 12), bg="#55fd8f", fg="black")
copy_rgb_button.pack(side=tk.LEFT, padx=5)

# Настройка кнопки выхода
exit_button = tk.Button(window, text="Exit", command=exit_program, font=("Arial", 12), width=15, bg="#d50005", fg="white")
exit_button.pack(pady=10)

# Запуск цикла событий Tkinter
window.mainloop()