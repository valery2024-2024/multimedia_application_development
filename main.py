from PIL import Image, ImageFilter, ImageEnhance, ImageOps
# 1. Відкрити зображення
img = Image.open("Image.jpg")
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

# crop (обрізання)
# # default_cropped_img = img.crop((450, 150, 800, 350))
# default_cropped_img.save("default_cropped_img.png")

# default_cropped_img = img.crop((150, 50, 200, 150))
# default_cropped_img.save("default_cropped_img_2.png")

# default_cropped_img = img.crop((750, 450, 900, 650))
# default_cropped_img.save("default_cropped_img_3.png")

# # default scale (стандартне маштування(за розміром))
# default_scaled_img = img.resize((900, 300))
# default_scaled_img.save("default_scaled_img.png")

# default_scaled_img = img.resize((300, 100))
# default_scaled_img.save("default_scaled_img_1.png")

# default_scaled_img = img.resize((200, 50))
# default_scaled_img.save("default_scaled_img_2.png")

# default_scaled_img = img.resize((700, 50))
# default_scaled_img.save("default_scaled_img_3.png")

# # scale with factor (маштабування за множником)
# scale_factor = 0.5
# new_width = int(img.width * scale_factor)
# new_height = int(img.height * scale_factor)

# scaled_image = img.resize((new_width, new_height))
# scaled_image.save("scaled_img.png")

# # scale with value (масштабування за 1-м значенням)
# new_width = 1920
# new_height = int((new_width / img.width) * img.height)
# scaled_with_value_image = img.resize((new_width, new_height))
# scaled_with_value_image.save("scaled_with_value_image.png")

# # mirror (flip) (відзеркалення)
# flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# flipped_img.save("flipped_img.png")

# # default blur (стандартне розмиття)
# img_blur = img.filter(ImageFilter.BLUR)
# img_blur.save("img_blur.png")

# # gaussin blur (розмиття за Гаусом)
# img_gaussin_blur = img.filter(ImageFilter.GaussianBlur)
# img_gaussin_blur.save("img_gaussin_blur.png")

# # smooth (згладжування)
# img_smooth = img.filter(ImageFilter.SMOOTH)
# img_smooth.save("img_smooth.png")

# # sharp (різкість)
# img_sharp = img.filter(ImageFilter.SHARPEN)
# img_sharp.save("img_sharp.png")

# # contrast (контраст)
# enhancer = ImageEnhance.Contrast(img)
# img_contrast = enhancer.enhance(2)
# img_contrast.save("img_contrast.png")

# # bright (яскравість)
# enhancer = ImageEnhance.Brightness(img)
# img_bright = enhancer.enhance(1.5)
# img_bright.save("img_bright.png")

# # color (насиченість)
# enhancer = ImageEnhance.Color(img)
# img_color = enhancer.enhance(1.3)
# img_color.save("img_color.png")

# # inversion (інверсія кольорів)
# img_invert = ImageOps.invert(img.convert("RGB"))
# img_invert.save("img_invert.png")

# # rotate (розворот)
# img_rotate = img.rotate(90)
# #img_rotate.save("img_rotate.png")