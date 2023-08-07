from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendance System")

        # Set the background color to black
        self.root.configure(bg="black")

        # load background image
        img = Image.open(r"image\background.png")
        img = img.resize((1920, 1080), resample=Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        bgimg = Label(self.root, image=self.photoimg)
        bgimg.place(x=0, y=0, width=1920, height=1080)

        def time():
            string = strftime('%H:%H:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(bgimg,font = ('calibri',14,'bold'),background='black',foreground='light blue')
        lbl.place(x=0,y=0,width=140,height=50)
        time()

        btn_frame=Frame(bgimg, bd=2,relief=RIDGE,background='')
        btn_frame.place(x=200,y=150, width=1125,height=512)

        # 1 student details button
        img1=Image.open(r"image\student detail.png")
        img1 = img1.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1=Button(btn_frame, image=self.photoimg1,command=self.student_details, cursor="hand2")
        # b1.place(x=100,y=70,width=200, height=200)
        b1.grid(row=0, column=0,padx=0,pady=0,sticky='w')

        # 2 attendance button
        img2=Image.open(r"image\attendance.png")
        img2 = img2.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2=Button(btn_frame, image=self.photoimg2,cursor="hand2",command=self.attendance_data)
        #b2.place(x=395,y=70,width=200, height=200)
        b2.grid(row=0, column=1,padx=100,pady=0,sticky='w')

        # 3 face recognition button
        img3=Image.open(r"image\face recog.png")
        img3 = img3.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3=Button(btn_frame, image=self.photoimg3,cursor="hand2",command=self.face_data)
        #b3.place(x=690,y=70,width=200, height=200)
        b3.grid(row=0, column=2,padx=0,pady=0,sticky='w')

        # 4 help center button
        img4=Image.open(r"image\help center.png")
        img4 = img4.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4=Button(btn_frame, image=self.photoimg4,cursor="hand2",command=self.help_data)
        #b4.place(x=985,y=70,width=200, height=200)
        b4.grid(row=0, column=3,padx=100,pady=0,sticky='w')

        # 5 train data button
        img5=Image.open(r"image\train data.png")
        img5 = img5.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5=Button(btn_frame, image=self.photoimg5,cursor="hand2",command=self.train_data)
        #b5.place(x=100,y=330,width=200, height=200)
        b5.grid(row=1, column=0,padx=0,pady=100,sticky='w')

        # 6 photo button
        img6=Image.open(r"image\photo.png")
        img6 = img6.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6=Button(btn_frame, image=self.photoimg6,cursor="hand2",command=self.open_img)
        #b6.place(x=395,y=330,width=200, height=200)
        b6.grid(row=1, column=1,padx=100,pady=0,sticky='w')

        # 7 developer button
        img7=Image.open(r"image\developer.png")
        img7 = img7.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7=Button(btn_frame, image=self.photoimg7,cursor="hand2", command=self.developer_data)
        #b7.place(x=690,y=330,width=200, height=200)
        b7.grid(row=1, column=2,padx=0,pady=0,sticky='w')

        # 8 log out button
        img8=Image.open(r"image\log out.png")
        img8 = img8.resize((200, 200), resample=Image.BILINEAR)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b8=Button(btn_frame, image=self.photoimg8,cursor="hand2",command=self.iLogOut)
        # b8.place(x=985,y=330,width=200, height=200)
        b8.grid(row=1, column=3,padx=100,pady=0,sticky='w')

    def open_img(self):
        os.startfile("C:/Users/User/Desktop/FRASys/__pycache__/data")

    def iLogOut(self):
        self.iLogOut=tkinter.messagebox.askyesno("Log Out, FRASys","Are sure to log out this project?",parent=self.root)
        if self.iLogOut >0:
            self.root.destroy()
        else:
            return

        #----------------------------------------------------------------------#

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()