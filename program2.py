import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def on_button_click(num):
    print(f"Наступна кнопка {num}")

# Вікно
root = tk.Tk()
root.title("Зображення + кнопки")
root.geometry("800x600")

# Ліва частина для зображення
left_frame = tk.Frame(root, bg="white")
left_frame.pack(side="left", fill="both", expand=True)

# Права частина кнопок
right_frame = tk.Frame(root, bg="lightgray")
right_frame.pack(side="right", fill="y")

img = Image.open("flipped_img.png").resize((600, 400))
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(left_frame, image=photo, bg="white")
img_label.image = photo          # ВАЖЛИВО: зберегти посилання!
img_label.pack(expand=True)

 

# Додаємо десять кнопок у правий фрейм
for i in range(1, 11):
    btn = tk.Button(right_frame, text=f"Кнопка {i}",
                    command=lambda n=i: on_button_click(n))
    btn.pack(fill="x", pady=2, padx=5)

root.mainloop()

    