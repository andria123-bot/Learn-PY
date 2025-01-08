# calculator needs repair
from tkinter import *

win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    try:
        global expression
        total = eval(expression)
        input_text.set(total)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

expression = ""

input_text = StringVar()

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font="Arial 18 bold", textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)

btns_frame = Frame(win, width=312, height=272.5, bg="gray")
btns_frame.pack()

clear = Button(btns_frame, text="C", font="Arial 18 bold", width=32, height=3, bd=0, cursor="hand2", command=bt_clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
multiply = Button(btns_frame, text="*", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=0, padx=1, pady=1)
subtract = Button(btns_frame, text="-", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click("-")).grid(row=1, column=1, padx=1, pady=1)
add = Button(btns_frame, text="+", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click("+")).grid(row=1, column=2, padx=1, pady=1)
seven = Button(btns_frame, text="7", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(7)).grid(row=2, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(8)).grid(row=2, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(9)).grid(row=2, column=2, padx=1, pady=1)
four = Button(btns_frame, text="4", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(4)).grid(row=3, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(5)).grid(row=3, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(6)).grid(row=3, column=2, padx=1, pady=1)
one = Button(btns_frame, text="1", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(1)).grid(row=4, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(2)).grid(row=4, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(3)).grid(row=4, column=2, padx=1, pady=1)
zero = Button(btns_frame, text="0", font="Arial 18 bold", width=21, height=3, bd=0, cursor="hand2", command=lambda: btn_click(0)).grid(row=5, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=lambda: btn_click(".")).grid(row=5, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", font="Arial 18 bold", width=10, height=3, bd=0, cursor="hand2", command=bt_equal).grid(row=6, column=1, padx=1, pady=1)

win.mainloop()
