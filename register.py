from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root 
        self.root.title("Register")
        self.root.geometry('1920x1080+0+0')

        #----------------------------------------------------------------------#
        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()  
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pwd=StringVar()
        self.var_conpwd=StringVar()

        # background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\FRASys\image\bg login.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=100,y=100,width=510,height=590)
        
        # left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\FRASys\image\register.png")
        lbl_bg1=Label(self.root,image=self.bg1)
        lbl_bg1.place(x=120,y=120,width=470,height=550)

        # main frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=610,y=100,width=800,height=590)

        register_lbl=Label(frame1,text="REGISTER HERE", font=("calibri",20,"bold"), fg="purple", bg="white")
        register_lbl.place(x=20,y=20)
        
        # Row 1 label entry
        fname=Label(frame1,text="First Name",font=("calibri",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame1,textvariable=self.var_fname,font=("calibri",14))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame1,text="Last Name", font=("calibri",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)

        self.lname_entry=ttk.Entry(frame1,textvariable=self.var_lname,font=("calibri",14))
        self.lname_entry.place(x=370,y=130,width=250)

        # Row 2 label entry
        contact=Label(frame1,text="Mobile Number",font=("calibri",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame1,textvariable=self.var_contact,font=("calibri",14))
        self.contact_entry.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email", font=("calibri",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.email_entry=ttk.Entry(frame1,textvariable=self.var_email,font=("calibri",14))
        self.email_entry.place(x=370,y=200,width=250)

        # Row 3 label entry
        pwd=Label(frame1,text="Password",font=("calibri",15,"bold"),bg="white")
        pwd.place(x=50,y=240)

        self.pwd_entry=ttk.Entry(frame1,textvariable=self.var_pwd, font=("calibri",14))
        self.pwd_entry.place(x=50,y=270,width=250)

        conpwd=Label(frame1,text="Confirm Your Password", font=("calibri",15,"bold"),bg="white",fg="black")
        conpwd.place(x=370,y=240)

        self.conpwd_entry=ttk.Entry(frame1,textvariable=self.var_conpwd, font=("calibri",14))
        self.conpwd_entry.place(x=370,y=270,width=250)
        
        # Row 4 label entry
        securityQ=Label(frame1,text="Security Question",font=("calibri",15,"bold"),bg="white")
        securityQ.place(x=50,y=310)

        self.combo_securityQ=ttk.Combobox(frame1,textvariable=self.var_securityQ,font=("calibri",14),state="readonly")
        self.combo_securityQ["values"]=("Select","Your birth place","Your mother's birth place","Your pet name","Your favourite color")
        self.combo_securityQ.place(x=50,y=340,width=250)
        self.combo_securityQ.current(0)

        securityA=Label(frame1,text="Security Answer", font=("calibri",15,"bold"),bg="white",fg="black")
        securityA.place(x=370,y=310)

        self.securityA_entry=ttk.Entry(frame1,textvariable=self.var_securityA,font=("calibri",14))
        self.securityA_entry.place(x=370,y=340,width=250)

        # check button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame1,variable=self.var_check,text="I Agree the Terms & Condition",font=("calibri",12,"bold"),bg="white",fg="black",activeforeground="black",activebackground="white")
        self.checkbtn.place(x=50,y=380)

        # button

        self.registerNow=Button(frame1,command=self.register_data,text="Register",font=("calibri",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="purple",activeforeground="light blue",activebackground="purple")
        self.registerNow.place(x=344,y=530,width=200,height=35)

        loginNow=Button(frame1,text="Login Now",font=("calibri",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="light blue",activeforeground="purple",activebackground="light blue")
        loginNow.place(x=572,y=530,width=200,height=35)

    #----------------------------------------------------------------------#
    # function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error!","All field are required !")
        elif self.var_pwd.get()!=self.var_conpwd.get():
            messagebox.showerror("Error!","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="9ef43cc3b6A6",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error!","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pwd.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo ("Succes","Registered Successfully")

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()