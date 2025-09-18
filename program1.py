from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

# список моїх зображень
images = ["flipped_img.png", "img_contrast.png", "img_invert.png"]
current_index = 0

def show_image(index):
    global photo, current_index
    current_index = index % len(images) # зациклення
    img = Image.open(images[current_index])
    img = img.resize((400, 300))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo) 

def next_image():
    show_image(current_index + 1)

def prev_image():
    show_image(current_index - 1)

root = Tk()
root.title("Галерея моїх зображень")

photo = None
label = Label(root)
label.pack()

btn_prev = Button(root, text="Попереднє", command=prev_image)
btn_prev.pack(side="left", padx=10)

btn_next = Button(root, text="Наступне", command=next_image)
btn_next.pack(side="right", padx=10)

show_image(0)

root.mainloop()
