# my GUI

from tkinter import *

# Create a window
root = Tk()

# Modify root window
root.title('__dark00ps__')
root.geometry('700x400')

app = Frame(root)
app.grid()

button1 = Button(app, text='Button One')
button1.grid()

button2 = Button(app)
button2.grid()

label = Label(app, text='BGCH')
label.grid()

# photo = PhotoImage(file="images.jpg")
# label = Label(root1, image=photo)
# label.pack()

# Kickoff the event loop
root.mainloop()
