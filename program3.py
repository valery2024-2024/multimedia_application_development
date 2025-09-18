from tkinter import Tk, Label, Button, Frame, PhotoImage

# 1) Список зображень (файли мають лежати поряд зі скриптом)
IMAGES = ["img_blur.png", "flipped_img.png", "img_invert.png"]

current_index = 0
photos = []  # кеш PhotoImage, щоб картинки не зникали
root = Tk()
root.title("Галерея зображень")
root.geometry("800x600")

# Верх: місце під зображення
img_label = Label(root, bg="white")
img_label.pack(side="top", pady=10)

# Низ: фрейм з двома кнопками
controls = Frame(root)
controls.pack(side="bottom", fill="x", pady=10)

def load_images():
    """Завантажуємо всі зображення одразу у PhotoImage (як у зразку без PIL)."""
    global photos
    for path in IMAGES:
        try:
            photos.append(PhotoImage(file=path))
        except Exception:
            photos.append(None)  # щоб не падало, якщо файл відсутній

def show_image(index: int):
    """Показ зображення за індексом з зацикленням."""
    global current_index
    if not photos:
        img_label.config(text="(Немає зображень)", image="")
        return
    current_index = index % len(photos)
    pic = photos[current_index]
    if pic is None:
        img_label.config(text=f"(Файл не знайдено: {IMAGES[current_index]})", image="")
    else:
        img_label.config(image=pic, text="")
        img_label.image = pic  # тримаємо посилання

def prev_image():
    show_image(current_index - 1)

def next_image():
    show_image(current_index + 1)

# Кнопки
btn_prev = Button(controls, text="◀ Назад", command=prev_image)
btn_prev.pack(side="left", padx=10)

btn_next = Button(controls, text="Вперед ▶", command=next_image)
btn_next.pack(side="right", padx=10)

# Старт
load_images()
show_image(0)

root.mainloop()
