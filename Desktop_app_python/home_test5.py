import os
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk, filedialog
from tkinter.filedialog import asksaveasfile
from datetime import datetime
from PIL import ImageGrab
import cv2
import image
import numpy as np
from PIL import Image, ImageTk
import customtkinter
import pymysql
import time
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error
import mysql.connector
from mysql.connector import pooling
from mysql.connector import Error
import glob
import io

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='battettsesophagus',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.title('Barrett’s Esophagus')
photo = PhotoImage(file="Logo/img.png")
root.iconphoto(False, photo)

cam_on = False
cap = None
out = None
now = datetime.now()
month = now.month
year = now.year
day = now.day
path = tk.StringVar()
# Receiving user's file_path selection
Name_folder= tk.StringVar()
path = "./" + str(year) + "_" + str(month) + "_" + str(day)
path2 = os.path.join("./" + str(year) + "_" + str(month) + "_" + str(day), Name_folder.get())


def report_next():
    root.destroy()
    import home

def Report_page():
    global name, age, first_data, follow_up_data, file_no, sex, refferig_doctor, premedication, scr, scr2, scr3, scr4, scr5, scr6, scr7, sig, patient_id, pic1, pic2, pic3

    def convertToBinaryData(filename):

      # Convert digital data to binary format
       with open(filename, 'rb') as file:
           binaryData = file.read()
       return binaryData

    # Insert to Database Report
    def save_patient():
        global pic1, pic2, pic3
        if entry_name.get() == "" or entry_age.get() == "" or entry_first_data.get() == "" or  entry_file_no.get() == "" or entry_sex.get() == "" or entry_refferig_doctor.get() == "" or entry_premedication.get() == "" or scr.get(
                1.0, END) == "" or scr2.get(1.0, END) == "" or scr3.get(1.0, END) == "" or scr4.get(1.0,
                                                                                                    END) == "" or scr5.get(
                1.0, END) == "" or scr6.get(1.0, END) == "" or scr7.get(1.0,
                                                                        END) == "" or entry_sig.get() == "" or entry_patient_id.get() == "":
            messagebox.showerror("Error", "Should You Add All Fields", parent=root)
        elif entry_file_no.get() != entry_file_no.get():
            messagebox.showerror("Error", "Hospital_id not correct", parent=root)
        else:
            try:
                con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
                cur = con.cursor()

                cur.execute(
                    "insert into reoprt(name,age,firstdata,followup,fileno,sex,refferingdoctor,permedication,proceduretechique,indication,esophagus,stomach,pyloricring,duodenum,conclusion,signature,idpatient,imgs,img2,img3) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        entry_name.get(),
                        entry_age.get(),
                        entry_first_data.get(),
                        entry_follow_up_data.get(),
                        entry_file_no.get(),
                        entry_sex.get(),
                        entry_refferig_doctor.get(),
                        entry_premedication.get(),
                        scr.get('1.0', 'end-1c'),
                        scr2.get('1.0', 'end-1c'),
                        scr3.get('1.0', 'end-1c'),
                        scr4.get('1.0', 'end-1c'),
                        scr5.get('1.0', 'end-1c'),
                        scr6.get('1.0', 'end-1c'),
                        scr7.get('1.0', 'end-1c'),
                        entry_sig.get(),
                        entry_patient_id.get(),
                        pic1,
                        pic2,
                        pic3,
                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "The report was successfully saved", parent=root)
                clear()
            # switch()
            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=root)

    # function to delete report
    def delete_report():

        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()
            cur.execute("delete from reoprt where proceduretechique=%s", scr.get('1.0', 'end-1c'))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "The report was successfully delet", parent=root)
            clear()
        # switch()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=root)

            # function to update reprt

    def update_report():
        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()

            cur.execute(
                "update reoprt set name=%s,age=%s,firstdata=%s,followup=%s,fileno=%s,sex=%s,refferingdoctor=%s,permedication=%s,proceduretechique=%s,indication=%s,esophagus=%s,stomach=%s,pyloricring=%s,duodenum=%s,conclusion=%s,signature=%s,idpatient=%s,imgs=%s,img2=%s,img3=%s where idpatient=%s",
                (
                    entry_name.get(),
                    entry_age.get(),
                    entry_first_data.get(),
                    entry_follow_up_data.get(),
                    entry_file_no.get(),
                    entry_sex.get(),
                    entry_refferig_doctor.get(),
                    entry_premedication.get(),
                    scr.get('1.0', 'end-1c'),
                    scr2.get('1.0', 'end-1c'),
                    scr3.get('1.0', 'end-1c'),
                    scr4.get('1.0', 'end-1c'),
                    scr5.get('1.0', 'end-1c'),
                    scr6.get('1.0', 'end-1c'),
                    scr7.get('1.0', 'end-1c'),
                    entry_sig.get(),
                    entry_patient_id.get(),
                    pic1,
                    pic2,
                    pic3,
                    entry_patient_id.get(),))

            con.commit()
            con.close()
            messagebox.showinfo("Success", "The report was successfully update", parent=root)


        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=root)

    def upload_file():
        global filename, img, f, pic1, pic2, pic3
        f_types = [('Jpg Files', '*.jpg'),
                   ('PNG Files', '*.png')]  # type of files to select
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)

        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((220, 190))  # new width & height
            img = ImageTk.PhotoImage(img)
            e1 = tk.Label(root)
            e1.place(x=1100, y=70)
            e1.image = img  # keep a reference! by attaching it to a widget attribute
            e1['image'] = img  # Show Image
            pic1 = convertToBinaryData(f)
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((220, 190))  # new width & height
            img = ImageTk.PhotoImage(img)
            e2 = tk.Label(root)
            e2.place(x=1100, y=260)
            e2.image = img  # keep a reference! by attaching it to a widget attribute
            e2['image'] = img  # Show Image
            pic2 = convertToBinaryData(f)
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
        for f in filename:
            img = Image.open(f)  # read the image file
            img = img.resize((220, 190))  # new width & height
            img = ImageTk.PhotoImage(img)
            e3 = tk.Label(root)
            e3.place(x=1100, y=450)
            e3.image = img  # keep a reference! by attaching it to a widget attribute
            e3['image'] = img  # Show Image
            pic3 = convertToBinaryData(f)

    rgb = None

    def save_report_as_image():
        save_path = filedialog.asksaveasfilename(defaultextension=".png", initialdir=path2)
        # Get the coordinates and dimensions of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Get the coordinates and dimensions of the tkinter window
        window_x = root.winfo_rootx()
        window_y = root.winfo_rooty()
        window_width = root.winfo_width()
        window_height = root.winfo_height()

        # Calculate the bounding box based on screen and window dimensions
        x = max(0, window_x)
        y = max(0, window_y)
        width = min(screen_width - x, window_width)
        height = min(screen_height - y, window_height)

        # Capture the screenshot of the tkinter window
        image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

        # Save the image as a file
        image.save(save_path)
        print("Report saved as report.png")

    report_frame = tk.Frame(main_frame)

    # report_frame.config(bg="#D1EAF0")
    def on_resize(event):
        photo = Image.open('background/img.png')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img = tk.Label()
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    # input_text = StringVar()
    name = StringVar()
    eage = IntVar()
    first_data = StringVar()
    follow_up_data = StringVar()
    file_no = StringVar()
    esex = StringVar()
    refferig_doctor = StringVar()
    premedication = StringVar()
    sig = StringVar()
    patient_id = StringVar()
    pic1 = BooleanVar()
    pic2 = BooleanVar()
    pic3 = BooleanVar()

    # top = Tk()

    l1= Label(text="Barrett's Esophagus Report",bg='#9FBEBE',fg='#000000')
    l1.place(x=600,y=8)

    l1.config(font=('bold',12))

    label_head_result = Label(text="   Name:  ", bg="#D1EAF0",
                              fg='black', font=("Inter,bold"))

    label_head_result.place(x=15, y=40)
    entry_name = tk.Entry(textvariable=name, bd=1)
    entry_name.place(x=80, y=42, width=180)
    # text=entry_name.get()
    # name=StringVar()

    age = Label(text="   Age:  ", bg='#D1EAF0',
                fg='black', font=("Inter,bold"))
    age.place(x=235, y=40)
    entry_age = tk.Entry(textvariable=eage, bd=1)
    entry_age.place(x=285, y=42, width=50)
    #age = StringVar()

    data = Label(text="First Data:  ", bg='#D1EAF0',
                 fg='black', font=("Inter,bold"))
    data.place(x=350, y=40)
    entry_first_data = tk.Entry(textvariable=first_data, bd=1)
    entry_first_data.place(x=430, y=42)
    # first_data=StringVar()

    data_up = Label(text="Follow UP Data:  ", bg='#D1EAF0',
                    fg='black', font=("Inter,bold"))
    data_up.place(x=570, y=40)
    entry_follow_up_data = tk.Entry(textvariable=follow_up_data, bd=1)
    entry_follow_up_data.place(x=688, y=42)
    # follow_up_data=StringVar()

    file = Label(text="fileNO:  ", bg='#D1EAF0',
                 fg='black', font=("Inter,bold"))
    file.place(x=820, y=40)
    entry_file_no = tk.Entry(textvariable=file_no, bd=1)
    entry_file_no.place(x=875, y=42, width=120)
    # file_no=StringVar()

    sex = Label(text="Sex:  ", bg='#D1EAF0',
                fg='black', font=("Inter,bold"))
    sex.place(x=999, y=40)
    entry_sex = tk.Entry(textvariable=esex, bd=1)
    entry_sex.place(x=1045, y=42, width=80)
    #sex = StringVar()

    rd = Label(text="Reffering Doctor:  ", bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 16))

    rd.place(x=10, y=100)
    entry_refferig_doctor = tk.Entry(textvariable=refferig_doctor, bd=1)
    entry_refferig_doctor.place(x=181, y=104, width=250)
    # refferig_doctor=StringVar()

    PR = Label(text="Premedication:  ", bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 16))

    PR.place(x=455, y=100)
    entry_premedication = tk.Entry(textvariable=premedication, bd=1)
    entry_premedication.place(x=610, y=104, width=250)
    # premedication=StringVar()
    scrolW = 90
    scrolH = 3
    # text=entry_premedication.get()

    label1 = Label(text='Procedure\nTechnique:', fg="#02808A", font=("Inter,bold", 16),
                   background="#D1EAF0")
    label1.place(x=13, y=150)
    scr = Text(bd=1, width=70, height=2, font=("Inter,bold", 16))
    scr.place(x=130, y=150, width=785)
    # text=scr.get('1.0', 'end-1c')

    label2 = Label(text='Indication:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label2.place(x=13, y=220)
    scr2 = Text(bd=1, width=65, height=2, font=("Inter,bold", 16))
    scr2.place(x=130, y=210)
    # text=scr2.get('1.0', 'end-1c')

    label3 = Label(text='Esophagus:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label3.place(x=13, y=290)
    scr3 = Text(bd=1, width=65, height=2, font=("Inter,bold", 16))
    scr3.place(x=130, y=280)
    # text=scr3.get('1.0', 'end-1c')

    label4 = Label(text='Stomach:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label4.place(x=13, y=360)
    scr4 = Text(bd=1, width=65, height=2, font=("Inter,bold", 16))
    scr4.place(x=130, y=350)
    # text=scr4.get('1.0', 'end-1c')

    label5 = Label(text='Pyloric Ring:', fg="#02808A", font=("Inter,bold", 15), background="#D1EAF0")
    label5.place(x=13, y=430)
    scr5 = Text(bd=1, width=65, height=2, font=("Inter,bold", 16))
    scr5.place(x=130, y=420)
    # text=scr5.get('1.0', 'end-1c')

    label6 = Label(text='Duodenum:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label6.place(x=13, y=500)
    scr6 = Text(bd=1, width=65, height=2, font=("Inter,bold", 16))
    scr6.place(x=130, y=490)
    # text=scr6.get('1.0', 'end-1c')

    label7 = Label(text='Conclusion:', fg="#02808A", font=("Inter,bold", 16), background="#D1EAF0")
    label7.place(x=13, y=570)
    scr7 = Text(bd=1, width=65, height=2, font=("Inter,bold", 16))
    scr7.place(x=130, y=560)
    # text=scr7.get('1.0', 'end-1c')

    label7 = Label(text='Signature:', fg="black", font=("Inter,bold", 15), background="#D1EAF0")
    label7.place(x=20, y=640)
    entry_sig = tk.Entry(textvariable=sig, bd=1)
    entry_sig.place(x=140, y=645, width=180, height=20)
    # sig=StringVar()
    # text=entry_sig.get()

    label8 = Label(text='Hospital ID:', fg="black", font=("Inter,bold", 15), background="#D1EAF0")
    label8.place(x=470, y=640)
    entry_patient_id = tk.Entry(textvariable=patient_id, bd=1)
    entry_patient_id.place(x=575, y=645, width=50)

    # patient_id=StringVar()
    # downlod data
    def read_Bloob():
        global name, age, first_data, follow_up_data, file_no, sex, refferig_doctor, premedication, scr, scr2, scr3, scr4, scr5, scr6, scr7, sig, patient_id, pic1, pic2, pic3

        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()
            sql = "select * from reoprt where idpatient like %s"
            val = entry_patient_id.get()
            cur.execute(sql, val)
            rows = cur.fetchall()
            for row in rows:
                # print(row[12])
                refferig_doctor.set(row[3])
                premedication.set(row[4])
                scr.delete(1.0, END)
                scr.insert('end-1c', row[5])
                scr2.delete(1.0, END)
                scr2.insert('end-1c', row[6])
                scr3.delete(1.0, END)
                scr3.insert('end-1c', row[7])
                scr4.delete(1.0, END)
                scr4.insert('end-1c', row[8])
                scr5.delete(1.0, END)
                scr5.insert('end-1c', row[9])
                scr6.delete(1.0, END)
                scr6.insert('end-1c', row[10])
                scr7.delete(1.0, END)
                scr7.insert('end-1c', row[11])
                name.set(row[12])
                eage.set(row[13])
                follow_up_data.set(row[14])
                file_no.set(row[15])
                esex.set(row[16])
                first_data.set(row[20])
                sig.set(row[17])

            con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=root)

            # text=entry_patient_id.get()

    # t1=Label(root,text="Result",fg="#02808A" ,font=("Bold", 15 ),background="white")
    # t1.place(x=1100 ,y=70)
    fram1 = ttk.Frame(width=220, height=190, relief=SUNKEN)
    fram1.place(x=1100, y=70)

    # t2=Label(root ,text= "follow", fg="#02808A" , font=('Bold',16),background="white")
    # t2.place (x=1100 ,y=360)
    fram2 = ttk.Frame(width=220, height=190, relief=SUNKEN)
    fram2.place(x=1100, y=260)

    fram2 = ttk.Frame(width=220, height=190, relief=SUNKEN)
    fram2.place(x=1100, y=450)

    # b1= button (root,text='Result',width=10 , background="white",fg="#02808A"  )
    # def subscribe():
    # return messagebox.showinfo('', 'The report was successfully saved')
    go_home_btn = Button(text="← Go to home", width=20, height=1, bg="#02808A", cursor="watch", fg="white",
                command=report_next)
    go_home_btn.place(x=1220, y=20, width=100)
    b1 = Button(text="Save", width=12, height=1, bg="#02808A", cursor="watch", fg="white",
                command=save_patient)
    b1.place(x=760, y=640)

    b1 = Button(text="Save Img", width=12, height=1, bg="white", cursor="watch", fg="#0C5B61",
                command=save_report_as_image)
    b1.place(x=860, y=640)
    b1 = Button(text="Update", width=12, height=1, bg="#02808A", cursor="watch", fg="white",
                command=update_report)
    b1.place(x=760, y=670)

    b1 = Button(text="Delete", width=12, height=1, bg="#02808A", cursor="watch", fg="white", command=delete_report)
    b1.place(x=860, y=670)

    b1 = tk.Button(root, text='Upload Images', width=15, bg="#02808A", fg="white", command=lambda: upload_file())

    b1.place(x=1090, y=650)
    b1 = tk.Button(root, text='Download Data', width=15, bg="#02808A", fg="white", command=read_Bloob)

    b1.place(x=1210, y=650)


    def switch():
        root.destroy()

    # clear data function
    def clear():
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_first_data.delete(0, END)
        entry_follow_up_data.delete(0, END)
        entry_file_no.delete(0, END)
        entry_sex.delete(0, END)
        entry_refferig_doctor.delete(0, END)
        entry_premedication.delete(0, END)
        entry_sig.delete(0, END)
        entry_patient_id.delete(0, END)
        scr.delete(1.0, END)
        scr2.delete(1.0, END)
        scr3.delete(1.0, END)
        scr4.delete(1.0, END)
        scr5.delete(1.0, END)
        scr6.delete(1.0, END)
        scr7.delete(1.0, END)


# ==========================================================================================================================

def result_page():

    video_frame = tk.Frame(main_frame)
    video_frame.configure(bg="#c7ebed")


    def on_resize(event):
        # resize the background image to the size of label
        #photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
        photo = Image.open('background/img.jpg') # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)


    img= tk.Label(video_frame)
    img.place(x=0, y=0,relwidth=1, relheight=1) # make label l to fit the parent window always
    img.bind('<Configure>', on_resize) # on_resi

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    imgTemp = Image.open("background/img.jpg")
    img2 = imgTemp.resize((height, 1800))
    img2 = imgTemp.resize((width, height))
    img = ImageTk.PhotoImage(img2)

    label = Label(video_frame, image=img)
    label.pack(side='top', fill=Y, expand=True)

    frame = tk.Frame(video_frame,width=500, height=300, relief=SUNKEN)
    frame.place(x=70, y=80)
    frame1 = tk.Frame(video_frame,width=250, height=250, relief=SUNKEN)
    frame1.place(x=180, y=400)
    var_photo = Variable()
    #img1 = Variable()
    def upload_file():
        global filename2
        #global var_photo
        f_types = [('JPG Files','*.jpg')]   # type of files to select
        filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)

        for f in filename:
            img=Image.open(f) # read the image file
            img=img.resize((500,300)) # new width & height
            img=ImageTk.PhotoImage(img)
            e1 =tk.Label(video_frame, width=500, height=300,)
            e1.place(x=70, y=80)
            #cv2.imshow("imgageee", img_up)
            e1.image = img # keep a reference! by attaching it to a widget attribute
            e1['image']=img
        #path = filename.lstrip("/").rstrip("/")

        #filename = re.sub(r"()", " ", filename)

        #filename = filename.replace("(","").replace(")","")
        #filename = *_filename
        #filename.rstrip('()')
        filename = str(filename)
        print(filename)
        filename2 = filename.lstrip("('").rstrip(",')")

        #filename = '"'+filename+'"'

        print(filename2)
        #path = filename[2:40]
        #print(filename[0:-1])
            #outfile = BytesIO()
            #print (outfile)

            #var_photo = img.get(outfile, "PNG")
            #var_photo.set(outfile.getvalue())
            #print(var_photo)
            #e1._image_ref = img
            #print(img)
            #foo = root.call(e1.cget('image'), 'cget', '-file')
            #cv2.imshow('')
            #print(foo)
            #bar = img['file']
            #print('1st image:\t%s\nEqual:\t%r' % (foo, bar, foo == bar))
            #img=ImageTk.PhotoImage(img)
            #img_up = img.cv2.copy()
            #print(img_up)
            #cv2.imshow("hj",img_up)
           # Show Image
        #filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)



    def result():
        global filename2,panel,line_image, img, line_img
        # Load the image
        print (filename2)
        #path2 = "'%s'" % (path)
        #print (path2)
        path = 'F:/final project/Desktop_app_python/Freezing Images/2.jpeg'
        image = cv2.imread(filename2)
        width = 250
        height = 250
        Original_Image = cv2.resize(image, (width, height))

        # Create a mask for the ROI using the grabcut algorithm
        mask = np.zeros(Original_Image.shape[:2], np.uint8)
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        rect = (10,10,225,225) # define the rectangle ROI here
        cv2.grabCut(Original_Image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        img= Original_Image*mask2[:,:,np.newaxis]
        cv2.imwrite("F:/final project/Desktop_app_python/Freezing Images/sample/ROI5.jpg",img)
        #cv2.imshow("Original Image", Original_Image)
        #cv2.imshow("ROI", img)

        # Convert the ROI to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        a_component = gray[:,:,1]

        # binary threshold the a-channel
        th = cv2.threshold(a_component,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]


        # function to obtain the largest contour in given image after filling it
        def get_region(image):
            contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            c = max(contours, key = cv2.contourArea)
            black = np.zeros((image.shape[0], image.shape[1]), np.uint8)
            mask = cv2.drawContours(black,[c],0,255, -1)
            return mask

        mask = get_region(th)


        # turning the region outside the green block white
        green_block = cv2.bitwise_and(img, img, mask = mask)
        green_block=(255,255,255)


        road = cv2.subtract(mask,th)
        # `road` contains some unwanted spots/contours which are removed using the function "get_region"
        only_road = get_region(road)


        road_colored = cv2.bitwise_and(img, img, mask = only_road)
        road_colored[only_road==0]=(255,255,255)
        # converting to grayscale and applying threshold
        th2 = cv2.threshold(road_colored[:,:,1],127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

        # using portion of the code from fmw42's answer, to get contours above certain area
        contours = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        result = img.copy()
        for c in contours:
            area = cv2.contourArea(c)
            if area > 1000:
                cv2.drawContours(result, [c], -1, (0,255 ,0 ), 2)
        #important###cv2.imshow("Contours", result)
        #important###cv2.imwrite("F:/final project/Desktop_app_python/contour5.jpg",result)


        # Find the longest contour (i.e., the green border)
        longest_contour = max(contours, key=cv2.contourArea)

        # Find the two farthest points on the contour
        farthest_points = cv2.approxPolyDP(longest_contour, epsilon=0.01*cv2.arcLength(longest_contour, True), closed=True)
        print(farthest_points)



        max_distance = 0
        farthest_points = None
        for i in range(len(longest_contour )):
            for j in range(i+1, len(longest_contour )):
                distance = np.linalg.norm(longest_contour [i] - longest_contour [j])
                if distance > max_distance:
                    max_distance = distance
                    farthest_points = (longest_contour [i], longest_contour [j])

        # Print the coordinates of the farthest points and the maximum distance between them
        if farthest_points is not None:
            pt1, pt2 = farthest_points
            line_img = result.copy()
            cv2.line(line_img, tuple(pt1[0]), tuple(pt2[0]), (255,0,  0), 2)
            print("The farthest points are", farthest_points[0], "and", farthest_points[1])
            print("The distance between them is",int(max_distance))
        else:
            print("Could not find farthest points on contour.")
        #cv2.imshow("Line", line_img)
        #cv2.imwrite("F:/final project/Desktop_app_python/Freezing Images/Line5.jpg", line_img)




        text = "P"

        # Define the font properties
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_color = (255, 255, 255) # white
        thickness = 2

        # Get the size of the number and text
        max_distance_size, _ = cv2.getTextSize(str(max_distance), font, font_scale, thickness)
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

        # Calculate the position of the number and text
        max_distance_x = 170
        max_distance_y = 225
        text_x = max_distance_x + max_distance_size[0]
        text_y =max_distance_y

        # Write the number and text on the image
        line_img = cv2.putText(line_img, "{:.2f}".format(max_distance)+ " " + text, (max_distance_x, max_distance_y), font, font_scale, font_color, thickness)
        #cv2.putText(line_img, text, (text_x, text_y), font, font_scale, font_color, thickness)

        #cv2.putText(line_img, "{:.2f}".format(max_distance) + " " + text, (text_x, text_y), font, font_scale, font_color, thickness)
        # Display the image
        #img = line_img.copy()

        #cv2.imshow('image', img)
        filename3 = filename2.rstrip(".jpg)")
        print(filename3)
        ext = '_result.jpg'
        filename_f = filename3+ext
        print(filename_f)

        cv2.imwrite(filename_f,line_img)
        #line_image = cv2.imread(filename2)
        line_img = ImageTk.PhotoImage(Image.open(filename_f))

        panel = Label(video_frame, image = line_img,width=500, height=300,)
        panel.place(x=70, y=400)
        #s_img = panel.cget(image)
        #cv2.imshow('m',s_img)



        #cv2.waitKey(0)



    #def Save():
    #    file = filedialog.asksaveasfilename(filetypes=[("PNG", ".png")])
    #    image = img.fromarray(rgb)
    #    image = photoImage(save)
    #    img.save(file+'.png')
    #    print(file)

    button = customtkinter.CTkButton(master=video_frame,
                                     text="Upload Image",
                                     font=('Inter', 20),
                                     text_color='#02808A',
                                     command= upload_file,
                                     width=120,
                                     height=35,
                                     border_width=1,
                                     corner_radius=5,
                                     fg_color="#FFFFFF",
                                     border_color="#02808A",
                                     hover_color="#CED2D2"

                                     )
    button.place(relx=0.59, rely=0.36, anchor=tkinter.CENTER)


    button = customtkinter.CTkButton(master=video_frame,
                                     text="Result",
                                     font=('Inter', 20),
                                     text_color='#FFFFFF',
                                     command=result,
                                     width=120,
                                     height=35,
                                     border_width=1,
                                     corner_radius=5,
                                     border_color="#02808A",
                                     hover_color="#CED2D2",
                                     fg_color="#00B2C6",


                                     )
    button.place(relx=0.59, rely=0.50, anchor=tkinter.CENTER)




    video_frame.grid(padx=0, pady=0, ipady=0, ipadx=0)


##########################################################################################################################

def all_patient_page():
    global patient_table, text, entry_name, entry_age, entry_first_data, entry_follow_up_data, entry_file_no, entry_sex, entry_refferig_doctor, entry_premedication, scr, scr2, scr3, scr4, scr5, scr6, scr7, entry_sig, entry_patient_id, pic1, pic2, pic3

    def fetc():
        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()
            cur.execute("select * from reoprt")
            rows = cur.fetchall()
            if len(rows) != 0:
                patient_table.delete(*patient_table.get_children())
                for row in rows:
                    patient_table.insert("", END, values=row)
                con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=all_patient_frame)

    def se():
        # global text

        try:
            con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
            cur = con.cursor()
            sql = "select * from reoprt where idpatient like %s"
            val = search_entry.get()
            cur.execute(sql, val)
            rows = cur.fetchall()
            if len(rows) != 0:
                patient_table.delete(*patient_table.get_children())
                for row in rows:
                    patient_table.insert("", END, values=row)
                con.commit()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=all_patient_frame)

    all_patient_frame = tk.Frame(main_frame)
    # sea=StringVar()

    search_frame = Frame(all_patient_frame, bg='#D1EAF0', )
    search_frame.grid(ipady=20, ipadx=700, padx=1)

    search = Label(search_frame, text="Search of patient report", bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 12))
    search.grid(ipadx=1, ipady=20)

    search_entry = customtkinter.CTkEntry(master=search_frame,
                                          font=('Inter', 20),

                                          text_color='#000000',
                                          width=200,
                                          height=40,
                                          placeholder_text="Search",
                                          # border_width=0,
                                          corner_radius=10,
                                          fg_color="#c7ebed",
                                          bg_color="#c7ebed",
                                          border_color="#02808A",

                                          )
    search_entry.grid(padx=10, pady=22, row=0, column=2, ipadx=25, ipady=5)
    text = search_entry.get()
    # text =search_entry.get()
    # print(text)
    search_button1 = customtkinter.CTkButton(master=search_frame,
                                             text="Search",
                                             font=('Inter', 20),
                                             text_color='#FFFFFF',
                                             command=se,
                                             width=120,
                                             height=30,
                                             # border_width=0,
                                             corner_radius=8,
                                             fg_color="#02808A",
                                             bg_color="#c7ebed",
                                             border_color="#02808A",

                                             )
    search_button1.grid(padx=20, pady=22, row=0, column=3, ipadx=10, ipady=5)

    detail_frame = Frame(all_patient_frame, bg="#F2F4F4")
    detail_frame.place(relx=0.001, rely=0.190, width=1050, height=600)

    scroll_x = Scrollbar(detail_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(detail_frame, orient=VERTICAL)
    patient_table = ttk.Treeview(detail_frame)
    patient_table.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    patient_table.configure(selectmode='extended')
    scroll_y.configure(command=patient_table.yview)
    scroll_x.configure(command=patient_table.xview)
    scroll_x.place(relx=0.0001, rely=0.910, width=1070, height=40)
    scroll_y.place(relx=0.990, rely=0.195, width=30, height=620)

    patient_table.configure(
        columns=(
        'Patient_Name', 'null', 'null', 'Age', 'FirstData', 'FollowUpData', 'FileNo', 'Sex', 'Reffering_Doctor',
        'Premedication', 'ProcedurTechnique', 'Indication', 'Esophagus', 'Stomach', 'Pyloric Ring', 'Duodenum',
        'Conclusion', 'Signature', 'Patient ID', 'img1', 'img2', 'img3', 'Id',)

    )
    fetc()
    patient_table.heading('#0', text='img1', anchor=W)
    patient_table.heading("null", text='null', anchor=W)
    patient_table.heading("null", text='null', anchor=W)
    patient_table.heading("Patient_Name", text='img1', anchor=W)
    patient_table.heading("Age", text='Reffering Doctor', anchor=W)
    patient_table.heading("FirstData", text='Premedication', anchor=W)
    patient_table.heading("FollowUpData", text='ProcedurTechnique', anchor=W)
    patient_table.heading("FileNo", text='Indication', anchor=W)
    patient_table.heading("Sex", text='Esophagus', anchor=W)
    patient_table.heading("Reffering_Doctor", text='Stomach', anchor=W)
    patient_table.heading("Premedication", text='Pyloric Ring', anchor=W)
    patient_table.heading("ProcedurTechnique", text='Duodenum', anchor=W)
    patient_table.heading("Indication", text='Conclusion', anchor=W)
    patient_table.heading("Esophagus", text='Name', anchor=W)
    patient_table.heading("Stomach", text='Age', anchor=W)
    patient_table.heading("Pyloric Ring", text='Follow Up Data', anchor=W)
    patient_table.heading("Duodenum", text='File No', anchor=W)
    patient_table.heading("Conclusion", text='Sex', anchor=W)
    patient_table.heading("Signature", text='Signature', anchor=W)
    patient_table.heading("Patient ID", text='img2', anchor=W)
    patient_table.heading("img1", text='img3', anchor=W)
    patient_table.heading("img2", text='First data', anchor=W)
    patient_table.heading("img3", text='ID report', anchor=W)
    patient_table.heading("Id", text='ID Patient', anchor=W)

    patient_table.column('#0', stretch=NO, minwidth=25, width=110)
    patient_table.column('#0', stretch=NO, minwidth=25, width=10)
    patient_table.column('#0', stretch=NO, minwidth=25, width=10)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=110)
    patient_table.column('#0', stretch=NO, minwidth=0, width=130)
    patient_table.column('#0', stretch=NO, minwidth=25, width=130)
    patient_table.column('#0', stretch=NO, minwidth=25, width=110)
    patient_table.column('#0', stretch=NO, minwidth=25, width=130)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)
    patient_table.column('#0', stretch=NO, minwidth=0, width=150)

    patient_table.place(x=0, y=1, width=1040, height=560)

    all_patient_frame.pack(expand=True, fill="both")
############################################################################################################################
cam_on = False
cap = None
out = None

#create folder
def create_folder():
    global path
    now = datetime.now()
    month = now.month
    year = now.year
    day = now.day

    path = "./" + str(year) + "_" + str(month) + "_" + str(day)

    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)


def create_patient_folder():
    global path2
    create_folder()
    now = datetime.now()
    month = now.month
    year = now.year
    day = now.day
    path2 = os.path.join("./" + str(year) + "_" + str(month) + "_" + str(day), Name_folder.get())
    print(path2)

    try:
        os.mkdir(path2)
        print("Folder %s created!" % path2)


    except FileExistsError:
        print("Folder %s already exists" % path2)



def video_record_page():
    global vid_lbl
    video_record_frame = tk.Frame(main_frame)
        # CREATE FOLDER
    path = ''
    path2 = ''

    def create_folder():
        global path
        now = datetime.now()
        month = now.month
        year = now.year
        day = now.day

        path = "./" + str(year) + "_" + str(month) + "_" + str(day)

        try:
            os.mkdir(path)
            print("Folder %s created!" % path)
        except FileExistsError:
            print("Folder %s already exists" % path)

    def create_patient_folder():
        global path2
        create_folder()
        now = datetime.now()
        month = now.month
        year = now.year
        day = now.day
        path2 = os.path.join("./" + str(year) + "_" + str(month) + "_" + str(day), Name_folder.get())
        print(path2)

        try:
            os.mkdir(path2)
            print("Folder %s created!" % path2)
            tkinter.messagebox.showinfo('Tips:', 'Folder name created successfully!')

        except FileExistsError:
            print("Folder %s already exists" % path2)
            tkinter.messagebox.showerror('Tips', 'The folder name exists, please change it')



    def on_resize(event):
        photo = Image.open('background/img.jpg')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img = tk.Label(video_record_frame)
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    def show_frame():
        global frame, out
        if cam_on:
            ret, frame = cap.read()

            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image).resize((640, 480))
                imgtk = ImageTk.PhotoImage(image=img)
                vid_lbl.imgtk = imgtk
                vid_lbl.configure(image=imgtk)

                if out is not None:
                    out.write(frame)  # Write the frame to the video file

            vid_lbl.after(10, show_frame)
    def start_vid():
        global cam_on, cap, out
        #stop_vid()
        cam_on = True

        # Open the video capture
        cap = cv2.VideoCapture(0)

        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        show_frame()

            # Start capturing and recording

    def stop_vid():
        global cam_on, cap, out
        cam_on = False

        if cap:
            cap.release()
        if out:
            out.release()
            out = None

    def save_vid():
        global out
        print("start video")
        stop_vid()

        file_types = [("MP4 Files", "*.mp4")]
        file_path = filedialog.asksaveasfile(filetypes=file_types, defaultextension=file_types,initialfile=path)

        if file_path is not None:
            # Open the saved video file and write the frames from the captured video
            saved_cap = cv2.VideoCapture('output.avi')
            out = cv2.VideoWriter(file_path.name, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (640, 480))

            while True:
                ret, frame = saved_cap.read()

                if not ret:
                    break

                out.write(frame)

            saved_cap.release()
            out.release()
            print("Video saved successfully!")

    folder_label= Label(video_record_frame,text="Enter Patient Name",bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 12))
    folder_label.place(x=120, y=70)

    Name_folder = customtkinter.CTkEntry(master=video_record_frame,font=('Inter',15),text_color='#000000',width=246,
    height=40,placeholder_text="Patient Name",corner_radius=10,fg_color="#c7ebed",bg_color="#c7ebed",border_color="#02808A",)
    Name_folder.place(x=280, y=69)

    create_patient_folder = customtkinter.CTkButton(master=video_record_frame,text="Create Patient Folder",
    font=('Inter', 17),bg_color='#D1EAF0',text_color='#FFFFFF',corner_radius=8,command=create_patient_folder,width=130,height=40,
    border_width=1,fg_color="#00B2C6",border_color="#02808A",)
    create_patient_folder.place(x=580, y=68)


    frame = Frame(video_record_frame, width=620,height=450)
    frame.place(x=70, y=150)


    vid_lbl = Label(frame, width=620,height=450)
    vid_lbl.place(x=0, y=0)

    # Buttons
    rec_icon = ImageTk.PhotoImage(Image.open("icons/img_2.png"))
    TurnCameraOn = customtkinter.CTkButton(master=video_record_frame,text="Start Video ",
    font=('Inter', 17),text_color='#FFFFFF',corner_radius=8,command=start_vid,width=130,height=40,
    border_width=1,fg_color="#00B2C6",border_color="#02808A",image=rec_icon)

    TurnCameraOn.place(x=800, y=270)

    stop_icon = ImageTk.PhotoImage(Image.open("icons/img_5.png"))
    TurnCameraOff = customtkinter.CTkButton(master=video_record_frame,text="Stop Video",
    font=('Inter', 17),text_color='#FFFFFF',corner_radius=8,command=stop_vid,width=130,height=40,
    border_width=1,fg_color="#00B2C6",border_color="#02808A",image=stop_icon)

    TurnCameraOff.place(x=800, y=350)

    SaveVideoButton = customtkinter.CTkButton(master=video_record_frame,text="Save Video",
    font=('Inter', 17),text_color='#FFFFFF',corner_radius=8,command=save_vid,width=130,height=40,
    border_width=1,fg_color="#00B2C6",border_color="#02808A",)
    #SaveVideoButton = Button(video_record_frame, text="Save Video", command=save_vid)
    SaveVideoButton.place(x=800, y=430)



    video_record_frame.pack(expand=True, fill="both")
############################################################################################################################

img_counter = 0
key = cv2.waitKey(50)

def image_capture_page():
    image_capture_page = tk.Frame(main_frame)

    def on_resize(event):
        photo = Image.open('background/img.jpg')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img = tk.Label(image_capture_page)
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    frame1 = Frame(image_capture_page, width=800, height=580)
    frame1.place(x=52, y=80)
    def upload_video():
        global cap2,frame1

        video_file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")], initialdir=path)

        # Check if the user selected a video file
        if not video_file_path:
            print("No video file selected.")
            exit()

        # Open the video file
        cap2 = cv2.VideoCapture(video_file_path)

        # Check if the video file was opened successfully
        if not cap2.isOpened():
            print("Error opening video file")
            exit()

        # Initialize the image counter
        # Get the directory of the selected video file

        show_frame()
        img_counter =0
        video_directory = "/".join(video_file_path.split("/")[:-1])

        while True:
            # Read a frame from the video
            ret, frame1 = cap2.read()

            # Check if the frame was read successfully
            if not ret:
                break

            # Display the frame
            cv2.imshow('frame', frame1)

            # Wait for the user to press a key
            key = cv2.waitKey(50)

            # Check if the user pressed the spacebar to capture an image
            if key == ord(' '):
                # Increment the image counter
                img_counter += 1

                # Generate a unique filename for the captured image in the selected video's folder
                img_name = "{}/image_{}.jpg".format(video_directory, img_counter)

                # Save the current frame as an image
                cv2.imwrite(img_name, frame1)

                # Print a message to the console
                print("Image captured:", img_name)

            # Check if the user pressed the 'q' key to quit
            if key == ord('q'):
                break

                # Release the video capture object and close all windows
        cap.release()
        cv2.destroyAllWindows()




    def show_frame():
        global cap2,frame
            #global frame
            # Read a frame from the video

        ret, frame = cap2.read()
        if ret:
                # Convert the frame from BGR to RGB and resize it
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image).resize((800, 580))
            imgtk = ImageTk.PhotoImage(image=img)

                # Update the image on the label
            vid_lbl.imgtk = imgtk
            vid_lbl.configure(image=imgtk)
        vid_lbl.after(10, show_frame)


                # Check if the frame was read successfully
       #if not ret:
       #   break
    vid_lbl = tk.Label(image_capture_page)
    vid_lbl.place(x=50, y=80)
    up_icon2 = ImageTk.PhotoImage(Image.open("icons/img_6.png"))
    upload_btn = customtkinter.CTkButton(master=image_capture_page,
                                     text="Upload Image",
                                     font=('Inter', 20),
                                     text_color='#02808A',
                                     command=upload_video,
                                     width=200,
                                     height=40,
                                     border_width=1,
                                     corner_radius=5,
                                     fg_color="#FFFFFF",
                                     border_color="#02808A",
                                     hover_color="#CED2D2",
                                     image=up_icon2,
                                     )

    upload_btn.place(x=40,y=30)

    image_capture_page.pack(expand=True, fill="both")

############################################################################################################################

def add_patient_page():
    # insert database to patient
    def save_Add_patient():
        if patient_name_entry.get() == "" or patient_id_entry.get() == "" or hospitalid_entry.get() == "" or phone_num_entry.get() == "" or age_entry.get() == "" or surgery_date_Entry.get() == "" or sex_entry.get() == "":
            messagebox.showerror("Error", "Should You Add All Fields", parent=add_patient_frame)
        elif hospitalid_entry.get() != hospitalid_entry.get():
            messagebox.showerror("Error", "Hospital_id not correct", parent=add_patient_frame)
        else:
            try:
                con = pymysql.connect(host="127.0.0.1", user="root", password="", database="battettsesophagus")
                cur = con.cursor()
                cur.execute("select * from patient where PatientName=%s", patient_name_entry.get())
                row = cur.fetchone()

                cur.execute(
                    "insert into patient(PatientName, PatientNaID,hospitalid,Patientphone,BirthDate,SurgeryDate,sex) values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        patient_name_entry.get(),
                        patient_id_entry.get(),
                        hospitalid_entry.get(),
                        phone_num_entry.get(),
                        age_entry.get(),
                        surgery_date_Entry.get(),
                        sex_entry.get(),

                    ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Add Patient Successfull", parent=add_patient_frame)
                clear()
                # switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=add_patient_frame)

    def switch():
        add_patient_frame.destroy()

        # clear data function

    def clear():
        patient_name_entry.delete(0, END)
        patient_id_entry.delete(0, END)
        hospitalid_entry.delete(0, END)
        phone_num_entry.delete(0, END)
        age_entry.delete(0, END)
        surgery_date_Entry.delete(0, END)
        # sex_entry.delete(0, END)

    add_patient_frame = tk.Frame(main_frame)

    def on_resize(event):
        # resize the background image to the size of label
        # photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
        photo = Image.open('background/img.png')  # load the background image
        image = photo.resize((event.width, event.height))
        # update the image of the label
        img.image = ImageTk.PhotoImage(image)
        img.config(image=img.image)

    img = tk.Label(add_patient_frame)
    img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
    img.bind('<Configure>', on_resize)  # on_resi

    # patient_name_label = tk.Label(add_patient_frame, text="Add Patient Data",font=('Bold',20),fg="#02808A",bg="#c7ebed")
    # patient_name_label.place(rely=.02,relx=.3)
    patient_name_entry = StringVar()
    patient_id_entry = StringVar()
    hospitalid_entry = StringVar()
    phone_num_entry = StringVar()
    age_entry = StringVar()
    surgery_date_Entry = StringVar()
    sex_entry = StringVar()

    patient_name_label = tk.Label(add_patient_frame, text="Patient Name        ", font=('Bold', 15), fg="#02808A",
                                  bg="#c7ebed")
    patient_name_label.place(rely=.05, relx=.02)
    patient_name_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                                width=610,
                                                height=50,
                                                corner_radius=8,
                                                placeholder_text="Enter Patient Name",
                                                font=('Inter', 16),
                                                fg_color="#c7ebed",
                                                bg_color="#c7ebed",
                                                border_color="#02808A", )
    # patient_name_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,border=0)
    # patient_name_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    patient_name_entry.place(rely=.05, relx=.25)
    text = patient_name_entry.get()

    patient_id_label = tk.Label(add_patient_frame, text="Patient ID              ", font=('Bold', 15), fg="#02808A",
                                bg="#c7ebed")
    patient_id_label.place(rely=.15, relx=.02)
    patient_id_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                              width=610,
                                              height=50,
                                              corner_radius=8,
                                              placeholder_text="Enter Patient ID",
                                              font=('Inter', 16),
                                              fg_color="#c7ebed",
                                              bg_color="#c7ebed",
                                              border_color="#02808A", )
    # patient_id_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    # patient_id_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    patient_id_entry.place(rely=.15, relx=.25)
    text = patient_id_entry.get()

    hospitalid_label = tk.Label(add_patient_frame, text="Hospital ID            ", font=('Bold', 15), fg="#02808A",
                                bg="#c7ebed")
    hospitalid_label.place(rely=.25, relx=.02)
    hospitalid_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                              width=610,
                                              height=50,
                                              corner_radius=8,
                                              placeholder_text="Enter Hospital ID",
                                              font=('Inter', 16),
                                              fg_color="#c7ebed",
                                              bg_color="#c7ebed",
                                              border_color="#02808A", )
    # hospital_id_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    # hospital_id_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    hospitalid_entry.place(rely=.25, relx=.25)
    text = hospitalid_entry.get()

    phone_num_label = tk.Label(add_patient_frame, text="Phone Number", font=('Bold', 15), fg="#02808A", bg="#c7ebed")
    phone_num_label.place(rely=.35, relx=.02)
    phone_num_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                             width=610,
                                             height=50,
                                             corner_radius=8,
                                             placeholder_text="Enter Phone Number",
                                             font=('Inter', 16),
                                             fg_color="#c7ebed",
                                             bg_color="#c7ebed",
                                             border_color="#02808A", )
    # phone_num_entry = tk.Entry(add_patient_frame, width=120, highlightthickness=.5,borderwidth=0)
    # phone_num_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    phone_num_entry.place(rely=.35, relx=.25)
    text = phone_num_entry.get()

    age_label = tk.Label(add_patient_frame, text="Birth Date", font=('Bold', 15), fg="#02808A", bg="#c7ebed")
    age_label.place(rely=.45, relx=.02)
    age_entry = customtkinter.CTkEntry(master=add_patient_frame,
                                       width=248,
                                       height=50,
                                       corner_radius=8,
                                       placeholder_text="Enter Birth Date",
                                       font=('Inter', 16),
                                       fg_color="#c7ebed",
                                       bg_color="#c7ebed",
                                       border_color="#02808A", )
    # age_entry = tk.Entry(add_patient_frame, show="Age", width=120, highlightthickness=.5,borderwidth=0)
    # age_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    age_entry.place(rely=0.45, relx=.25)
    text = age_entry.get()

    surgery_date_label = tk.Label(add_patient_frame, text="Surgery Date", font=('Bold', 15), fg="#02808A",
                                  bg="#c7ebed")
    surgery_date_label.place(rely=.55, relx=.02)
    surgery_date_Entry = customtkinter.CTkEntry(master=add_patient_frame,
                                                width=248,
                                                height=50,
                                                corner_radius=8,
                                                placeholder_text="Enter Surgery Date",
                                                font=('Inter', 16),
                                                fg_color="#c7ebed",
                                                bg_color="#c7ebed",
                                                border_color="#02808A", )
    # surgery_date_Spinbox = tk.Spinbox(add_patient_frame,from_='0',to='2023', width=118, highlightthickness=.5,borderwidth=0)
    # surgery_date_Spinbox.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    surgery_date_Entry.place(rely=0.55, relx=.25)
    text = surgery_date_Entry.get()

    sex_label = tk.Label(add_patient_frame, justify=LEFT, text="Sex", font=('Bold', 15),
                         fg="#02808A", bg="#c7ebed")
    sex_label.place(rely=.65, relx=.02)
    sex_entry = customtkinter.CTkComboBox(master=add_patient_frame,
                                          # text="Sex",
                                          font=('Inter', 20),
                                          text_color='#000000',
                                          values=["Male", "Female"],
                                          width=248,
                                          height=50,
                                          # border_width=0,
                                          corner_radius=8,
                                          fg_color="#c7ebed",
                                          bg_color="#c7ebed",
                                          border_color="#02808A",

                                          )

    # sex_entry = ttk.Combobox(add_patient_frame, width=50, justify=LEFT,values=["Male","Female"])
    # surgery_date_entry.config(highlightbackground = "#02808A", highlightcolor= "#02808A")
    sex_entry.place(rely=.65, relx=.25)
    text = sex_entry.get()

    add_button = customtkinter.CTkButton(master=add_patient_frame,

                                         text="Add Patient",
                                         font=('Inter', 20),
                                         text_color='#FFFFFF',
                                         command=save_Add_patient,
                                         width=149,
                                         height=42,
                                         # border_width=0,
                                         corner_radius=8,
                                         fg_color="#02808A",
                                         bg_color="#c7ebed",
                                         border_color="#02808A",
                                         # command=lambda: pages(add_patient_page()),

                                         )
    # add_button = tk.Button(add_patient_frame, text="Add Patient", width=30,font=('Bold',15),fg="#FFFFFF",bg="#02808A")
    add_button.place(rely=0.75, relx=.8)

    add_patient_frame.pack(expand=True, fill="both")


###############################################################################################################################
main_frame = tk.Frame(root)


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


def pages(page):
    delete_pages()
    page()


options_frame = tk.Frame(root, bg='#03B5C7')

icon1 = ImageTk.PhotoImage(Image.open("icons/add patient data.png"))
patient_btn = customtkinter.CTkButton(master=options_frame,
                                      text="Add patient",
                                      font=('Inter', 20, 'bold'),
                                      text_color='#02808A',
                                      command=lambda: pages(add_patient_page),
                                      width=259,
                                      height=56,
                                      image=icon1,
                                      anchor="w",
                                      # border_width=0,
                                      corner_radius=8,
                                      fg_color="#FFFFFF",
                                      bg_color="#03B5C7",
                                      border_color="#02808A",
                                      hover_color="#F5F3F3"

                                      )
# patient_btn = tk.Button(options_frame,width=25,text='Add patient\'s data',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(add_patient_page))
patient_btn.place(x=20, y=20)

icon2 = ImageTk.PhotoImage(Image.open("icons/all patient data.png"))
all_patient_btn = customtkinter.CTkButton(master=options_frame,
                                          text="All patient",
                                          font=('Inter', 20, 'bold'),
                                          text_color='#02808A',
                                          command=lambda: pages(all_patient_page),
                                          width=259,
                                          height=56,
                                          image=icon2,
                                          anchor="w",
                                          # border_width=0,
                                          corner_radius=8,
                                          fg_color="#FFFFFF",
                                          bg_color="#03B5C7",
                                          border_color="#02808A",
                                          hover_color="#F5F3F3"

                                          )
# images_btn = tk.Button(options_frame,width=25, text='All patient page',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(all_patient_page))
all_patient_btn.place(x=20, y=100)

icon3 = ImageTk.PhotoImage(Image.open("icons/img_1.png"))
video_btn = customtkinter.CTkButton(master=options_frame,
                                    text="Video Capture",
                                    font=('Inter', 20, "bold"),
                                    text_color='#02808A',
                                    command=lambda: pages(video_record_page),
                                    width=259,
                                    height=56,
                                    image=icon3,
                                    anchor="w",
                                    # border_width=0,
                                    corner_radius=8,
                                    fg_color="#FFFFFF",
                                    bg_color="#03B5C7",
                                    border_color="#02808A",
                                    hover_color="#F5F3F3"

                                    )
# video_btn = tk.Button(options_frame,width=25, text='Video',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(video_page))
video_btn.place(x=20, y=180)

icon4 = ImageTk.PhotoImage(Image.open("icons/img_3.png"))
capture_btn = customtkinter.CTkButton(master=options_frame,
                                    text="Image Capture",
                                    font=('Inter', 20, "bold"),
                                    text_color='#02808A',
                                    command=lambda: pages(image_capture_page),
                                    width=259,
                                    height=56,
                                    image=icon4,
                                    anchor="w",
                                    # border_width=0,
                                    corner_radius=8,
                                    fg_color="#FFFFFF",
                                    bg_color="#03B5C7",
                                    border_color="#02808A",
                                    hover_color="#F5F3F3"

                                    )
# video_btn = tk.Button(options_frame,width=25, text='Video',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(video_page))
capture_btn.place(x=20, y=260)

icon5 = ImageTk.PhotoImage(Image.open("icons/img_4.png"))
result_btn = customtkinter.CTkButton(master=options_frame,
                                    text="Result",
                                    font=('Inter', 20, "bold"),
                                    text_color='#02808A',
                                    command=lambda: pages(result_page),
                                    width=259,
                                    height=56,
                                    image=icon5,
                                    anchor="w",
                                    # border_width=0,
                                    corner_radius=8,
                                    fg_color="#FFFFFF",
                                    bg_color="#03B5C7",
                                    border_color="#02808A",
                                    hover_color="#F5F3F3"

                                    )
# video_btn = tk.Button(options_frame,width=25, text='Video',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(video_page))
result_btn.place(x=20, y=340)

icon6 = ImageTk.PhotoImage(Image.open("icons/report.png"))
report_btn = customtkinter.CTkButton(master=options_frame,
                                     text="Report",
                                     font=('Inter', 20, 'bold'),
                                     text_color='#02808A',
                                     command=lambda: pages(Report_page),
                                     width=259,
                                     height=56,
                                     image=icon6,
                                     anchor="w",
                                     # border_width=0,
                                     corner_radius=8,
                                     fg_color="#FFFFFF",
                                     bg_color="#03B5C7",
                                     border_color="#02808A",
                                     hover_color="#F5F3F3"

                                     )
# report_btn = tk.Button(options_frame,width=25, text='Report',font=('Bold',15),fg='#03B5C7',bd=0, command=lambda:pages(Report_page))
report_btn.place(x=20, y=420)


def close():
    # win.destroy()
    root.quit()

icon7 = ImageTk.PhotoImage(Image.open("icons/exit.png"))
Exit_btn = customtkinter.CTkButton(master=options_frame,
                                   text="Exit",
                                   font=('Inter', 20, 'bold'),
                                   text_color='#02808A',
                                   anchor="w",
                                   width=259,
                                   height=56,
                                   image=icon7,
                                   # border_width=0,
                                   corner_radius=8,
                                   fg_color="#FFFFFF",
                                   bg_color="#03B5C7",
                                   border_color="#02808A",
                                   hover_color="#F5F3F3",
                                   command=close,

                                   )
# Exit_btn = tk.Button(options_frame,width=25, text='Exit',font=('Bold',15),fg='#03B5C7',bd=0)
Exit_btn.place(x=20, y=580)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=304, height=955)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=1406, height=1024, bg="#c7ebed")


def on_resize(event):
    # resize the background image to the size of label
    # photo = ImageTk.PhotoImage(Image.open("images/bg.jpg"))
    photo = Image.open('background/background.png')  # load the background image
    image = photo.resize((event.width, event.height))
    # update the image of the label
    img.image = ImageTk.PhotoImage(image)
    img.config(image=img.image)


img = tk.Label(main_frame)
img.place(x=0, y=0, relwidth=1, relheight=1)  # make label l to fit the parent window always
img.bind('<Configure>', on_resize)  # on_resi

root.mainloop()
