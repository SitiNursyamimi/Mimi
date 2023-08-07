from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition Attendance System: Student Details")

        # Set the background color to black
        self.root.configure(bg="black")

        #----------------------------------------------------------------------#
        self.var_dep=StringVar()
        self.var_program=StringVar()
        self.var_group=StringVar()
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.va_studentid=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_lectname=StringVar()
        
        img9 = Image.open(r"C:\Users\User\Desktop\FRASys\image\bg student detail.png")
        img9 = img9.resize((1280, 720), resample=Image.BILINEAR)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        bgimg9 = Label(self.root, image=self.photoimg9)
        bgimg9.place(x=0, y=0, width=1280, height=720)

        main_frame=Frame(bgimg9, bd=2)
        main_frame.place(x=20,y=70,width=1240, height=630)

        #----------------------------------------------------------------------#
  
        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2,relief=RIDGE, text="Student Details", font=("calibri",12,"bold"))
        Left_frame.place(x=17,y=10,width=585, height=600)

        img_left=Image.open(r"C:\Users\User\Desktop\FRASys\image\profile.png")
        img_left=img_left.resize((270,270),resample=Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0, width=270,height=270)
        
        # current course
        course_info=LabelFrame(Left_frame, bd=2, relief = RIDGE, text="Course Info", font=("calibri",12,"bold"))
        course_info.place(x=270,y=10,width=292,height=230)
 
        # Department
        dep_label = Label(course_info, text="Department:", font=("calibri", 12, "bold"), disabledforeground="black")
        dep_label.grid(row=0,column=0, padx=10, sticky="E")
       
        dep_combo=ttk.Combobox(course_info,textvariable=self.var_dep,font=("calibri",12),width=17, state="readonly")
        dep_combo["values"]=("Select Department", "Computer Science", "Plantation and Agrotechnology")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5)

        # programme
        prog_label = Label(course_info, text="Programme:", font=("calibri", 12, "bold"), disabledforeground="black")
        prog_label.grid(row=1,column=0, padx=10, sticky="E")
       
        prog_combo=ttk.Combobox(course_info,textvariable=self.var_program,font=("calibri",12),width=17, state="readonly")
        prog_combo["values"]=("Select Programme", "AT110", "AT220", "AT222", "AT223", "AT224", "AT226", "CS110", "CS230", "CS246", "CS251", "CS253", "CS255", "CS266")
        prog_combo.current(0)
        prog_combo.grid(row=1,column=1,padx=2,pady=5)

        # Group
        grp_label = Label(course_info, text="Group:", font=("calibri", 12, "bold"))
        grp_label.grid(row=2,column=0, padx=10, sticky="E")

        course_entry=ttk.Entry(course_info,textvariable=self.var_group,width=19,font=("calibri",12))
        course_entry.grid(row=2,column=1,padx=2, pady=5)
        
        # Course
        course_label = Label(course_info, text="Course:", font=("calibri", 12, "bold"))
        course_label.grid(row=3,column=0, padx=10, sticky="E")

        course_entry=ttk.Entry(course_info,textvariable=self.var_course,width=19,font=("calibri",12))
        course_entry.grid(row=3,column=1,padx=2, pady=5)

        # Semester
        sem_label = Label(course_info, text="Semester:", font=("calibri", 12, "bold"), disabledforeground="black")
        sem_label.grid(row=4,column=0, padx=10, sticky="E")
       
        sem_combo=ttk.Combobox(course_info,textvariable=self.var_semester,font=("calibri",12),width=17, state="readonly")
        sem_combo["values"]=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        sem_combo.current(0)
        sem_combo.grid(row=4,column=1,padx=2,pady=5)

        #----------------------------------------------------------------------#

        # student information
        std_info=LabelFrame(Left_frame, bd=2, relief = RIDGE, text="Student Info", font=("calibri",12,"bold"))
        std_info.place(x=20,y=250,width=542,height=310)  

        # student id
        stdID_label = Label(std_info, text="Student ID:", font=("calibri", 12, "bold"))
        stdID_label.grid(row=0,column=0, padx=10, sticky="E")

        stdID_entry=ttk.Entry(std_info,textvariable=self.va_studentid,width=20,font=("calibri",12))
        stdID_entry.grid(row=0,column=1,padx=10, pady=5)

        # student name
        stdName_label = Label(std_info, text="Name:", font=("calibri", 12, "bold"))
        stdName_label.grid(row=1,column=0, padx=10, sticky="E")

        stdName_entry=ttk.Entry(std_info,textvariable=self.var_name,width=20,font=("calibri",12))
        stdName_entry.grid(row=1,column=1,padx=10, pady=5)

        # Mobile Number
        mobNum_label = Label(std_info, text="Mobile Number:", font=("calibri", 12, "bold"))
        mobNum_label.grid(row=2,column=0, padx=10, sticky="E")

        mobNum_entry=ttk.Entry(std_info,textvariable=self.var_phone,width=20,font=("calibri",12))
        mobNum_entry.grid(row=2,column=1,padx=10, pady=5)

        # Gender
        gender_label = Label(std_info, text="Gender:", font=("calibri", 12, "bold"), disabledforeground="black")
        gender_label.grid(row=3,column=0, padx=10, sticky="E")
       
        gender_combo=ttk.Combobox(std_info,textvariable=self.var_gender,font=("calibri",12),width=18, state="readonly")
        gender_combo["values"]=("Select Gender","Female", "Male", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=10,pady=5)

        # Email
        email_label = Label(std_info, text="Email:", font=("calibri", 12, "bold"))
        email_label.grid(row=4,column=0, padx=10, sticky="E")

        email_entry=ttk.Entry(std_info,textvariable=self.var_email,width=20,font=("calibri",12))
        email_entry.grid(row=4,column=1,padx=10, pady=5)

        # Lecturer's Name
        lect_label = Label(std_info, text="Lecturer's Name:", font=("calibri", 12, "bold"))
        lect_label.grid(row=5,column=0, padx=10, sticky="E")

        lect_entry=ttk.Entry(std_info,textvariable=self.var_lectname,width=20,font=("calibri",12))
        lect_entry.grid(row=5,column=1,padx=10, pady=5)

        # Radio Button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(std_info,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=6, column=0)

        radiobutton2=ttk.Radiobutton(std_info,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobutton2.grid(row=6, column=1)

        # Take photo button
        take_photo_btn=Button(std_info,command=self.generate_dataset, text ="Take Photo", width=14, font=("calibri",13,"bold"),bg="white",fg="purple")
        take_photo_btn.grid(row=7,column=0,pady=2)

        # Update photo button
        update_photo_btn=Button(std_info, text ="Update Photo", width=14, font=("calibri",13,"bold"),bg="white",fg="purple")
        update_photo_btn.grid(row=7,column=1,pady=2)

        #----------------------------------------------------------------------#

        # buttons frame
        btn_frame=Frame(std_info, bd=2,relief=RIDGE)
        btn_frame.place(x=326,y=194, width=202,height=75)

        save_btn=Button(btn_frame, text ="Save",command=self.add_data, width=10, font=("calibri",13,"bold"),bg="purple",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame, text ="Update", command=self.update_data, width=10, font=("calibri",13,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame, text ="Reset",command=self.reset_data, width=10, font=("calibri",13,"bold"),bg="grey",fg="white")
        reset_btn.grid(row=1,column=0)

        delete_btn=Button(btn_frame, text ="Delete", command=self.delete_data, width=10, font=("calibri",13,"bold"),bg="grey",fg="white")
        delete_btn.grid(row=1,column=1)

        #----------------------------------------------------------------------#

        # right label frame
        Right_frame=LabelFrame(main_frame, bd=2,relief=RIDGE, text="Student Details", font=("calibri",12,"bold"))
        Right_frame.place(x=630,y=10,width=585, height=600)

        # Search system
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE, text="Search System",font=("calibri",12,"bold"))
        search_frame.place(x=20,y=10,width=542,height=105)

        search_label = Label(search_frame, text="Search By:", font=("calibri", 13, "bold"),fg="purple")
        search_label.grid(row=0,column=0, padx=10, sticky="E")

        search_combo=ttk.Combobox(search_frame,font=("calibri",12),width=17, state="readonly")
        search_combo["values"]=("Select", "Group", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5)

        search_entry=ttk.Entry(search_frame,width=20,font=("calibri",12))
        search_entry.grid(row=0,column=2,padx=10, pady=5)

        search_btn=Button(search_frame, text ="Search", width=8, font=("calibri",13,"bold"),bg="purple",fg="white")
        search_btn.grid(row=1,column=2,padx=2,sticky="E")

        showAll_btn=Button(search_frame, text ="Show All", width=8, font=("calibri",13,"bold"),bg="purple",fg="white")
        showAll_btn.grid(row=1,column=4,padx=2,sticky="E")       

        #----------------------------------------------------------------------#

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=20,y=130,width=542,height=430) 

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("studentid","program","group","course","semester","dep","name","gender","phone","email","lectname","photo"),
                                        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("studentid",text="Student ID")
        self.student_table.heading("program", text="Programme")
        self.student_table.heading("group", text="Group")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("phone",text="Mobile Number")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("lectname", text="Lecturer's Name")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        
        self.student_table.column("studentid",width=100)
        self.student_table.column("program",width=100)
        self.student_table.column("group",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("lectname",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)       
        self.fetch_data()
    #----------------------------------------------------------------------#
    # function creation

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.va_studentid.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9ef43cc3b6A6",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.va_studentid.get(),
                    self.var_program.get(),
                    self.var_group.get(),
                    self.var_course.get(),
                    self.var_semester.get(),
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_lectname.get(),
                    self.var_radio1.get(),
             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)
    
    #----------------------------------------------------------------------#
   
    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9ef43cc3b6A6",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #----------------------------------------------------------------------#
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.va_studentid.set(data[0]),
        self.var_program.set(data[1]),
        self.var_group.set(data[2]),
        self.var_course.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_dep.set(data[5]),
        self.var_name.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_email.set(data[9]),
        self.var_lectname.set(data[10]),
        self.var_radio1.set(data[11])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.va_studentid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Updates=messagebox.askyesno("Update?","Do you want to update this student details?",parent=self.root)
                if Updates:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9ef43cc3b6A6",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET program=%s, `group`=%s, course=%s, semester=%s, dep=%s, name=%s, gender=%s, phone=%s, email=%s, lectname=%s, photo=%s WHERE studentid=%s",
                                        (   self.var_program.get(),
                                            self.var_group.get(),
                                            self.var_course.get(),
                                            self.var_semester.get(),
                                            self.var_dep.get(),
                                            self.var_name.get(),
                                            self.var_gender.get(),
                                            self.var_phone.get(),
                                            self.var_email.get(),
                                            self.var_lectname.get(),
                                            self.var_radio1.get(),
                                            self.va_studentid.get(),
                                        ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details successfully updated", parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)
             
    # delete function
    def delete_data(self):
        if self.va_studentid.get()=="":
            messagebox.showerror("Error","Please insert your Student ID", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student detail?",parent=self.root)
                if delete:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9ef43cc3b6A6",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="Delete from student where studentid=%s"
                    val=(self.va_studentid.get(),)
                    my_cursor.execute(sql,val)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details successfully deleted", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

    # reset function
    def reset_data(self):
        self.va_studentid.set(""),
        self.var_program.set("Select Programme")
        self.var_group.set(""),
        self.var_course.set(""),
        self.var_semester.set("Select Semester"),
        self.var_dep.set("Select Department"),
        self.var_name.set(""),
        self.var_gender.set("Select Gender"),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_lectname.set(""),
        self.var_radio1.set("")

    #----------------------------------------------------------------------#
    # generating data set
    # generating take photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.va_studentid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9ef43cc3b6A6",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET program=%s, `group`=%s, course=%s, semester=%s, dep=%s, name=%s, gender=%s, phone=%s, email=%s, lectname=%s, photo=%s WHERE studentid=%s",
                                        (   self.var_program.get(),
                                            self.var_group.get(),
                                            self.var_course.get(),
                                            self.var_semester.get(),
                                            self.var_dep.get(),
                                            self.var_name.get(),
                                            self.var_gender.get(),
                                            self.var_phone.get(),
                                            self.var_email.get(),
                                            self.var_lectname.get(),
                                            self.var_radio1.get(),
                                            self.va_studentid.get() == id + 1
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #----------------------------------------------------------------------#
                # load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier(r"C:\Users\User\venv\Lib\site-packages\pkg_resources\__pycache__\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                        # scaling factor=1.3
                        # minimum neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y + h , x:x + w]
                        return face_cropped
                    
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret , my_frame= cap.read()
                    if ret:
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path = "C:/Users/User/Desktop/FRASys/__pycache__/data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    else:
                        messagebox.showerror("Error", "Failed to capture video from the camera", parent=self.root)
                        break    
                cap.release()
                # cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()