from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Multi calc")
root.iconbitmap("img/calc_dark_800.ico")
root.resizable(False, False)

# MENU LOGIC FUNCTIONS

def quit_app():
    response = messagebox.askyesnocancel("Exit program", "Are You sure You wanna exit this prefect app?")
    if response == 1:
        messagebox.showinfo("Ah vot kak", "Bastard!")
        root.quit()
    elif response == 0:
        messagebox.showinfo("Molodec!", "Good boy <3")

# TOP MENU

explore_menu = Menu(tearoff=0)
explore_menu.add_command(label="Your Own Photo", state=DISABLED)
explore_menu.add_command(label="Photos selected by Me", state=DISABLED)

main_menu = Menu()
main_menu.add_cascade(label="Explore Some Photos", menu=explore_menu)
main_menu.add_cascade(label="Exit Program", command=quit_app)

root.config(menu=main_menu)



# CALCULATOR LOGIC FUNCTIONS

def btn_click(sym):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(sym))

def add():
    global operation
    operation = "addition"

    global first_num
    first_num = float(e.get())

    e.delete(0, END)

def subtract():
    global operation
    operation = "subtraction"

    global first_num
    first_num = float(e.get())

    e.delete(0, END)

def multiply():
    global operation
    operation = "multiplication"

    global first_num
    first_num = float(e.get())

    e.delete(0, END)

def divide():
    global operation
    operation = "division"

    global first_num
    first_num = float(e.get())

    e.delete(0, END)

def sqrt():
    num = float(e.get())
    e.delete(0, END)
    e.insert(0, sqrt(num))

def power2():
    num = float(e.get())
    e.delete(0, END)
    e.insert(0, pow(num, 2))

# EXPERIMENTAL FUNCTION TO ADD PLACEHOLDER
# WORKS ONLY 1 TIME

def on_click(event):
    e.configure(state=NORMAL)
    e.delete(0, END)
    e.unbind('<Button-1>', on_click_event)

# END

def equals():
    second_num = e.get()
    e.delete(0, END)
    
    if operation == "addition":
        e.insert(0, first_num + float(second_num))
    if operation == "subtraction":
        e.insert(0, first_num - float(second_num))
    if operation == "multiplication":
        e.insert(0, first_num * float(second_num))
    if operation == "division":
        if int(second_num) == 0:
            e.insert(0, "TI KAK IZ DURKI VIBRALSA?")
            e.configure(state=DISABLED)
        else:
            e.insert(0, first_num / float(second_num))

def clear():
    e.delete(0, END)

# ENTER FIELD

e = Entry(root, width=80, borderwidth=5)

# BUTTONS DESIGN

btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))

btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))

btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))

btn_clear = Button(root, text="C", padx=40, pady=20, command=clear)
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
btn_dot = Button(root, text=".", padx=42, pady=20, command=lambda: btn_click("."))

btn_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)
btn_divide = Button(root, text="/", padx=49, pady=20, command=divide)

btn_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)
btn_sqrt = Button(root, text="√x", padx=45, pady=20, command=sqrt, state=DISABLED)

btn_add = Button(root, text="+", padx=39, pady=20, command=add)
btn_2power = Button(root, text="x^2", padx=42, pady=20, command=power2)

btn_equals = Button(root, text="=", padx=95, pady=20, command=equals)

# PLACEMENT OF ENTER FIELD & BUTTONS

e.grid(row=0, column=0, columnspan=5)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)

btn_clear.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
btn_dot.grid(row=4, column=2)

btn_multiply.grid(row=1, column=3)
btn_divide.grid(row=1, column=4)

btn_subtract.grid(row=2, column=3)
btn_sqrt.grid(row=2, column=4)

btn_add.grid(row=3, column=3)
btn_2power.grid(row=3, column=4)

btn_equals.grid(row=4, column=3, columnspan=2)

# BINDING EVENT

on_click_event = e.bind('<Button-1>', on_click)

root.mainloop()
