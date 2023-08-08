
from tkinter import messagebox
import pymysql
import os
import tkinter
from tkinter import *
from tkinter import scrolledtext, messagebox, ttk, filedialog
from PIL import Image, ImageTk
import customtkinter


def login_user():
    if dr_name_entry.get() == "" or hospital_id_entry.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=loin_root)
    else:
        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()

            cur.execute("select * from doctor where Doctorname=%s and HospitalID= %s",
                        (dr_name_entry.get(), hospital_id_entry.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid User drname and hospital_id", parent=loin_root)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=loin_root)
                loin_root.destroy()
                import home_test5


            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=loin_root)


def signup_page():
    loin_root.destroy()
    import register


loin_root = Tk()
loin_root.title("Login ")
photo = PhotoImage(file="Logo/login.png")
loin_root.iconphoto(False, photo)
width = loin_root.winfo_screenwidth()
height = loin_root.winfo_screenheight()
loin_root.geometry("{}x{}+0+0".format(loin_root.winfo_screenwidth(), loin_root.winfo_screenheight()))

imgTemp = Image.open("Background/img.png")
# img2 = imgTemp.resize((height,1800))
img2 = imgTemp.resize((width, height))
img = ImageTk.PhotoImage(img2)

label = Label(loin_root, image=img)
label.pack(side='top', fill=Y, expand=True)

frame = customtkinter.CTkFrame(master=loin_root,
                               width=780,
                               height=380,
                               corner_radius=10,
                               fg_color="#00B2C6",
                               border_width=1.5,
                               border_color="#02808A",

                               )
frame.place(relx=0.5, rely=0.59, anchor=tkinter.CENTER)

icon = ImageTk.PhotoImage(Image.open("icons/dr name.png"))
l1 = Label(frame, image=icon, bg="#00B2C6")
l1.place(relx=0.06, rely=0.19)

icon1 = ImageTk.PhotoImage(Image.open("icons/id.png"))
l1 = Label(frame, image=icon1, bg="#00B2C6")
l1.place(relx=0.059, rely=0.43)

dr_name_entry = customtkinter.CTkEntry(master=frame,
                                       width=550,
                                       height=50,
                                       corner_radius=15,
                                       placeholder_text="Dr Name",
                                       font=('Inter', 16),
                                       fg_color="#F5F5F5",
                                       border_color="#F5F5F5",

                                       )
dr_name_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

text = dr_name_entry.get()

hospital_id_entry = customtkinter.CTkEntry(master=frame,
                                           width=550,
                                           height=50,
                                           corner_radius=15,
                                           placeholder_text="Hospital Id",
                                           font=('Inter', 16),
                                           fg_color="#F5F5F5",
                                           border_color="#F5F5F5",

                                           )
hospital_id_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

text = hospital_id_entry.get()

button = customtkinter.CTkButton(master=frame,
                                 text="Login",
                                 font=('Inter', 20),
                                 text_color='#FFFFFF',
                                 command=login_user,
                                 width=200,
                                 height=40,
                                 border_width=0,
                                 corner_radius=8,
                                 fg_color="#02808A",
                                 border_color="#F5F5F5",
                                 )
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

txt = Label(frame, text="  Don’t have an account?  ",
            fg='#F5F5F5', font=('Inter', 13,), background="#00B2C6")
txt.place(relx=0.3, rely=0.81)




button2 = customtkinter.CTkButton(master=frame,
                                  text="Sign Up",
                                  font=('Inter', 16, "bold"),
                                  text_color='#02808A',
                                  command=signup_page,
                                  width=60,
                                  height=40,
                                  border_width=0,
                                  corner_radius=8,
                                  fg_color="#00B2C6",
                                  border_color="#FFFFFF",
                                  hover_color="#FFFFFF"
                                  )
button2.place(relx=0.6, rely=0.85, anchor=tkinter.CENTER)

loin_root.mainloop()

