from tkinter import *
from PIL import Image, ImageTk

root = Tk()

canvas = Canvas(width=500, height=500, bg='white')
canvas.pack()
image = Image.open("Trollface.jpg")
photo = ImageTk.PhotoImage(image)
canvas.create_image(250, 250, image=photo)

root.mainloop()
