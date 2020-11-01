# MIT License
# 
# Copyright (c) 2020 Rokibul Islam, Pujan Talukder
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

#Changed folder structure, hence lost contirbutions history, referer to https://github.com/rokibulislaam/pension-calculator/commit/00bc59100c2546656e341ca5364f78ffe474f0a8 to see commits until changing the folder structure

import os
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, StringVar, messagebox
from tkinter.constants import BOTH, CENTER, E, FLAT, LEFT, RIGHT, TOP, TRUE, W, X
from tkinter.ttk import Combobox
from utils.reset import reset_fun
from utils.get_commutation_value import get_commutation_value
from utils.calc_basic_pay import cal_basic_pay

# ******** definition of functions***************************************

tempdate = 0   # global variable
tempmonth = 0  # global variable
tempyear = 0   # global variable
tempbpension = 0      # global variable
typeofretirement = "Select"  # global variable
percentageofComm = "Select"  # global variable


def cal_service():
    global tempdate, tempmonth, tempyear
    tempdate = (int(rdate.get()) - int(jdate.get()))
    tempmonth = (int(rmonth.get()) - int(jmonth.get()))
    tempyear = (int(ryear.get()) - int(jyear.get()))
    if(int(jmonth.get()) > int(rmonth.get())):
        tempyear = tempyear - 1
        # function to convert negative num into positive num
        tempmonth = abs(tempmonth)


def cal_retirement():
    rtempyear = (60 + int(dobyear.get()))
    rtempmonth = int(dobmonth.get())
    rtempdate = int(dobdate.get())
    r_date.set(str(rtempdate))
    r_month.set(str(rtempmonth))
    r_year.set(str(rtempyear))


def cal_service_years():
    global tempdate, tempmonth, tempyear
    tempdate = (int(rdate.get()) - int(jdate.get()))
    tempmonth = (int(rmonth.get()) - int(jmonth.get()))
    tempyear = (int(ryear.get()) - int(jyear.get()))
    if(int(jmonth.get()) > int(rmonth.get())):
        tempyear = tempyear - 1
        # function to convert negative num into positive num
        tempmonth = abs(tempmonth)
    return tempyear


def calculate_pension():
    if(cal_service_years() < 20):
        messagebox.showerror(
            title=None, message="No Pension! (Service is less than 20 years)")
    else:
        # if user keep basic pay entry box empty then no funtion will be called
        tempbpension = cal_basic_pay(basicpay_widget=basicpay)
        bpension.set(tempbpension)
        mpension.set(tempbpension)
        # 30% of basic paysclae for family pension
        fpension.set(int(basicpay.get()) * 0.3)
        cammount.set("N/A")
        rmpension.set("N/A")
        cal_service()
        qmonth.set(tempmonth)
        qyear.set(tempyear)


def cal_commutation():
    if(coummutper.get() and age.get()):
        percentage_of_basic_payscale = float(
            bpension.get()) * int(coummutper.get())/100
        age_next_birthday = int(age.get())
        commutation = 12 * \
            int(get_commutation_value(age_next_birthday)) * \
            int(percentage_of_basic_payscale)
        global cammount
        global rmpension
        cammount.set(commutation)
        rmpension.set(float(bpension.get()) - percentage_of_basic_payscale)


root = tk.Tk()


# color will be used gray70
root.geometry("1200x700+115+15")
root.resizable(0, 0)
root.title("Pension_Calculator")
root.iconbitmap(os.path.join(os.getcwd(), 'icons', 'pcalcy1.ico'))

# ********************* codes for main frame and sub frame******************************

header = Frame(root, bg="white")
header.pack(fill=X, side=TOP)

centreframe = Frame(root, bg="white")
centreframe.pack(fill=BOTH, side=TOP, expand=TRUE)

leftframe = Frame(centreframe, bg="gray82", padx=8, pady=8)
leftframe.pack(expand=TRUE, fill=BOTH, side=LEFT, padx=20, pady=20)

rightframe = Frame(centreframe, bg="gray82", padx=8, pady=8)
rightframe.pack(expand=TRUE, fill=BOTH, side=LEFT, padx=20, pady=20)


# **************** codes for header label****************************************************

heading = Label(
    header,
    text="BASIC PENSION AND COMMUTATION CALCULATOR",
    font=("Product Sans", 22, "bold"),
    bg="white",
    fg="black",
)
heading.pack(expand=TRUE, fill=X, pady=6)

# ********************codes for left frames and labels user inputs section****************

heading1 = Label(
    leftframe,
    text="ENTER DATA TO CALCULATE PENSION AND COMMUTATION",
    font=("arial", 15, "bold"),
    fg="black",
    bg="gray82",
    pady=2
)
heading1.pack(side=TOP)

Lframe1 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1,
                pady=0
                )
Lframe1.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Lframe2 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )

Lframe2.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Lframe3 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )

Lframe3.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Lframe4 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )

Lframe4.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Lframe5 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )

Lframe5.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)


submitbutton1 = Button(
    leftframe,
    text="SUBMIT",
    font=("arial", 13, "bold"),
    fg="black",
    bg="gray45",
    relief=FLAT,
    padx=6,
    pady=2,
    activebackground="black",
    activeforeground="white",
    command=calculate_pension

)
submitbutton1.pack(pady=8)

Lframe6 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )

Lframe6.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Lframe7 = Frame(leftframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )

Lframe7.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

submitbutton2 = Button(
    leftframe,
    text="SUBMIT",
    font=("arial", 13, "bold"),
    fg="black",
    bg="gray45",
    relief=FLAT,
    padx=6,
    pady=2,
    activebackground="black",
    activeforeground="white",
    command=cal_commutation

)
submitbutton2.pack(pady=5)

# ********************codes for left frames and labels user inputs section****************

heading2 = Label(
    rightframe,
    text="PENSION AND COMMUTED VALUE",
    font=("arial", 15, "bold"),
    fg="black",
    bg="gray82"
)
heading2.pack(side=TOP)

Rframe1 = Frame(rightframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )
Rframe1.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Rframe2 = Frame(rightframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )
Rframe2.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Rframe3 = Frame(rightframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )
Rframe3.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Rframe4 = Frame(rightframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )
Rframe4.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Rframe5 = Frame(rightframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )
Rframe5.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)

Rframe6 = Frame(rightframe,
                bg="gray82",
                bd=1,
                highlightbackground="black",
                highlightthickness=1
                )
Rframe6.pack(expand=TRUE, fill=BOTH, padx=8, pady=5)


# ************************ codes for input field***********************
label1 = Label(
    Lframe2,
    text="Type of Retirement",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label1.pack(side=LEFT)

label2 = Label(
    Lframe1,
    text="Date of Birth",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label2.pack(side=LEFT)

label3 = Label(
    Lframe3,
    text="Date of Joining",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label3.pack(side=LEFT)

label4 = Label(
    Lframe4,
    text="Date of Retirement",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label4.pack(side=LEFT)

label5 = Label(
    Lframe5,
    text="Basic Pay or Average of Last 10 month Emoluments",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label5.pack(side=LEFT)

label6 = Label(
    Lframe6,
    text="Percentage of Commutation(Max 40%)",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label6.pack(side=LEFT)

label7 = Label(
    Lframe7,
    text="Age Next Birth Day(age at retirement + 1 year)",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label7.pack(side=LEFT)

# ********************codes for dropdown user inputs****************
# Combobox creation

typeRetirement = Combobox(Lframe2, width=28, values=[
    "Select", "Superannuation", "VRS"], state="readonly")


typeRetirement.pack(side=RIGHT, padx=10)
typeRetirement.current(0)  # method to set default value


def change_combobox_value(eventObject):
    if(eventObject.widget.get() == "Superannuation" and eventObject.widget.get()):
        cal_retirement()


typeRetirement.bind('<<ComboboxSelected>>', change_combobox_value)


# ******************* enrty input filed for DOB user input entry box***************************


dobdate = Entry(Lframe1, width=5, justify=CENTER)
dobmonth = Entry(Lframe1, width=5, justify=CENTER)
dobyear = Entry(Lframe1, width=10, justify=CENTER)

datelabel = Label(Lframe1, bg="gray82", fg="black",
                  text="D", font=("arial", 10, "bold"))
monthlabel = Label(Lframe1, bg="gray82", fg="black",
                   text="M", font=("arial", 10, "bold"))
yearlabel = Label(Lframe1, bg="gray82", fg="black",
                  text="Y", font=("arial", 10, "bold"))


dobyear.pack(side=RIGHT, padx=10, ipady=3)
yearlabel.pack(side=RIGHT)

dobmonth.pack(side=RIGHT, padx=5, ipady=3)
monthlabel.pack(side=RIGHT)

dobdate.pack(side=RIGHT, padx=5, ipady=3)
datelabel.pack(side=RIGHT)


# ******************codes for date of joining user input enytry box******************

jdate = Entry(Lframe3, width=5,  justify=CENTER)
jmonth = Entry(Lframe3, width=5, justify=CENTER)
jyear = Entry(Lframe3, width=10, justify=CENTER)

datelabel = Label(Lframe3, bg="gray82", fg="black",
                  text="D", font=("arial", 10, "bold"))
monthlabel = Label(Lframe3, bg="gray82", fg="black",
                   text="M", font=("arial", 10, "bold"))
yearlabel = Label(Lframe3, bg="gray82", fg="black",
                  text="Y", font=("arial", 10, "bold"))


jyear.pack(side=RIGHT, padx=10, ipady=3)
yearlabel.pack(side=RIGHT)

jmonth.pack(side=RIGHT, padx=5, ipady=3)
monthlabel.pack(side=RIGHT)

jdate.pack(side=RIGHT, padx=5, ipady=3)
datelabel.pack(side=RIGHT)

# ***********************codes for date of retirement user input entry box**************
r_date = StringVar()
r_month = StringVar()
r_year = StringVar()

rdate = Entry(Lframe4, width=5, textvariable=r_date, justify=CENTER)
rmonth = Entry(Lframe4, width=5, textvariable=r_month, justify=CENTER)
ryear = Entry(Lframe4, width=10, textvariable=r_year, justify=CENTER)

datelabel = Label(Lframe4, bg="gray82", fg="black",
                  text="D", font=("arial", 10, "bold"))
monthlabel = Label(Lframe4, bg="gray82", fg="black",
                   text="M", font=("arial", 10, "bold"))
yearlabel = Label(Lframe4, bg="gray82", fg="black",
                  text="Y", font=("arial", 10, "bold"))


ryear.pack(side=RIGHT, padx=10, ipady=3)
yearlabel.pack(side=RIGHT)

rmonth.pack(side=RIGHT, padx=5, ipady=3)
monthlabel.pack(side=RIGHT)

rdate.pack(side=RIGHT, padx=5, ipady=3)
datelabel.pack(side=RIGHT)

# ******************** codes for basic pay user input entry box**************


basicpay = Entry(Lframe5, width=31, justify=RIGHT, )
basicpay.pack(side=RIGHT, ipady=3, padx=10)

# ******************* codes for dropdown menu of commutation percentage************
# Combobox creation

coummutper = Combobox(Lframe6, width=7, values=[
    "Select", "40", "30", "20", "10"], state="readonly")


coummutper.pack(side=RIGHT, padx=10)
coummutper.current(0)  # method to set default value


# def set_percentage_comm_val(event):
#     percentage_of_comm = event.widget.get()
#     if(event.Widget.get() != 'Select'):
#         cal_commutation(percentage_of_comm)


# coummutper.bind('<<ComboboxSelected>>', set_percentage_comm_val)

# ******************* codes for age next birthday user input entry box*************

age = Entry(Lframe7, width=10, justify=CENTER)
age.pack(side=RIGHT, padx=10, ipady=3)


# *****************************codes for output area*****************************
# ********* name labels ************
label1 = Label(
    Rframe1,
    text="Basic Pension",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label1.pack(side=LEFT)

label2 = Label(
    Rframe2,
    text="Regular Pension",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label2.pack(side=LEFT)

label3 = Label(
    Rframe3,
    text="Family Pension",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label3.pack(side=LEFT)

label4 = Label(
    Rframe4,
    text="Commuted Ammount",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label4.pack(side=LEFT)

label5 = Label(
    Rframe5,
    text="Reduced Monthly Pension",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label5.pack(side=LEFT)

label6 = Label(
    Rframe6,
    text="Total Qualifying Service",
    font=("arial", 14),
    bg="gray82",
    fg="black",
    padx=10,
    anchor=W

)
label6.pack(side=LEFT)

# *************** codes for output field to display values****************

bpension = StringVar()
label1 = Label(
    Rframe1,
    textvariable=bpension,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=E,
    width=12
)
label1.pack(side=RIGHT, padx=8)

mpension = StringVar()
label2 = Label(
    Rframe2,
    textvariable=mpension,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=E,
    width=12

)
label2.pack(side=RIGHT, padx=8)

fpension = StringVar()
label3 = Label(
    Rframe3,
    textvariable=fpension,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=E,
    width=12

)
label3.pack(side=RIGHT, padx=8)
cammount = StringVar()

label4 = Label(
    Rframe4,
    textvariable=cammount,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=E,
    width=12

)
label4.pack(side=RIGHT, padx=8)

rmpension = StringVar()
label5 = Label(
    Rframe5,
    textvariable=rmpension,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=E,
    width=12

)
label5.pack(side=RIGHT, padx=8)


# ******* codes for qualifying service output*************

qmonth = StringVar()
label6 = Label(
    Rframe6,
    textvariable=qmonth,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=CENTER,
    width=2
)

qyear = StringVar()
label7 = Label(
    Rframe6,
    textvariable=qyear,
    font=("arial"),
    bg="white",
    fg="black",
    padx=10,
    anchor=CENTER,
    width=2
)


# ********** Reset Button ******************


reset = Button(
    rightframe,
    text="RESET",
    font=("arial", 13, "bold"),
    fg="black",
    bg="gray45",
    relief=FLAT,
    padx=8,
    pady=2,
    activebackground="black",
    activeforeground="white",
    command=lambda: reset_fun(bpension, mpension, fpension,
                              cammount, rmpension, qmonth, qyear, dobdate, dobmonth, dobyear, jdate, jmonth, jyear, rdate, rmonth, ryear, basicpay, age,  typeRetirement, coummutper)
)
reset.pack(pady=10)

monthlabel = Label(Rframe6, bg="gray82", fg="black",
                   text="M", font=("arial", 10, "bold"))
yearlabel = Label(Rframe6, bg="gray82", fg="black",
                  text="Y", font=("arial", 10, "bold"))


label6.pack(side=RIGHT, padx=8)
monthlabel.pack(side=RIGHT)
label7.pack(side=RIGHT, padx=8)
yearlabel.pack(side=RIGHT)


if __name__ == "__main__":
    root.mainloop()
