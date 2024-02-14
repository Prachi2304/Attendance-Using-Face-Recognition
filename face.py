from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from st import Student
from helpp import Help
from traindata import Train_Data
import os
from face_recognition import Face_Recognition
from attendancee import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title("FACE RECOGNITION SYSTEM")
        #first image                                                                                                                    
        img=Image.open(r"C:\Users\ASUS\Desktop\New folder\darkbeige.jpg")
        img=img.resize((500,130),Image.BILINEAR)
        self.photoimg=ImageTk.PhotoImage(img)


        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\ASUS\Desktop\New folder\darkbeige.jpg")
        img1=img1.resize((500,130),Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)


        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\ASUS\Desktop\New folder\darkbeige.jpg")
        img2=img2.resize((550,130),Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)


        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        #bground image
        img3=Image.open(r"C:\Users\ASUS\Desktop\New folder\bg1.jpg")
        img3=img3.resize((1530,710),Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)


        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="ATTENDANCE  USING  FACE  RECOGNITION  SYSTEM",font=("algerian",35,"bold"),bg="beige",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        

        #first option
        img4=Image.open(r"C:\Users\ASUS\Desktop\New folder\studdennttbeige2.jpeg")
        img4=img4.resize((220,220),Image.BILINEAR)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="circle")
        b1.place(x=200,y=100,width=220,height=200)



        b1_1=Button(bg_img,text="STUDENT DATA",command=self.student_details,cursor="circle",font=("algerian",15,"bold"),bg="beige",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)


        #second option
        img5=Image.open(r"C:\Users\ASUS\Desktop\New folder\Screenshot (27).png")
        img5=img5.resize((220,220),Image.BILINEAR)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="circle")
        b2.place(x=600,y=100,width=220,height=200)



        b2_2=Button(bg_img,text="FACE Recognition",command=self.Face_recognition,cursor="circle",font=("algerian",15,"bold"),bg="beige",fg="black")
        b2_2.place(x=600,y=300,width=220,height=40)


        
        #third option
        imge6=Image.open(r"C:\Users\ASUS\Desktop\New folder\attennn.jpg")
        imge6=imge6.resize((250,220),Image.BILINEAR)
        self.photoimge6=ImageTk.PhotoImage(imge6)

        b3=Button(bg_img,image=self.photoimge6,cursor="circle")
        b3.place(x=1000,y=100,width=220,height=200)



        b3_3=Button(bg_img,text="ATTENDANCE",cursor="circle",command=self.attendance_data,font=("algerian",15,"bold"),bg="beige",fg="black")
        b3_3.place(x=1000,y=300,width=220,height=40)

        #fourth option
        img6=Image.open(r"C:\Users\ASUS\Desktop\New folder\facescanbeige.jpg")
        img6=img6.resize((250,220),Image.BILINEAR)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="circle")
        b3.place(x=200,y=380,width=220,height=200)



        b3_3=Button(bg_img,text="TRAIN DATA",cursor="circle",command=self.Train_data,font=("algerian",15,"bold"),bg="beige",fg="black")
        b3_3.place(x=200,y=580,width=220,height=40)



        #fifth option
        img7=Image.open(r"C:\Users\ASUS\Desktop\New folder\ooo.jpg")
        img7=img7.resize((220,220),Image.BILINEAR)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="circle",command=self.help_data)
        b4.place(x=600,y=380,width=220,height=200)



        b4_4=Button(bg_img,text="HELP",cursor="circle",command=self.help_data,font=("algerian",15,"bold"),bg="beige",fg="black")
        b4_4.place(x=600,y=580,width=220,height=40)
        


         #sixth option
        img8=Image.open(r"C:\Users\ASUS\Desktop\New folder\beigeexit.jpg")
        img8=img8.resize((220,220),Image.BILINEAR)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="circle",command=self.exit)
        b5.place(x=1000,y=380,width=220,height=200)



        b5_5=Button(bg_img,text="EXIT",cursor="circle",command=self.exit,font=("algerian",15,"bold"),bg="beige",fg="black")
        b5_5.place(x=1000,y=580,width=220,height=40)


    def exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this page",parent=self.root)
        if self.Exit>0:
            self.root.destroy()
        else:
            return


        #function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)    
    def Face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)




if __name__=="__main__":
    root=Tk()
    object=Face_Recognition_System(root)
    root.mainloop()
        
