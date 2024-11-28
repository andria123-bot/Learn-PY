from tkinter import *
from tkinter import messagebox

def click():
  #messagebox.showinfo(title="This is an info message box", message="You clicked the button!")
  # while(True):
    #messagebox.showwarning(title="WARNING!", message="You have A VIRUS!!!!")
  # messagebox.showerror(title="ERROR!", message="Something went wrong :()")
  # if messagebox.askretrycancel(title="Ask ok cancel", message="Do you want to retry the thing?"):
  #   print("U did retried a thing!")
  # else:
  #   print("U canceled a things:(")
  
  # if messagebox.askyesno(title="Yes/No", message="Do you want to continue?"):
  #   print("i like to continue")
  # else:
  #   print("i don't like to continue")

  # answer = messagebox.askquestion(title="ask question", message="Do you liek pie?")
  # if(answer == "yes"):
  #   print("i like pie too")
  # else:
  #   print("i don't like pie")
  
  answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you want to code?", icon='error')

  if(answer == True):
    print("you like to code")
  elif(answer == False):
    print("you don't like to code")
  else:
    print("you canceled the code")
  
  
  
  
  
  
  
  
  
  
  
window = Tk()

button = Button(window, command=click, text='Click me')
button.pack()


window.mainloop()