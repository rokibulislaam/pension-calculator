import tkinter
from tkinter import *

root = Tk()

# color will be use gray70
root.geometry("1300x770+115+15")
root.resizable(0,0)
root.title("Pension_Calculator")
root.iconbitmap("D:/GUI/icons/pcalcy1.ico")

#********************* codes for main frame and sub frame******************************

header = Frame(root, bg = "white")
header.pack( fill = X, side = TOP)

centreframe = Frame(root, bg = "white")
centreframe.pack(fill = BOTH, side = TOP, expand = TRUE)

leftframe = Frame(centreframe, bg = "gray75", padx = 5, pady = 5)
leftframe.pack(expand = TRUE, fill = BOTH, side = LEFT, padx = 15, pady = 20)

rightframe = Frame(centreframe, bg = "gray75", padx = 5, pady = 5 )
rightframe.pack(expand = TRUE, fill = BOTH, side = LEFT, padx = 15, pady = 20)



#********************codes for frames and labels user inputs and output section****************
heading = Label(
    header,
    text = "BASIC PENSION AND COMMUTATION CALCULATOR",
    font = ("times", 22),
    bg = "white",
    fg = "black",
    )
heading.pack(expand = TRUE, fill = X, pady = 5)

heading1 = Label(
    leftframe,
    text = "ENTER DATA TO CALCULATE PENSION AND COMMUTATION",
    font = ("arial", 15),
    fg = "black",
    bg = "gray75",
    pady = 2
)
heading1.pack(side = TOP)

frame1 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
frame1.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

frame2 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame2.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

frame3 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame3.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

frame4 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame4.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

frame5 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame5.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

frame6 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame6.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

submitbutton1 = Button(
    leftframe,
    text = "SUBMIT",
    font = ("arial", 13),
    fg = "black",
    bg = "gray45",
    relief = FLAT,
    padx = 6,
    pady = 2
)
submitbutton1.pack(pady = 5)

frame7 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame7.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

frame8 = Frame(leftframe, 
    bg = "gray75",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

frame8.pack(expand = TRUE, fill = BOTH, padx = 6, pady = 5)

submitbutton2 = Button(
    leftframe,
    text = "SUBMIT",
    font = ("arial", 13),
    fg = "black",
    bg = "gray45",
    relief = FLAT,
    padx = 6,
    pady = 2
)
submitbutton2.pack(pady = 5)

heading2 = Label(
    rightframe,
    text = "PENSION AND COMMUTED VALUE",
    font = ("arial", 15),
    fg = "black",
    bg = "gray75"
)
heading2.pack(side = TOP )


root.mainloop()