import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font

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

leftframe = Frame(centreframe, bg = "gray82", padx = 8, pady = 8)
leftframe.pack(expand = TRUE, fill = BOTH, side = LEFT, padx = 20, pady = 20)

rightframe = Frame(centreframe, bg = "gray82", padx = 8, pady = 8 )
rightframe.pack(expand = TRUE, fill = BOTH, side = LEFT, padx = 20, pady = 20)


#**************** codes for header label****************************************************

heading = Label(
    header,
    text = "BASIC PENSION AND COMMUTATION CALCULATOR",
    font = ("Product Sans", 22, "bold"),
    bg = "white",
    fg = "black",
    )
heading.pack(expand = TRUE, fill = X, pady = 6)

#********************codes for left frames and labels user inputs section****************

heading1 = Label(
    leftframe,
    text = "ENTER DATA TO CALCULATE PENSION AND COMMUTATION",
    font = ("arial", 15, "bold"),
    fg = "black",
    bg = "gray82",
    pady = 2
)
heading1.pack(side = TOP)

Lframe1 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1,
    pady = 0
)
Lframe1.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Lframe2 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

Lframe2.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Lframe3 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

Lframe3.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Lframe4 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

Lframe4.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Lframe5 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

Lframe5.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)


submitbutton1 = Button(
    leftframe,
    text = "SUBMIT",
    font = ("arial", 13, "bold"),
    fg = "black",
    bg = "gray45",
    relief = FLAT,
    padx = 6,
    pady = 2,
    activebackground = "black",
    activeforeground = "white",
    
)
submitbutton1.pack(pady = 8)

Lframe6 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

Lframe6.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Lframe7 = Frame(leftframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)

Lframe7.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

submitbutton2 = Button(
    leftframe,
    text = "SUBMIT",
    font = ("arial", 13, "bold"),
    fg = "black",
    bg = "gray45",
    relief = FLAT,
    padx = 6,
    pady = 2,
    activebackground = "black",
    activeforeground = "white",
    
)
submitbutton2.pack(pady = 5)

#********************codes for left frames and labels user inputs section****************

heading2 = Label(
    rightframe,
    text = "PENSION AND COMMUTED VALUE",
    font = ("arial", 15, "bold"),
    fg = "black",
    bg = "gray82"
)
heading2.pack(side = TOP )

Rframe1 = Frame(rightframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
Rframe1.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Rframe2 = Frame(rightframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
Rframe2.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Rframe3 = Frame(rightframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
Rframe3.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Rframe4 = Frame(rightframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
Rframe4.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Rframe5 = Frame(rightframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
Rframe5.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)

Rframe6 = Frame(rightframe, 
    bg = "gray82",
    bd = 1,
    highlightbackground="black",
    highlightthickness=1
)
Rframe6.pack(expand = TRUE, fill = BOTH, padx = 8, pady = 5)


reset = Button(
    rightframe,
    text = "RESET",
    font = ("arial", 13, "bold"),
    fg = "black",
    bg = "gray45",
    relief = FLAT,
    padx = 8,
    pady = 2,
    activebackground = "black",
    activeforeground = "white",
    
)
reset.pack(pady = 10)



#************************ codes for input field***********************
label1 = Label(
    Lframe1,
    text = "Type Of Retirement",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label1.pack(side = LEFT)

label2 = Label(
    Lframe2,
    text = "Date Of Birth",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label2.pack(side = LEFT)

label3 = Label(
    Lframe3,
    text = "Date Of Joining",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label3.pack(side = LEFT)

label4 = Label(
    Lframe4,
    text = "Date Of Retirement",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label4.pack(side = LEFT)

label5 = Label(
    Lframe5,
    text = "Basic Pay Or Average Of Last 10 mont Emoluments",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label5.pack(side = LEFT)

label6 = Label(
    Lframe6,
    text = "Percentage Of Commutation(Max 40%)",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label6.pack(side = LEFT)

label7 = Label(
    Lframe7,
    text = "Age Next Birth Day(age at retirement + 1 year)",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label7.pack(side = LEFT)

#********************codes for dropdown user inputs****************
# Combobox creation 

typeRetirement = ttk.Combobox(Lframe1, width = 28, values=["Superannuation","VRS"], state = "readonly") 
  

typeRetirement.pack(side = RIGHT, padx = 10) 
typeRetirement.current(0) # method to set default value

#******************* enrty input filed for DOB user input entry box***************************
data1 = StringVar()
data2 = StringVar()
data3 = StringVar()

dobdate = ttk.Entry(Lframe2, width = 5, textvariable= data1, justify=CENTER) 
dobmonth = ttk.Entry(Lframe2, width = 5, textvariable= data2, justify=CENTER)
dobyear = ttk.Entry(Lframe2, width = 10,  textvariable= data3, justify=CENTER)

datelabel = Label(Lframe2, bg = "gray82", fg = "black", text = "D", font = ("arial", 10 , "bold"))
monthlabel = Label(Lframe2, bg = "gray82", fg = "black", text = "M", font = ("arial", 10 , "bold"))
yearlabel = Label(Lframe2, bg = "gray82", fg = "black", text = "Y", font = ("arial", 10 , "bold"))



dobyear.pack(side= RIGHT, padx=10, ipady=3)
yearlabel.pack(side=RIGHT)

dobmonth.pack(side= RIGHT, padx=5, ipady=3)
monthlabel.pack(side=RIGHT)

dobdate.pack(side= RIGHT, padx=5, ipady=3)
datelabel.pack(side=RIGHT)


#******************codes for date of joining user input enytry box******************

jdata1 = StringVar()
jdata2 = StringVar()
jdata3 = StringVar()

jdate = ttk.Entry(Lframe3, width = 5, textvariable= jdata1, justify=CENTER) 
jmonth = ttk.Entry(Lframe3, width = 5, textvariable= jdata2, justify=CENTER)
jyear = ttk.Entry(Lframe3, width = 10,  textvariable= jdata3, justify=CENTER)

datelabel = Label(Lframe3, bg = "gray82", fg = "black", text = "D", font = ("arial", 10 , "bold"))
monthlabel = Label(Lframe3, bg = "gray82", fg = "black", text = "M", font = ("arial", 10 , "bold"))
yearlabel = Label(Lframe3, bg = "gray82", fg = "black", text = "Y", font = ("arial", 10 , "bold"))



jyear.pack(side= RIGHT, padx=10, ipady=3)
yearlabel.pack(side=RIGHT)

jmonth.pack(side= RIGHT, padx=5, ipady=3)
monthlabel.pack(side=RIGHT)

jdate.pack(side= RIGHT, padx=5, ipady=3)
datelabel.pack(side=RIGHT)

#***********************codes for date of retirement user input entry box**************
rdata1 = StringVar()
rdata2 = StringVar()
rdata3 = StringVar()

rdate = ttk.Entry(Lframe4, width = 5, textvariable= rdata1, justify=CENTER) 
rmonth = ttk.Entry(Lframe4, width = 5, textvariable= rdata2, justify=CENTER)
ryear = ttk.Entry(Lframe4, width = 10,  textvariable= rdata3, justify=CENTER)

datelabel = Label(Lframe4, bg = "gray82", fg = "black", text = "D", font = ("arial", 10 , "bold"))
monthlabel = Label(Lframe4, bg = "gray82", fg = "black", text = "M", font = ("arial", 10 , "bold"))
yearlabel = Label(Lframe4, bg = "gray82", fg = "black", text = "Y", font = ("arial", 10 , "bold"))



ryear.pack(side= RIGHT, padx=10, ipady=3)
yearlabel.pack(side=RIGHT)

rmonth.pack(side= RIGHT, padx=5, ipady=3)
monthlabel.pack(side=RIGHT)

rdate.pack(side= RIGHT, padx=5, ipady=3)
datelabel.pack(side=RIGHT)

#******************** codes for basic pay user input entry box**************


basicpay = ttk.Entry(Lframe5, width=31, justify = RIGHT, )
basicpay.pack(side= RIGHT, ipady=3, padx = 10)

#******************* codes for dropdown menu of commutation percentage************
# Combobox creation 

coummutper = ttk.Combobox(Lframe6, width = 7, values=["40","30","20","10"], state = "readonly") 
  

coummutper.pack(side = RIGHT, padx = 10) 
coummutper.current(0) # method to set default value

#******************* codes for age next birthday user input entry box*************

age = ttk.Entry(Lframe7, width = 10, justify = CENTER)
age.pack(side= RIGHT, padx = 10, ipady = 3)



#*****************************codes for output area*****************************

label1 = Label(
    Rframe1,
    text = "Basic Pension",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label1.pack(side = LEFT)

label2 = Label(
    Rframe2,
    text = "Regular Pension",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label2.pack(side = LEFT)

label3 = Label(
    Rframe3,
    text = "Family Pension",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label3.pack(side = LEFT)

label4 = Label(
    Rframe4,
    text = "Commuted Ammount",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label4.pack(side = LEFT)

label5 = Label(
    Rframe5,
    text = "Reduced Monthly Pension",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label5.pack(side = LEFT)

label6 = Label(
    Rframe6,
    text = "Total Qualifying Service",
    font = ("arial", 14),
    bg = "gray82",
    fg = "black",
    padx = 10,
    anchor = W
    
)
label6.pack(side = LEFT)

#*************** codes fof output field to display values****************

bpension = StringVar()
label1 = Label(
    Rframe1,
    textvariable = bpension,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = E,
    width = 12
    
)
label1.pack(side = RIGHT, padx=8)

mpension = StringVar()
label2 = Label(
    Rframe2,
    textvariable = mpension,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = E,
    width = 12
    
)
label2.pack(side = RIGHT, padx = 8)

fpension = StringVar()
label3 = Label(
    Rframe3,
    textvariable = fpension,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = E,
    width = 12
    
)
label3.pack(side = RIGHT, padx = 8)

cammount = StringVar()
label4 = Label(
    Rframe4,
    textvariable = cammount,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = E,
    width = 12
    
)
label4.pack(side = RIGHT, padx = 8)

rmpension = StringVar()
label5 = Label(
    Rframe5,
    textvariable = rmpension,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = E,
    width = 12
    
)
label5.pack(side = RIGHT, padx = 8)


#******* codes for qualifying service output*************

qmonth = StringVar()
label6 = Label(
    Rframe6,
    textvariable= qmonth,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = CENTER,
    width = 2
)

qyear = StringVar()
label7 = Label(
    Rframe6,
    textvariable = qyear,
    font = ("arial"),
    bg = "white",
    fg = "black",
    padx = 10,
    anchor = CENTER,
    width = 2
)

monthlabel = Label(Rframe6, bg = "gray82", fg = "black", text = "M", font = ("arial", 10 , "bold"))
yearlabel = Label(Rframe6, bg = "gray82", fg = "black", text = "Y", font = ("arial", 10 , "bold"))


label6.pack(side = RIGHT, padx = 8)
monthlabel.pack(side= RIGHT)
label7.pack(side = RIGHT, padx = 8)
yearlabel.pack(side= RIGHT)




root.mainloop()