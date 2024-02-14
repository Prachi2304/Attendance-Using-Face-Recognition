from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import mysql.connector
#import cv2
 

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x570+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP  DESK",font=("times new roman",17,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=800,height=28)

        img_top=Image.open(r"C:\Users\ASUS\Desktop\New folder\black-screen.jpg")
        img_top=img_top.resize((800,570),Image.BILINEAR)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=28,width=800,height=570)

        dev_label=Label(f_lbl,text="Email:sharmap4396@gmail.com",font=("times new roman",15,"bold"),bg="black",fg="blue")
        dev_label.place(x=380,y=250)

if __name__== "__main__":
    root=Tk()
    object=Help(root)
    root.mainloop()


                
