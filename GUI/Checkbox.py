from tkinter import *

def display():
  if (x.get() == "YES"):
    print("You agreed")
  else:
    print("You didn't agree")

window = Tk()


x = BooleanVar()

dscpfp_photo = PhotoImage(file='GUI/dscpfp.PNG')

check_button = Checkbutton(window,
                          text="I agree something",
                          variable=x,
                          onvalue=YES,
                          offvalue=NO,
                          command=display,
                          font=('Arial', 20),
                          fg='#00FF00',
                          bg='black',
                          activeforeground='#00FF00',
                          activebackground='black',
                          padx=25,
                          pady=10,
                          image=dscpfp_photo,
                          compound='left')

check_button.pack()
window.mainloop()
