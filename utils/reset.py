from tkinter import StringVar
from tkinter.constants import END


def reset_fun(basic_pension_str_var, regular_pension_str_var, family_pension_str_var, commuted_ammount_str_var, reduced_monthly_pension_str_var, total_qualifying_service_year_str_var, total_qualifying_service_month_str_var, dobdate_entry, dobmonth_entry, dobyear_entry, jdate_entry, jmonth_entry, jyear_entry, rdate_entry, rmonth_entry, ryear_entry, basicpay_entry, age_entry, typeRetirement, coummutper):
    basic_pension_str_var.set("")
    regular_pension_str_var.set("")
    family_pension_str_var.set("")
    commuted_ammount_str_var.set("")
    reduced_monthly_pension_str_var.set("")
    total_qualifying_service_month_str_var.set("")
    total_qualifying_service_year_str_var.set("")
    dobdate_entry.delete(0, END)
    dobmonth_entry.delete(0, END)
    dobyear_entry.delete(0, END)
    jdate_entry.delete(0, END)
    jmonth_entry.delete(0, END)
    jyear_entry.delete(0, END)
    rdate_entry.delete(0, END)
    rmonth_entry.delete(0, END)
    ryear_entry.delete(0, END)
    basicpay_entry.delete(0, END)
    age_entry.delete(0, END)
    typeRetirement.current(0)
    coummutper.current(0)
