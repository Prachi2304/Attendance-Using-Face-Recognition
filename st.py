from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("FACE RECOGNITION SYSTEM")

        #----------variables--------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_name=StringVar()
        self.var_sem=StringVar()
        self.var_stud_id=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_sec=StringVar()
        

        #first image
        img=Image.open(r"C:\Users\ASUS\Desktop\New folder\studeennt.jpg")
        img=img.resize((500,130),Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
            
            

        

        #second image
        img1=Image.open(r"C:\Users\ASUS\Desktop\New folder\attendanceimage.jpg")
        img1=img1.resize((500,130),Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\ASUS\Desktop\New folder\studeennt.jpg")
        img2=img2.resize((550,130),Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bground image
        img3=Image.open(r"C:\Users\ASUS\Desktop\New folder\black.png")
        img3=img3.resize((1538,710),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1538,height=710)


        title_lbl=Label(bg_img,text="STUDENT  DATA",font=("algerian",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=11,y=0,width=1538,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1520,height=650)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=710,height=590)

        img_left=Image.open(r"C:\Users\ASUS\Desktop\New folder\studdentbeige.jpg")
        img_left=img_left.resize((700,130),Image.BILINEAR)
        self.photoimg_left=ImageTk.PhotoImage(img_left)


        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=700,height=130)

        
        #current course
        current_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Current Course Details",font=("times new roman",12,"bold"))
        current_frame.place(x=25,y=170,width=700,height=130)

        #department
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo['values']=("Select Department","Arts and Science","Engineering","Business","Arts and Communication","Commerce","IT","Management")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,stick=W)
        
        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo['values']=("Select Course","CSE","Civil","Mechanical","Electrical","Electronics","Biotech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo['values']=("Select year","2022-2023","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        dep_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        dep_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class Student information
        class_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Current Course Details",font=("times new roman",12,"bold"))
        class_frame.place(x=25,y=300,width=700,height=295)

        #student id
        student_label=Label(class_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        student_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_entry=ttk.Entry(class_frame,textvariable=self.var_stud_id,width=20,font=("times new roman",12,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_label=Label(class_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #section
        studentsec_label=Label(class_frame,text="Section",font=("times new roman",12,"bold"),bg="white")
        studentsec_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #studentsec_entry=ttk.Entry(class_frame,textvariable=self.var_sec,width=20,font=("times new roman",12,"bold"))
        #studentsec_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        sec_combo=ttk.Combobox(class_frame,textvariable=self.var_sec,font=("times new roman",12,"bold"),state="readonly",width=18)
        sec_combo['values']=("Select Section ","A","B","C","D","E","F","G","AI","IOT","Cyber","AI&ML","DS")
        sec_combo.current(0)
        sec_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #roll no.
        studentroll_label=Label(class_frame,text="Roll No.",font=("times new roman",12,"bold"),bg="white")
        studentroll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentroll_entry=ttk.Entry(class_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        
        #Gender
        gender_label=Label(class_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #studentroll_entry=ttk.Entry(class_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #studentroll_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo['values']=("Select Gender ","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        
        #dob
        dob_label=Label(class_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        
        #email
        mail_label=Label(class_frame,text="Email ID",font=("times new roman",12,"bold"),bg="white")
        mail_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        mail_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        
        #phone no.
        phone_label=Label(class_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        
        #address
        address_label=Label(class_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobut1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Upload photo",value="Yes")
        radiobut1.grid(row=6,column=0)

        radiobut1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Do not upload photo",value="No")
        radiobut1.grid(row=6,column=1)

        #button frame
        button2_frame=LabelFrame(class_frame,bd=2,bg="white",relief=RIDGE)
        button2_frame.place(x=5,y=215,width=680,height=28)

        take_photo_btn=Button(button2_frame,command=self.generate_dataset,text="Upload Photo",width=16,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        take_photoo_btn=Button(button2_frame,text="Delete Data",command=self.delete_data,width=16,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        take_photoo_btn.grid(row=0,column=1)

        update_btn=Button(button2_frame,text="Update",width=16,command=self.update_data,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(button2_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        
        #button frame2
        button_frame=LabelFrame(class_frame,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=5,y=246,width=680,height=30)

        save_btn=Button(button_frame,text="Save",command=self.add_data,width=70,font=("times new roman ",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=710,height=590)

        img_right=Image.open(r"C:\Users\ASUS\Desktop\New folder\studentbeige1.jpg")
        img_right=img_right.resize((700,130),Image.BILINEAR)
        self.photoimg_right=ImageTk.PhotoImage(img_right)


        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=700,height=130)



        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=4,y=150,width=700,height=410)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Name","Department","Course","Year","Sem","ID","Roll No.","DOB","Gender","Phone No.","Email","Section","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("ID",text=" ID")
        self.student_table.heading("Roll No.",text="Roll_No")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phone No.",text="Phone_No")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"
        


        self.student_table.column("Name",width=100)
        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Roll No.",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Phone No.",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #-----------function declaration--------------

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stud_id.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_dob.get()=="" or self.var_roll.get()=="" or self.var_sem.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_gender.get()=="" or self.var_sec.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                             self.var_name.get(),
                                                                                                             self.var_dep.get(),
                                                                                                             self.var_course.get(),
                                                                                                             self.var_year.get(),
                                                                                                             self.var_sem.get(),
                                                                                                             self.var_stud_id.get(),
                                                                                                             self.var_roll.get(),
                                                                                                             self.var_dob.get(),
                                                                                                             self.var_gender.get(),
                                                                                                             self.var_phone.get(),
                                                                                                             self.var_email.get(),
                                                                                                             self.var_sec.get(),
                                                                                                             self.var_address.get(),
                                                                                                             self.var_radio1.get()
                                                                                                             
                                                                                                            ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR",f"Due to:{str(es)}",parent=self.root)



         #--------------fetch data---------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #--------------get cursor-----------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_name.set(data[0]);
        self.var_dep.set(data[1]);
        self.var_course.set(data[2]);
        self.var_year.set(data[3]);
        self.var_sem.set(data[4]);
        self.var_stud_id.set(data[5]);
        self.var_roll.set(data[6]);
        self.var_dob.set(data[7]);
        self.var_gender.set(data[8]);
        self.var_phone.set(data[9]);
        self.var_email.set(data[10]);
        self.var_sec.set(data[11]);
        self.var_address.set(data[12]);
        self.var_radio1.set(data[13]);

        #delete data
    def delete_data(self):
        if self.var_stud_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_stud_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        

        


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stud_id.get()=="" or self.var_course.get()=="Select Course" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='',database='face_recognition')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Sem=%s,Roll_No=%s,DOB=%s,Gender=%s,Phone_No=%s,Email=%s,Section=%s,Address=%s,Photo=%s where ID=%s",(

                                                                                                            self.var_name.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_sem.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_sec.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_stud_id.get()
                                                                                                    ))

                         

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student detaiks successfully updated completely",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                ################reset data################
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_stud_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_sem.set("")
        self.var_dob.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_sec.set("")
        self.var_address.set("")
        self.var_radio1.set("")

                    
                        
    

#------------------------------------- take photo ---------------------------------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_stud_id.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_dob.get()=="" or self.var_roll.get()=="" or self.var_sem.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_gender.get()=="" or self.var_sec.get()=="" :
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                        id+=1
                    my_cursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Sem=%s,Roll_No=%s,DOB=%s,Gender=%s,Phone_No=%s,Email=%s,Section=%s,Address=%s,Photo=%s where ID=%s",(
                                                                                                                                                                                                                                                                                                         

                                                                                                                                                                     self.var_name.get(),
                                                                                                                                                                     self.var_dep.get(),
                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                     self.var_sem.get(),
                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                     self.var_sec.get(),
                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                     self.var_stud_id.get()==id+1

                                                                                                                                                                      ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()



                    face_class=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                    def face_cropp(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_class.detectMultiScale(gray,1.3,5)
                         #scaling factor=1.3
                         #Minimum neighbour =5

                         for(x,y,w,h) in faces:
                             face_cropp=img[y:y+h,x:x+w]
                             return face_cropp

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropp(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropp(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Croped Face",face)


                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)












                                                                                                                                                                                                















                
    
if __name__=="__main__":
    root=Tk()
    object=Student(root)
    root.mainloop()
        
