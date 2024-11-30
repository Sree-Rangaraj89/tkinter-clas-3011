from tkinter import Tk,Label,Button,Entry,Frame,Text
window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greetings = Label(text="Hello user", fg='black', bg='white')
button = Button(text="click me", bg='black', fg='white')
entry = Entry(fg="yellow",bg="blue",width=50)
greetings.pack()
button.pack()
entry.pack()

frame = Frame(master=window,borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='red', bg='beige')
textbox.pack()

window.mainloop()