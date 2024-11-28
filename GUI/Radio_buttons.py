from tkinter import *

window = Tk()

food = ["pizza", "hamburger", "hotdog"]

# pizzaImage = PhotoImage(file='GUI/Pizza.jpg')
# hamburgerImage = PhotoImage(file='GUI/hamburger.jpg')
# hotdogImage = PhotoImage(file='GUI/hotdog.jpg')

x = IntVar()

for index in range(len(food)):
  radiobutton = Radiobutton(window, 
                            text=food[index], # adds text to radio buttons
                            variable=x, # groups radiobuttons together if they share the same variable
                            value=index, # assings each radio button a different value
                            padx=25) # adds padding on x-axis
  radiobutton.pack(anchor=W)
window.mainloop()