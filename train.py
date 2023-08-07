from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition Attendance System: Train Data")

        # Set the background color to black
        self.root.configure(bg="black")

        # background image
        img10 = Image.open(r"image\bg train.png")
        img10 = img10.resize((1280, 720), resample=Image.BILINEAR)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        bgimg10 = Label(self.root, image=self.photoimg10)
        bgimg10.place(x=0, y=0, width=1280, height=720)

        # button
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier, cursor="hand2",font=("calibri",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=400,y=200, width=200, height=60)

    def train_classifier(self):
        data_dir=("C:/Users/User/Desktop/FRASys/__pycache__/data")
        path=[os.path.join (data_dir,file) for file in os.listdir("C:/Users/User/Desktop/FRASys/__pycache__/data")]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') # gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #----------------------------------------------------------------------#
        # train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results","Training datasets completed!!")
    
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 