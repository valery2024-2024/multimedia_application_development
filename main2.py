from PIL import Image, ImageFilter, ImageEnhance, ImageOps

img = Image.open("koala.jpg")   # <<< заміни на свій файл за потреби
print(img.size)
print(img.format)

# Effect 1 (Вінтаж)
e1_color = ImageEnhance.Color(img).enhance(0.6)            # менша насиченість
e1_dark  = ImageEnhance.Brightness(e1_color).enhance(0.9)  # трохи темніше
e1_blur  = e1_dark.filter(ImageFilter.GaussianBlur(1.5))   # легкий blur
e1_blur.save("effect1_vintage.png")

# Effect 2 (Поп-арт)
e2_contrast = ImageEnhance.Contrast(img).enhance(2.2)      # контраст
e2_bright   = ImageEnhance.Brightness(e2_contrast).enhance(1.25)  # яскравість
e2_flip     = e2_bright.transpose(Image.FLIP_LEFT_RIGHT)   # дзеркало
e2_invert   = ImageOps.invert(e2_flip.convert("RGB"))      # інверсія
e2_invert.save("effect2_popart.png")

# Effect 3 (Кінематографічний)
w, h = img.size
target_ratio = 16/9
# рахуємо центральний crop під 16:9
if w / h >= target_ratio:
    # занадто широкий — обмежуємо ширину
    new_w = int(h * target_ratio)
    new_h = h
else:
    # занадто високий — обмежуємо висоту
    new_w = w
    new_h = int(w / target_ratio)

left   = (w - new_w) // 2
top    = (h - new_h) // 2
right  = left + new_w
bottom = top + new_h

e3_crop = img.crop((left, top, right, bottom))
e3_1080 = e3_crop.resize((1920, 1080))  # точний розмір Full HD

# різкість (легкий SHARPEN)
e3_sharp = e3_1080.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
e3_sharp = e3_sharp.filter(ImageFilter.SHARPEN)

# трохи менша насиченість для кіно-стилю
e3_cine = ImageEnhance.Color(e3_sharp).enhance(0.9)
e3_cine.save("effect3_cinematic.png")

print("Готово: effect1_vintage.png, effect2_popart.png, effect3_cinematic.png")
