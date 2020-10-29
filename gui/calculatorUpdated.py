import tkinter      # importing tkinter module
from tkinter import *
from tkinter import messagebox

val = ""
value1 = 0
operator = ""


def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)

def btn0_clicked():
    global val
    val = val + "0"
    data.set(val)

def add_clicked():
    global value1
    global operator
    global val
    value1 = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def minus_clicked():
    global value1
    global operator
    global val
    value1 = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def mul_clicked():
    global value1
    global operator
    global val
    value1 = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def div_clicked():
    global value1
    global operator
    global val
    value1 = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def clr_clicked():
    global value1
    global operator
    global val
    value1 = 0
    operator = ""
    val = ""
    data.set(val)

def result():
    global value1
    global val
    global operator
    value2 = val
    if operator == "+":
        x = int((value2.split("+")[1]))
        c = value1 + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((value2.split("-")[1]))
        c = value1 - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((value2.split("*")[1]))
        c = value1 * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((value2.split("/")[1]))
        if x == 0:
            messagebox.showerror(title = None, message= "Error,Division not possible")
            value1 = ""
            val = ""
            data.set(val)
        else:
            c = int(value1 / x)
            data.set(c)
            val = str(c)


root = Tk()     
#The Tk class is instantiated without arguments
#This creates a toplevel widget of Tk which usually is the main window of an application
root.geometry("250x400+550+200")
root.resizable(0,0)
root.title("calculator")
root.iconbitmap("D:/GUI/icons/calcy.ico")



# frames for the buttons & label
mylabel = Frame(root, highlightbackground="white", highlightcolor="white", highlightthickness = 1, bd = 0)
mylabel.pack(expand = True, fill = "both") 

btnrow1 = Frame(root, bg = "white")
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root, bg = "white")
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root, bg = "white")
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root, bg = "white")
btnrow4.pack(expand = True, fill = "both")
#*************************code for label*****************************************************
data = StringVar()

myNewlabel = Label(
    mylabel,
    bg = "black",
    fg = "white",
    font = ("Verdana", 18),
    border = 4,
    anchor = SE,
    textvariable = data, 
    relief="flat",
    )
myNewlabel.pack(expand = TRUE, fill = "both")

#*************************code for buttons in frame 1 ****************************************
btn_7 = Button(
    btnrow1,
    text = "7",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn7_clicked
)
btn_7.pack(side = LEFT, expand = TRUE, fill = "both")

btn_8 = Button(
    btnrow1,
    text = "8",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn8_clicked
)
btn_8.pack(side = LEFT, expand = TRUE, fill = "both")

btn_9 = Button(
    btnrow1,
    text = "9",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn9_clicked
)
btn_9.pack(side = LEFT, expand = TRUE, fill = "both")

btn_div = Button(
    btnrow1,
    text = "/",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = div_clicked
)
btn_div.pack(side = LEFT, expand = TRUE, fill = "both")


#***********************code for buttons in frame 2***********************************
btn_4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn4_clicked
)
btn_4.pack(side = LEFT, expand = TRUE, fill = "both")

btn_5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn5_clicked
)
btn_5.pack(side = LEFT, expand = TRUE, fill = "both")

btn_6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn6_clicked
)
btn_6.pack(side = LEFT, expand = TRUE, fill = "both")

btn_mul = Button(
    btnrow2,
    text = "x",
    font = ("Verdana", 19),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = mul_clicked
)
btn_mul.pack(side = LEFT, expand = TRUE, fill = "both")


#*****************************code for buttons in frame 3****************************
btn_1 = Button(
    btnrow3,
    text = "1",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn1_clicked,
)
btn_1.pack(side = LEFT, expand = TRUE, fill = "both")

btn_2 = Button(
    btnrow3,
    text = "2",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn2_clicked
)
btn_2.pack(side = LEFT, expand = TRUE, fill = "both")

btn_3 = Button(
    btnrow3,
    text = "3",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn3_clicked
)
btn_3.pack(side = LEFT, expand = TRUE, fill = "both")

btn_sub = Button(
    btnrow3,
    text = "-",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = minus_clicked
)
btn_sub.pack(side = LEFT, expand = TRUE, fill = "both")

#***************************code for buttons in frame 4****************************
btn_clr = Button(
    btnrow4,
    text = "clr",
    font = ("Verdana", 16),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = clr_clicked
)
btn_clr.pack(side = LEFT, expand = TRUE, fill = "both")

btn_0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = btn0_clicked
)
btn_0.pack(side = LEFT, expand = TRUE, fill = "both")

btn_eql = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 19),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = result
)
btn_eql.pack(side = LEFT, expand = TRUE, fill = "both")

btn_add = Button(
    btnrow4,
    text = "+",
    font = ("Verdana", 17),
    bg = "#000000",
    fg = "white",
    relief = GROOVE,
    border = 0,
    command = add_clicked
)
btn_add.pack(side = LEFT, expand = TRUE, fill = "both")


root.mainloop()
