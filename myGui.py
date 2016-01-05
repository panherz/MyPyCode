# my GUI

import Tkinter

# Create a window
root = Tkinter.Tk()

# Modify root window
root.title('__dark00ps__')
root.geometry('700x400')

app = Tkinter.Frame(root)
app.grid()

button1 = Tkinter.Button(app, text='Button One')
button1.grid()

button2 = Tkinter.Button(app)
button2.grid()

label = Tkinter.Label(app, text='BGCH')
label.grid()

# photo = PhotoImage(file="images.jpg")
# label = Label(root1, image=photo)
# label.pack()

# Kickoff the event loop
root.mainloop()
