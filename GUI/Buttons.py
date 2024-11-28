from tkinter import *

window = Tk()

photo = PhotoImage(file='GUI/dscpfp.PNG')

count = 0
def click():
  global count
  count += 1
  print(f'You Clicked {count} times')


button = Button(window,
                text="Click Me!",
                command=click,
                font=('Comic  Sans', 30),
                fg='#00FF00',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE, # To click button if DISABLED u cant click
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()