# Практична №2. Базова обробка зображень (tkinter + Pillow)

from tkinter import Tk, Frame, Label, Button, filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

# 1) Вхідне зображення (зміни назву файла за потреби)
IMAGE_PATH = "flipped_img.png"

# Глобальні посилання (щоб картинка не "зникала")
original_img = None   # оригінал
work_img = None       # робоча копія (над нею виконуємо ефекти)
photo = None          # об'єкт ImageTk.PhotoImage для показу

# 2) Функції допоміжні
def load_image(path: str):
    """Завантажити зображення в пам'ять: original_img і робочу копію."""
    global original_img, work_img
    original_img = Image.open(path).convert("RGBA")   # уніфікуємо режим
    work_img = original_img.copy()
    show_image(work_img)

def fit_to_area(img: Image.Image, max_w=700, max_h=520):
    """Підігнати зображення під область показу зі збереженням пропорцій."""
    img = img.copy()
    img.thumbnail((max_w, max_h))
    return img

def show_image(img: Image.Image):
    """Показати зображення у лівій панелі."""
    global photo
    disp = fit_to_area(img, max_w=660, max_h=520)
    photo = ImageTk.PhotoImage(disp)
    img_label.config(image=photo, text="")
    img_label.image = photo  # ВАЖЛИВО: зберегти посилання

def reset_image():
    """Повернутися до оригіналу."""
    global work_img
    work_img = original_img.copy()
    show_image(work_img)

# 3) Ефекти обробки (кнопки праворуч)
def blur_soft():
    """Слабкий блур."""
    global work_img
    work_img = work_img.filter(ImageFilter.GaussianBlur(radius=2))
    show_image(work_img)

def blur_strong():
    """Сильний блур."""
    global work_img
    work_img = work_img.filter(ImageFilter.GaussianBlur(radius=6))
    show_image(work_img)

def invert_colors():
    """Інверсія кольорів з урахуванням альфа-каналу."""
    global work_img
    if work_img.mode == "RGBA":
        rgb, a = work_img.convert("RGB"), work_img.split()[-1]
        inv = ImageOps.invert(rgb).convert("RGBA")
        inv.putalpha(a)
        work_img = inv
    else:
        work_img = ImageOps.invert(work_img.convert("RGB"))
    show_image(work_img)

def to_grayscale():
    """Ефект 'сірого'."""
    global work_img
    work_img = ImageOps.grayscale(work_img).convert("RGBA")
    show_image(work_img)

def more_contrast():
    """Додатковий ефект: контраст +40%."""
    global work_img
    enhancer = ImageEnhance.Contrast(work_img.convert("RGB"))
    work_img = enhancer.enhance(1.4).convert("RGBA")
    show_image(work_img)

def more_brightness():
    """Додатковий ефект: яскравість +25%."""
    global work_img
    enhancer = ImageEnhance.Brightness(work_img.convert("RGB"))
    work_img = enhancer.enhance(1.25).convert("RGBA")
    show_image(work_img)

def save_as():
    """Зберегти поточне оброблене зображення у новий файл."""
    if work_img is None:
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg"), ("All files", "*.*")]
    )
    if path:
        # Якщо обрано JPEG — збережемо без альфа
        img_to_save = work_img.convert("RGB") if path.lower().endswith((".jpg", ".jpeg")) else work_img
        img_to_save.save(path)

# 4) Інтерфейс: ліва панель (зображення), права панель (кнопки)
root = Tk()
root.title("Практична №2 — Базова обробка зображень")
root.geometry("980x620")

# Ліва панель
left = Frame(root, bg="white")
left.pack(side="left", fill="both", expand=True)
img_label = Label(left, bg="white", text="(Завантаження зображення...)")
img_label.pack(side="top", pady=10)

# Права панель з кнопками (вертикально)
right = Frame(root, bg="#f0f0f0")
right.pack(side="right", fill="y", padx=8, pady=8)

# Кнопки-ефекти
Button(right, text="Слабкий блур",  command=blur_soft).pack(fill="x", pady=4)
Button(right, text="Сильний блур",  command=blur_strong).pack(fill="x", pady=4)
Button(right, text="Інверсія кольорів", command=invert_colors).pack(fill="x", pady=4)
Button(right, text="Сіре (grayscale)",   command=to_grayscale).pack(fill="x", pady=4)
Button(right, text="Контраст +",         command=more_contrast).pack(fill="x", pady=4)
Button(right, text="Яскравість +",       command=more_brightness).pack(fill="x", pady=4)

# Службові
Button(right, text="Скинути (оригінал)", command=reset_image).pack(fill="x", pady=12)
Button(right, text="Зберегти…",          command=save_as).pack(fill="x", pady=4)

# Стартове завантаження і показ
load_image(IMAGE_PATH)

root.mainloop()
