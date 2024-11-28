from tkinter import *

window = Tk()

photo = PhotoImage(file='GUI/dscpfp.PNG')

label = Label(window, 
              text="Hello World my name is andria", 
              font=('Arial', 40, 'bold'), 
              fg='#00FF00',
              bg='black',
              relief=SUNKEN, # RAISED SUNKEN
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

label.pack() # displays at top of the window and middle of the window
# label.place(x=100, y=100) # displays by X Y position

window.mainloop()