from PIL import Image, ImageFilter, ImageEnhance, ImageOps
# 1. Відкрити зображення
img = Image.open("Image2.jpg")
print(img.size)
print(img.format)

# 2. Вирізвти центральну частину
cropped_img = img.crop((45, 68, 137, 206))
cropped_img.save("step2_crop.png")

# 3. Зменшити масштаб у двічі
scaled_img = cropped_img.resize(
    (cropped_img.width // 2, cropped_img.height // 2)
)
scaled_img.save("step3_scaled.png")

# 4. Gaussian Blur
gaussian_img = scaled_img.filter(ImageFilter.GaussianBlur(5))
gaussian_img.save("step4_gaussian.png")

# 5. Інверсія кольорів
inverted_img = ImageOps.invert(gaussian_img.convert("RGB"))
inverted_img.save("step5_invert.png")

# 6. Збільшення яскравості на 50%
enhancer = ImageEnhance.Brightness(inverted_img)
bright_img = enhancer.enhance(1.5)
bright_img.save("step6_bright.png")

# 7. Зберегти фінальне зображення
bright_img.save("result1.png")

print("Готово! Файл збережено як result1.png")