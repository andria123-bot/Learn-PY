from tkinter import *
window = Tk()

def submit():
  print("The temperature is: ", str(scale.get()) + "degrees C")

# images = PhotoImage(file="GUI/images/dscpfp.PNG")
# hotLabel = Label(image=images) # FOR IMAGES DISABLED CUZ ITS UGLY
# hotLabel.pack()

scale = Scale(window, 
              from_ = 100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
              #showvalue=0, # hides current value
              resolution=5,
              troughcolor='#65EAFE',
              fg='#FF1C00',
              bg='#111111')
scale.pack()
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])

button = Button(window, text="submit", command=submit)
button.pack()


window.mainloop()