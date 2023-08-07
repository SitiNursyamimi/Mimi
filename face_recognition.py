from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition Attendance System: Face Recognition")
        
        # Set the background color to black
        self.root.configure(bg="black")

        # Initialize the video capture as an instance variable
        self.video_cap = None

        # background image
        img11 = Image.open(r"image\bg face recog.png")
        img11 = img11.resize((1280, 720), resample=Image.BILINEAR)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        bgimg11 = Label(self.root, image=self.photoimg11)
        bgimg11.place(x=0, y=0, width=1280, height=720)

        # button face recognition
        b1_1=Button(bgimg11,text="Face Recognition",cursor="hand2", font=("calibri",18, "bold"), bg="light blue",fg="black",command=self.face_recog )
        b1_1.place(x=857,y=480,width=230, height=50)

        # description face recognition
        text1_1 = Label(self.root, text="Click this", font=("calibri", 12), bg="black", fg="purple", compound="center")
        text1_1.place(x=872, y=550, width=200, height=30)


        # Bind the closing event of the root window to the custom function
        #self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    #----------------------------------------------------------------------#
    # attendance section
    def mark_attendance(self,i,p,d,n):
        with open("Attendance Data Excel.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                
            if((i not in name_list) and (p not in name_list) and (d not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {p}, {d}, {n}, {dtString}, {d1}, Present")

    #----------------------------------------------------------------------#
    # face recognition system code
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="9ef43cc3b6A6",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select studentid from student where studentid=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                my_cursor.execute("select program from student where studentid=" + str(id))
                p = my_cursor.fetchone()
                p = "+".join(p)
                
                my_cursor.execute("select dep from student where studentid=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                my_cursor.execute("select name from student where studentid=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),2)
                    cv2.putText(img, f"Program: {p}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    self.mark_attendance(i,p,d,n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 3)

                coord=[x,y,w,h]

            return coord
    
        def recognize(img,clf,faceCascade,ret):
            if ret:
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                if coord:
                    (x,y,w,h)=coord
                return img
    
        faceCascade=cv2.CascadeClassifier(r"C:\Users\User\venv\Lib\site-packages\pkg_resources\__pycache__\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        self.video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=self.video_cap.read()
            if not ret:
                break

            img=recognize(img,clf,faceCascade,ret)
            cv2.imshow("Welcome To FRASys",img)

            key = cv2.waitKey(1)

            if key==13:
                break

            if key == 27:
                break

        self.video_cap.release()
        cv2.destroyAllWindows()

    #def on_close(self):
        #if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # Release the video capture and destroy the OpenCV window
            #self.video_cap.release()
            #cv2.destroyAllWindows()
            # Close the Tkinter window
            #self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop() 