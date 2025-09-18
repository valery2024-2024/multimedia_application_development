# tkinter
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk

root = Tk()
root.title("My Window with the program")
root.geometry("650x450")

label = Label(root, text="Valerii Formaniuk KN-3/1" )
label.pack()

def on_click():
    print("button clicked")

button = Button(root, text="click me", command=on_click)
button.pack()

img = Image.open("img_invert.png")
img.resize((80, 100))
photo = ImageTk.PhotoImage(img)

label_img = Label(root, image=photo)
label_img.image = photo
label_img.pack()


root.mainloop()