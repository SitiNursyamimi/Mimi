from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition Attendance System: Attendance Data")

        self.var_attend_id=StringVar()
        self.var_attend_program=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        
        # Set the background color to black
        self.root.configure(bg="black")

        # background image
        img12 = Image.open(r"image\bg attendance.png")
        img12 = img12.resize((1280, 720), resample=Image.BILINEAR)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        bgimg12 = Label(self.root, image=self.photoimg12)
        bgimg12.place(x=0, y=0, width=1280, height=720)

        main_frame=Frame(bgimg12, bd=2)
        main_frame.place(x=20,y=70,width=1240, height=630)

        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2,relief=RIDGE, text="Student Attendance Details", font=("calibri",12,"bold"))
        Left_frame.place(x=17,y=10,width=585, height=600)

        img_left=Image.open(r"C:\Users\User\Desktop\FRASys\image\profile.png")
        img_left=img_left.resize((270,270),resample=Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0, width=270,height=270)

        # frame beside icon
        course_info=LabelFrame(Left_frame, bd=0, relief = RIDGE)
        course_info.place(x=270,y=10,width=292,height=250)
 
        # Attendance ID
        empID_label = Label(course_info, text="Attendance ID:", font=("calibri", 12, "bold"), disabledforeground="black")
        empID_label.grid(row=0,column=0, padx=10, sticky="E")
       
        empID_entry=ttk.Entry(course_info, width=19,textvariable=self.var_attend_id,font=("calibri",12))
        empID_entry.grid(row=0,column=1,padx=2,pady=5)

        # name
        name_label = Label(course_info, text="Name:", font=("calibri", 12, "bold"), disabledforeground="black")
        name_label.grid(row=1,column=0, padx=10, sticky="E")
       
        name_entry=ttk.Entry(course_info,width=19,textvariable=self.var_attend_name,font=("calibri",12))
        name_entry.grid(row=1,column=1,padx=2,pady=5)

        # date
        date_label = Label(course_info, text="Date:", font=("calibri", 12, "bold"))
        date_label.grid(row=2,column=0, padx=10, sticky="E")

        date_entry=ttk.Entry(course_info,width=19,textvariable=self.var_attend_date,font=("calibri",12))
        date_entry.grid(row=2,column=1,padx=2, pady=5)
        
        # time
        time_label = Label(course_info, text="Time:", font=("calibri", 12, "bold"))
        time_label.grid(row=3,column=0, padx=10, sticky="E")

        time_entry=ttk.Entry(course_info,width=19,textvariable=self.var_attend_time, font=("calibri",12))
        time_entry.grid(row=3,column=1,padx=2, pady=5)

        # Attendance Status
        status_label = Label(course_info, text="Status:", font=("calibri", 12, "bold"), disabledforeground="black")
        status_label.grid(row=4,column=0, padx=10, sticky="E")
       
        status_combo=ttk.Combobox(course_info,font=("calibri",12),width=17,textvariable=self.var_attend_attendance, state="readonly")
        status_combo["values"]=("Select Status","Present", "Absent")
        status_combo.current(0)
        status_combo.grid(row=4,column=1,padx=2,pady=5)

        # department
        dep_label = Label(course_info, text="Department:", font=("calibri", 12, "bold"), disabledforeground="black")
        dep_label.grid(row=5,column=0, padx=10, sticky="E")
       
        dep_combo=ttk.Combobox(course_info,font=("calibri",12),width=17,textvariable=self.var_attend_dep, state="readonly")
        dep_combo["values"]=("Select Department", "Computer Science", "Plantation and Agrotechnology")
        dep_combo.current(0)
        dep_combo.grid(row=5,column=1,padx=2,pady=5)

        # program
        prog_label = Label(course_info, text="Program:", font=("calibri", 12, "bold"), disabledforeground="black")
        prog_label.grid(row=6,column=0, padx=10, sticky="E")
       
        prog_combo=ttk.Combobox(course_info,font=("calibri",12),width=17,textvariable=self.var_attend_program,  state="readonly")
        prog_combo["values"]=("Select Programme", "AT110", "AT220", "AT222", "AT223", "AT224", "AT226", "CS110", "CS230", "CS246", "CS251", "CS253", "CS255", "CS266")
        prog_combo.current(0)
        prog_combo.grid(row=6,column=1,padx=2,pady=5)

        #----------------------------------------------------------------------#

        # buttons frame
        btn_frame=Frame(Left_frame, bd=0,relief=RIDGE)
        btn_frame.place(x=30,y=300,width=512,height=90)

        impCsv_btn=Button(btn_frame, text ="Import File",cursor="hand2",command=self.importCsv, width=11, font=("calibri",13,"bold"),bg="purple",fg="white")
        impCsv_btn.grid(row=0,column=0,padx=10,pady=10)

        exCsv_btn=Button(btn_frame, text ="Export File",cursor="hand2", command=self.exportCsv, width=11, font=("calibri",13,"bold"),bg="purple",fg="white")
        exCsv_btn.grid(row=0,column=1,padx=10,pady=10)

        reset_btn=Button(btn_frame, text ="update",cursor="hand2", width=11, font=("calibri",13,"bold"),bg="grey",fg="white")
        reset_btn.grid(row=0,column=2,padx=10,pady=10)

        delete_btn=Button(btn_frame, text ="Reset",cursor="hand2",command=self.reset_data, width=11, font=("calibri",13,"bold"),bg="grey",fg="white")
        delete_btn.grid(row=0,column=3,padx=10,pady=10)

        #----------------------------------------------------------------------#

        # right label frame
        Right_frame=LabelFrame(main_frame, bd=2,relief=RIDGE, text="Student Details", font=("calibri",12,"bold"))
        Right_frame.place(x=630,y=10,width=585, height=600)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="light blue")
        table_frame.place(x=20,y=10,width=542,height=550)

        #   scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","program","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("program",text="Programme")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("program",width=100)
        self.AttendanceReportTable.column("name",width=200)
        self.AttendanceReportTable.column("dep",width=200)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=150)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #----------------------------------------------------------------------#
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile: 
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_attend_id.set(row[0])
        self.var_attend_program.set(row[1])
        self.var_attend_name.set(row[2])
        self.var_attend_dep.set(row[3])
        self.var_attend_time.set(row[4])
        self.var_attend_date.set(row[5])
        self.var_attend_attendance.set(row[6])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_program.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop() 