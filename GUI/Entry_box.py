from tkinter import *

window = Tk()

def submit():
  username = entry.get()
  print(f'Hello {username}')
  entry.config(state=DISABLED)

def delete():
  entry.delete(0, END)

def backspace():
  entry.delete(len(entry.get())-1)

entry = Entry(window,
              font=("Arial", 50),
              fg='#00FF00',
              bg='black',
              show="*") # For Password not be visible

# entry.insert(0, "ANDROID") # adds auto name in input field
entry.pack(side=LEFT)

submit_btn = Button(window, text="submit", command=submit)
submit_btn.pack(side=RIGHT)

delete_btn = Button(window, text="delete", command=delete)
delete_btn.pack(side=RIGHT)

backspace_btn = Button(window, text="backspace", command=backspace)
backspace_btn.pack(side=RIGHT)


window.mainloop()