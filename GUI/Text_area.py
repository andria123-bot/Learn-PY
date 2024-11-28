from tkinter import *

window = Tk()

def submit():
  input = text.get("1.0", END)
  print(input)


button = Button(window, text="Submit", command=submit)

text = Text(window,
            bg="light yellow",
            font=("ink free", 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")

button.pack()
text.pack()


window.mainloop()