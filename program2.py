import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageOps, ImageEnhance


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

img_default = Image.open("flipped_img.png").resize((600, 400))
img_to_show = img_default
photo = ImageTk.PhotoImage(img_default)
img_label = tk.Label(left_frame, image=photo, bg="white")
img_label.image = photo          # ВАЖЛИВО: зберегти посилання!
img_label.pack(expand=True)

def inversion_color():
    global img_to_show
    img_to_show = ImageOps.invert(img_default.convert("RGB"))
    show_img()

def show_default(): 
    global img_to_show
    img_to_show = img_default
    show_img()   

def show_img():
    global photo
    photo = ImageTk.PhotoImage(img_to_show)
    img_label.config(image=photo)

def contrast():
    global img_to_show 
    enhancer = ImageEnhance.Contrast(img_default) 
    img_to_show = enhancer.enhance(2) 
    show_img() 

def save_img():
    img_to_show.save("result_img.png")     
 


# Додаємо декілька кнопок у правий фрейм
btn0 = tk.Button(right_frame, text=f"Початкове", command=show_default)
btn0.pack(fill="x", pady=2, padx=5)

btn1 = tk.Button(right_frame, text=f"Інверсія", command=inversion_color)
btn1.pack(fill="x", pady=2, padx=5)

btn2 = tk.Button(right_frame, text=f"Контраст", command=contrast)
btn2.pack(fill="x", pady=2, padx=5)

btnSave = tk.Button(right_frame, text=f"Зберегти", command=save_img)
btnSave.pack(fill="x", pady=2, padx=5)

root.mainloop()

    