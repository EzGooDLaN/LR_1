import tkinter as tk
from tkinter import messagebox


def is_obtuse(x1, y1, x2, y2, x3, y3):                                                              #проверка что не на одной прямой, иначе это не треугольник
    area2 = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if area2 == 0:
        return False

    a = (x2 - x1) ** 2 + (y2 - y1) ** 2
    b = (x3 - x2) ** 2 + (y3 - y2) ** 2
    c = (x1 - x3) ** 2 + (y1 - y3) ** 2

    a, b, c = sorted([a, b, c])

    return a + b < c


def check():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        x3 = float(entry_x3.get())
        y3 = float(entry_y3.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа во все поля")
        return

    if is_obtuse(x1, y1, x2, y2, x3, y3):
        result_label.config(text="Треугольник тупоугольный", fg="green")
    else:
        result_label.config(text="Треугольник не тупоугольный", fg="red")


root = tk.Tk()
root.title("Тупоугольный треугольник")
root.geometry("320x280")
root.resizable(False, False)


tk.Label(root, text="Точка 1").grid(row=0, column=0, columnspan=4, pady=(10, 0))                                    #Точка 1
tk.Label(root, text="x:").grid(row=1, column=0, padx=(10, 2))
entry_x1 = tk.Entry(root, width=8)
entry_x1.grid(row=1, column=1)
tk.Label(root, text="y:").grid(row=1, column=2, padx=(10, 2))
entry_y1 = tk.Entry(root, width=8)
entry_y1.grid(row=1, column=3)


tk.Label(root, text="Точка 2").grid(row=2, column=0, columnspan=4, pady=(10, 0))                                    #Точка 2
tk.Label(root, text="x:").grid(row=3, column=0, padx=(10, 2))
entry_x2 = tk.Entry(root, width=8)
entry_x2.grid(row=3, column=1)
tk.Label(root, text="y:").grid(row=3, column=2, padx=(10, 2))
entry_y2 = tk.Entry(root, width=8)
entry_y2.grid(row=3, column=3)


tk.Label(root, text="Точка 3").grid(row=4, column=0, columnspan=4, pady=(10, 0))                                     #Точка 3
tk.Label(root, text="x:").grid(row=5, column=0, padx=(10, 2))
entry_x3 = tk.Entry(root, width=8)
entry_x3.grid(row=5, column=1)
tk.Label(root, text="y:").grid(row=5, column=2, padx=(10, 2))
entry_y3 = tk.Entry(root, width=8)
entry_y3.grid(row=5, column=3)


tk.Button(root, text="Проверить", command=check, width=20).grid(                                                    #Кнопка
    row=6, column=0, columnspan=4, pady=15
)


result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))                                                 #Результат
result_label.grid(row=7, column=0, columnspan=4)

root.mainloop()
