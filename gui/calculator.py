# my simple calculator project with tkinter

import tkinter as tk

var1 = " " # global variable to store string 
helping_var = " "

def button_click(number):
    current = myInputField.get()
    myInputField.delete(0, tk.END)
    myInputField.insert(0,str(current)+str(number))
    # each time the input field will be changed, the global variable will be updated with new value
    global var1 
    var1 = myInputField.get()

def button_clear():
    myInputField.delete(0, tk.END)

def add_number():
    global first_number
    first_number = int(var1)
    # after assigning the value of global variable var1 into first_number, var1 will be empty
    myInputField.delete(0, tk.END)
    global helping_var
    # whenever the add_number function will be called the helping variable will be set to "add"
    helping_var = "add"
    

def sub_number():
    global first_number
    first_number = int(var1)
    myInputField.delete(0, tk.END)
    global helping_var
    # whenever the sub_number function will be called the helping variable will be set to "sub"
    helping_var = "sub"

def mul_number():
    global first_number
    first_number = int(var1)
    myInputField.delete(0, tk.END)
    global helping_var
    # whenever the mul_number function will be called the helping variable will be set to "mul"
    helping_var = "mul"

def div_number():
    global first_number
    first_number = int(var1)
    myInputField.delete(0, tk.END)
    global helping_var
    # whenever the div_number function will be called the helping variable will be set to "div"
    helping_var = "div"

def equal():
    # equal function assign the value of global variable var1 into block variable second_number
    if helping_var == "add":
        second_number = int(var1)
        sum = first_number + second_number
        myInputField.delete(0, tk.END)
        myInputField.insert(0, str(sum))
    if helping_var == "sub":
        second_number = int(var1)
        value = first_number - second_number
        myInputField.delete(0, tk.END)
        myInputField.insert(0, str(value))
    if helping_var == "mul":
        second_number = int(var1)
        value = first_number * second_number
        myInputField.delete(0, tk.END)
        myInputField.insert(0, str(value))
    if helping_var == "div":
        second_number = int(var1)
        value = first_number / second_number
        myInputField.delete(0, tk.END)
        myInputField.insert(0, str(value))

# defining root widget

root = tk.Tk()
root.title("My Calcy")
myInputField = tk.Entry(root, width=45, borderwidth=5)
myInputField.grid(row=0, column=0, columnspan=3, pady=15)




# defining buttons
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_ad = tk.Button(root, text="+", padx=38.5, pady=20, command= add_number)
button_sub = tk.Button(root, text="-", padx=40.4, pady=20, command= sub_number)
button_mul = tk.Button(root, text="*", padx=40, pady=20, command= mul_number)
button_div = tk.Button(root, text="/", padx=40, pady=20, command= div_number)

button_eql = tk.Button(root, text="=", padx=38, pady=83, command= equal)
button_clr = tk.Button(root, text="c", padx=40, pady=20, command= button_clear)

#showing buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clr.grid(row=4, column=1)
button_eql.grid(row=4, column=2, rowspan=5)

button_ad.grid(row=5, column=0)
button_sub.grid(row=5, column=1)

button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1)

# putting the parent window into loop
root.mainloop()
