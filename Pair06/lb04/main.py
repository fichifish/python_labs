import tkinter as tk
from tkinter import messagebox
import student_utils

def stats():
    value = count.get()
    if not value.isdecimal() or int(value) < 1 or int(value) > 20:
        messagebox.showerror("Помилка", "Ти не гідний жити")
        return
    students = ["Artem", "Komarov", "MrFish"]
    text = ""
    for i in students:
        grades = student_utils.generate_grades(int(value))
        avg = student_utils.average_grade(grades)
        level = student_utils.get_level(avg)
        s = f"{i}: {grades} -> {avg} -> {level}\n"
        text += s
    print(text)
    res.delete("1.0", tk.END)
    res.insert(tk.END, text)

root = tk.Tk()
root.title("Статистика учнів")
inn = tk.Label(root, text="Кількість оцінок, до 20")
inn.pack(pady=5)
count = tk.Entry(root)
count.pack(pady=5)
button = tk.Button(root, text="Сформувати звіт", command=stats)
button.pack(pady=5)
res = tk.Text(root, height=32, width=128)
res.pack(pady=10)

root.mainloop()