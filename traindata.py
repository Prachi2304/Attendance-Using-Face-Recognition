from tkinter import*
from tkinter import ttk
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk 
import tkinter
import mysql.connector
import os
import cv2
import numpy as np

class Train_Data:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x570+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        title_lbl=Label(self.root,text="TRAIN DATA ",font=("algerian",17,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=800,height=28)

        imgtop=Image.open(r"C:\Users\ASUS\Desktop\New folder\scan6.jpg")
        imgtop=imgtop.resize((800,273),Image.BILINEAR)
        self.photoimgtop=ImageTk.PhotoImage(imgtop)


        f_lbl=Label(self.root,image=self.photoimgtop)
        f_lbl.place(x=0,y=28,width=800,height=273)


        #--------------button----------------
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_class,cursor="circle",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=0,y=301,width=800,height=24)


        imgb=Image.open(r"C:\Users\ASUS\Desktop\New folder\scan6.jpg")
        imgb=imgb.resize((800,273),Image.BILINEAR)
        self.photoimgb=ImageTk.PhotoImage(imgb)


        f_lbl=Label(self.root,image=self.photoimgb)
        f_lbl.place(x=0,y=325,width=800,height=273)

    def train_class(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #----------------train the classifier------------------

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")

        
        

        
        

if __name__=="__main__":
    root=Tk()
    object=Train_Data(root)
    root.mainloop()
            
