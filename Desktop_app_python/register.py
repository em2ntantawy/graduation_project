import os
import tkinter
from tkinter import *

from PIL import Image, ImageTk
import customtkinter

from tkinter import messagebox
import pymysql
import time
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error


def login_page():
    register_window.destroy()
    import login

def clear():
    dr_name_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    hospital_id_entry.delete(0, END)


def connect_database():
    if dr_name_entry.get() == "" or email_entry.get() == "" or phone_entry.get() == "" or hospital_id_entry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required", parent=register_window)
    elif hospital_id_entry.get() != hospital_id_entry.get():
        messagebox.showerror("Error", "Hospital_id not correct", parent=register_window)
    else:
        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()
            cur.execute("select * from doctor where Doctorname=%s and HospitalID= %s",
                        (dr_name_entry.get(), hospital_id_entry.get()))
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "You already have an account", parent=register_window)
            else:
                cur.execute(
                    "insert into doctor(Doctorname, Doctoremail,Doctorphomne,HospitalID) values(%s,%s,%s,%s)",
                    (
                        dr_name_entry.get(),
                        email_entry.get(),
                        phone_entry.get(),
                        hospital_id_entry.get(),

                    ))

                con.commit()
                con.close()
                messagebox.showinfo("Success", "Ragistration Successfull", parent=register_window)
                clear()
                register_window.destroy()
                import home_test5

        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=register_window)






#signup screen
register_window = Tk()
register_window.title("Registration")
photo = PhotoImage(file="Logo/register.png")
register_window.iconphoto(False, photo)
# window.overrideredirect(1)
# Set Geometry
register_window.geometry(
    "{}x{}+0+0".format(register_window.winfo_screenwidth(), register_window.winfo_screenheight()))
width = register_window.winfo_screenwidth()
height = register_window.winfo_screenheight()

imgTemp = Image.open("Background/img.png")
img2 = imgTemp.resize((height, 1800))
img2 = imgTemp.resize((width, height))
img = ImageTk.PhotoImage(img2)

label = Label(register_window, image=img)
label.pack(side='top', fill=Y, expand=True)

frame = customtkinter.CTkFrame(master=register_window,
                               width=780,
                               height=580,
                               corner_radius=10,
                               fg_color="#00B2C6",
                               border_width=1.5,
                               border_color="#02808A",

                               )
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

icon = ImageTk.PhotoImage(Image.open("icons/dr name.png"))
l1 = Label(frame, image=icon, bg="#00B2C6")
l1.place(relx=0.05, rely=0.1)

icon1 = ImageTk.PhotoImage(Image.open("icons/email.png"))
# resized_image= icon1.resize((32,32), Image.ANTIALIAS)
l1 = Label(frame, image=icon1, bg="#00B2C6")
l1.place(relx=0.05, rely=0.3)

icon2 = ImageTk.PhotoImage(Image.open("icons/phone.png"))
l1 = Label(frame, image=icon2, bg="#00B2C6")
l1.place(relx=0.05, rely=0.48)

icon3 = ImageTk.PhotoImage(Image.open("icons/id.png"))
l1 = Label(frame, image=icon3, bg="#00B2C6")
l1.place(relx=0.05, rely=0.61)

# entry box
dr_name_entry = StringVar()
dr_name_entry = StringVar()
email_entry = StringVar()
hospital_id_entry = StringVar()

dr_name_entry = customtkinter.CTkEntry(master=frame,
                                       width=550,
                                       height=50,
                                       corner_radius=15,
                                       placeholder_text="Dr Name",
                                       font=('Inter', 16),
                                       fg_color="#F5F5F5",
                                       border_color="#F5F5F5",

                                       )
dr_name_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

text = dr_name_entry.get()

email_entry = customtkinter.CTkEntry(master=frame,
                                     width=550,
                                     height=50,
                                     corner_radius=15,
                                     placeholder_text="Email",
                                     font=('Inter', 16),
                                     fg_color="#F5F5F5",
                                     border_color="#F5F5F5",

                                     )
email_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

text = email_entry.get()

phone_entry = customtkinter.CTkEntry(master=frame,
                                     width=550,
                                     height=50,
                                     corner_radius=15,
                                     placeholder_text="Phone",
                                     font=('Inter', 16),
                                     fg_color="#F5F5F5",
                                     border_color="#F5F5F5",

                                     )
phone_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
text = phone_entry.get()

hospital_id_entry = customtkinter.CTkEntry(master=frame,
                                           width=550,
                                           height=50,
                                           corner_radius=15,
                                           placeholder_text="Hospital Id",
                                           font=('Inter', 16),
                                           fg_color="#F5F5F5",
                                           border_color="#F5F5F5",

                                           )
hospital_id_entry.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

text = hospital_id_entry.get()

button = customtkinter.CTkButton(master=frame,
                                 text="Register",
                                 font=('Inter', 20),
                                 text_color='#FFFFFF',
                                 command= connect_database,
                                 width=180,
                                 height=40,
                                 border_width=0,
                                 corner_radius=12,
                                 fg_color="#02808A",
                                 border_color="#F5F5F5",

                                 )
button.place(relx=0.5, rely=0.80, anchor=tkinter.CENTER)

txt = Label(frame, text="   Already have an account?  ",
            fg='#F5F5F5', font=('Inter', 13,), background="#00B2C6")
txt.place(x=250, y=510)

button = customtkinter.CTkButton(master=frame,
                                 text="Login ",
                                 font=('Inter', 14, "bold"),
                                 text_color='#02808A',
                                 cursor='hand2',
                                 command=login_page,
                                 width=60,
                                 height=40,
                                 border_width=0,
                                 corner_radius=8,
                                 fg_color="#00B2C6",
                                 border_color="#FFFFFF",
                                 hover_color="#FFFFFF"
                                 )
button.place(x=490, y=523, anchor=tkinter.CENTER)
register_window.grid_rowconfigure(0, weight=1)
register_window.grid_columnconfigure(0, weight=1)

# Execute Tkinter
register_window.mainloop()
