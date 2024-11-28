from tkinter import *
from tkinter import filedialog

def openFile():
  filepath = filedialog.askopenfilename()
  file = open(filepath, 'r')
  print(file)

window = Tk()
button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()
