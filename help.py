from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition Attendance System: Help Center")

        # Set the background color to black
        self.root.configure(bg="black")

        # background image
        img11 = Image.open(r"image\help dev bg.png")
        img11 = img11.resize((1280, 720), resample=Image.BILINEAR)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        bgimg11 = Label(self.root, image=self.photoimg11)
        bgimg11.place(x=0, y=0, width=1280, height=720)

        text1_1 = Label(self.root, text="Any inquiries, please contact via email\nsyamimiazha2@gmail,com", font=("calibri", 12), bg="purple", fg="white", compound="center")
        text1_1.place(x=415, y=495, width=450, height=75)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop() 