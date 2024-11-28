from tkinter import *

window = Tk() #instalite an instance of a window
window.geometry("420x420")
window.title("First GUI")

icon = PhotoImage(file='GUI/dscpfp.PNG')
window.iconphoto(True, icon)
window.config(background="#6cfcff")

window.mainloop() #place window on computer screen and also lisen for event
