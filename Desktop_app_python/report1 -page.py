from tkinter import *
from tkinter import ttk
import tkinter
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

report_root = tk.Tk()
canvas = Canvas()
input_text = StringVar()
report_root.title("Barrett's Esophagus" )
report_root.geometry("1300x1500")  # set starting size of window
  # width x height
report_root.config(bg="white")  # set background color of root window

lt= Label(report_root, text="Barrett's Esophagus Report", bg="#9FBEBE", fg='#000000' )
lt.place(x=30 ,y=205)
lt.pack(pady=6  ,fill= "x")
lt.config(font=("bold", 12))

#top = Tk()
label_head_result = Label(text="   Name:  "         ,bg='white',
 fg='black', font = 'Verdana 8 bold'  )
label_head_result.place(x=15, y=40)
entry = tk.Entry(report_root,bd=3)
entry.place(x=75,y=40 ,width=160 )

age = Label(text="   Age:  "         ,bg='white',
 fg='black', font = 'Verdana 8 bold'  )
age.place(x=235, y=40)
entry = tk.Entry(report_root,bd=3)
entry.place(x=280,y=40,width=50 )

data = Label(text="First Data:  "         ,bg='white',
 fg='black', font = 'Verdana 8 bold'  )
data.place(x=350, y=40)
entry = tk.Entry(report_root,bd=3)
entry.place(x=425,y=40 )

data_up = Label(text="Follow UP Data:  "  ,bg='white',
 fg='black', font = 'Verdana 8 bold'  )
data_up.place(x=570, y=40)
entry = tk.Entry(report_root ,bd=3)
entry.place(x=677,y=40)

file = Label(text="fileNO:  "         ,bg='white',
 fg='black', font = 'Verdana 8 bold'  )
file.place(x=820, y=40)
entry = tk.Entry(report_root ,bd=3)
entry.place(x=870,y=40,width=120 )

sex = Label(text="Sex:  "   ,bg='white',
 fg='black', font = 'Verdana 8 bold'  )
sex.place(x=999, y=40)
entry = tk.Entry(report_root ,bd=3)
entry.place(x=1032,y=40,width=80 )



rd=Label(report_root,text="Reffering Doctor:  ",bg='white', fg='#02808A', font = ("Verdana 5 bold",16)  )

rd.place(x=10, y=100)
entry = tk.Entry(report_root ,bd=3)
entry.place(x=181,y=104,width=250 )

PR=Label(report_root,text="Premedication :  ",bg='white', fg='#02808A', font = ("Verdana 5 bold",16)  )

PR.place(x=455, y=100)
entry = tk.Entry(report_root ,bd=3)
entry.place(x=610,y=104,width=250 )




label1 = Label(report_root, text='Procedure Technique :',fg="#02808A" ,font=("Verdana 5 bold", 16 ),background="white")
label1.place(x=10, y=150)
scrolW=90
scrolH=3
scr=scrolledtext.ScrolledText(report_root, width=scrolW, height=scrolH, wrap=tk.WORD ,bd=3)
scr.place(x=230,y=150)

label2 = Label(report_root, text='Indication :' ,fg="#02808A",font=("Verdana 5 bold", 16 ),background="white")
label2.place(x=10, y=220)
scr2=scrolledtext.ScrolledText(report_root,bd=4, width=scrolW, height=scrolH, wrap=tk.WORD)
scr2.place(x=130,y=210)

label3 = Label(report_root,text='Esophagus:',fg="#02808A",font=("Verdana 5 bold", 16 ),background="white")
label3.place(x=10, y=290)
scr3=scrolledtext.ScrolledText(report_root, width=scrolW, height=scrolH, wrap=tk.WORD ,bd=3)
scr3.place(x=130,y=280)


label4 = Label(report_root,text='Stomach :',fg="#02808A",font=("Verdana 5 bold", 16 ),background="white")
label4.place(x=10, y=360)
scr3=scrolledtext.ScrolledText(report_root, width=scrolW, height=scrolH, wrap=tk.WORD ,bd=3)
scr3.place(x=130,y=350)


label5 = Label(report_root,text='Pyloric Ring:',fg="#02808A",font=("Verdana 5 bold", 16 ),background="white")
label5.place(x=10, y=430)
scr5=scrolledtext.ScrolledText(report_root, width=scrolW, height=scrolH, wrap=tk.WORD ,bd=3)
scr5.place(x=130,y=420)


label6 = Label(report_root,text='Duodenum :',fg="#02808A",font=("Verdana 5 bold", 16 ),background="white")
label6.place(x=10, y=500)
scr6=scrolledtext.ScrolledText(report_root, width=scrolW, height=scrolH, wrap=tk.WORD ,bd=3)
scr6.place(x=130,y=490)

label7 = Label(report_root,text='Conclusion :',fg="#02808A",font=("Verdana 5 bold", 16 ),background="white")
label7.place(x=10, y=570)
scr6=scrolledtext.ScrolledText(report_root, width=scrolW, height=scrolH, wrap=tk.WORD ,bd=3)
scr6.place(x=130,y=560)

label7 = Label(report_root,text='Signature:',fg="black",font=("Verdana 5 bold", 10 ),background="white")
label7.place(x=80, y=680)
entry1 = tk.Entry(report_root,bd=3)
entry1.place(x=143,y=682  ,width=180 ,height= 20)

label8 = Label(report_root,text='Patient ID :',fg="black" ,font=("bold", 15 ),background="white")
label8.place(x=470, y=680)
entry1 = tk.Entry(report_root ,bd=3)
entry1.place(x=575,y=682  ,width=50)





#t1=Label(root,text="Result",fg="#02808A" ,font=("Bold", 15 ),background="white")
#t1.place(x=1100 ,y=70)
fram1=ttk.Frame(width=200,height=200, relief=SUNKEN)
fram1.place(x=1000 ,y=90)

#t2=Label(root ,text= "follow", fg="#02808A" , font=('Bold',16),background="white")
#t2.place (x=1100 ,y=360)
fram2=ttk.Frame(width=200,height=200, relief=SUNKEN)
fram2.place(x=1000 ,y=290)

fram2=ttk.Frame(width=200,height=200, relief=SUNKEN)
fram2.place(x=1000 ,y=500)

#b1= button (root,text='Result',width=10 , background="white",fg="#02808A"  )
def subscribe():
    return messagebox.showinfo('','The report was successfully saved')



b1= Button(report_root, text = "Save", width = 12, height = 1, bg = "#02808A", cursor = "watch" ,fg="white",
command= subscribe)
b1.place(x=720 ,y=670)

b1= Button(report_root, text = "Print", width = 12, height = 1, bg = "white", cursor = "watch" ,fg="#0C5B61",)

b1.place(x=820 ,y=670)



report_root.mainloop()
