from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("FACE RECOGNITION SYSTEM")

        ##############variables
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image                                                                                                                    
        img=Image.open(r"C:\Users\ASUS\Desktop\New folder\attendanceimage.jpg")
        img=img.resize((800,200),Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        #second image
        img1=Image.open(r"C:\Users\ASUS\Desktop\New folder\attendanceimage.jpg")
        img1=img1.resize((800,200),Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)


        #bground image
        img3=Image.open(r"C:\Users\ASUS\Desktop\New folder\black.png")
        img3=img3.resize((1538,710),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1538,height=710)


        title_lbl=Label(bg_img,text="ATTENDANCE  RECORD",font=("algerian",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=11,y=0,width=1538,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1520,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=710,height=590)

        img_left=Image.open(r"C:\Users\ASUS\Desktop\New folder\attendanceimagee.jpg")
        img_left=img_left.resize((700,130),Image.BILINEAR)
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=700,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=135,width=702,height=400)


        #####labels and entries##############

        #attendance id
        #attendance_label=Label(left_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"),bg="white")
        #attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #attendance_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"))
        #attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=0,padx=4,pady=10)

        attendance_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        attendance_name.grid(row=0,column=1,pady=10)

        #Roll no.
        roll_label=Label(left_inside_frame,text="Roll NO",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2)

        attendance_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        attendance_roll.grid(row=0,column=3,pady=8)

        #Department
        dep_label=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0)

        attendance_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        attendance_dep.grid(row=1,column=1,pady=8)

        #time
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=1,column=2)

        attendance_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        attendance_time.grid(row=1,column=3,pady=8)

        #Date
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=0)

        attendance_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        attendance_date.grid(row=2,column=1,pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        attendanceLabel.grid(row=2,column=2,pady=8)
        
        self.attern_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.attern_status['values']=("Status","Present","Absent")
        self.attern_status.current(0)
        self.attern_status.grid(row=2,column=3,pady=8)
        #####button frame

        button_frame=LabelFrame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=4,y=350,width=682,height=35)

        save_btn=Button(button_frame,text="Import CSV",command=self.importCsv,width=22,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        updatee_btn=Button(button_frame,text="Export CSV",command=self.exportCsv,width=22,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        updatee_btn.grid(row=0,column=1)

        #updatea_btn=Button(button_frame,text="Update",width=16,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        #updatea_btn.grid(row=0,column=2)

        updateb_btn=Button(button_frame,text="Reset",command=self.reset_data,width=22,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        updateb_btn.grid(row=0,column=2)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=710,height=590)

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=5,width=700,height=455)

        ############scroll bar###########
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("roll",text="Roll NO.")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        ######################fetch data##########################
        
               

    
    def fetchData(self,rows):
        global mydata
        mydata=rows
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported"+os.path.basename(fln)+"Successfully")
        except Exception as es:
                messagebox.showerror("ERROR",f"Due to:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    def reset_data(self):
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        

    

    
        




if __name__=="__main__":
    root=Tk()
    object=Attendance(root)
    root.mainloop()























        
