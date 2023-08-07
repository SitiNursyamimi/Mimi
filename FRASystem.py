from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login")
        self.root.geometry('1920x1080+0+0')

        #----------------------------------------------------------------------#
        # background image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\User\Desktop\FRASys\image\bg login.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"image\profile.png")
        img1=img1.resize((100,100),resample=Image.BILINEAR)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img1.place(x=727,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started!",font=("calibri",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text="Email",font=("calibri",15,"bold"),fg="light blue",bg="black")
        username.place(x=70,y=150)

        self.txtuser=ttk.Entry(frame,font=("calibri",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("calibri",15,"bold"),fg="light blue",bg="black")
        password.place(x=70,y=220)

        self.txtpwd=ttk.Entry(frame,font=("calibri",15,"bold"))
        self.txtpwd.place(x=40,y=250,width=270)

        #----------------------------------------------------------------------#
        # icon
        img2=Image.open(r"image\lock.png")
        img2=img2.resize((25,25),resample=Image.BILINEAR)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lbl_img2.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"image\key.png")
        img3=img3.resize((25,25),resample=Image.BILINEAR)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lbl_img3.place(x=650,y=395,width=25,height=25)

        # login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("calibri",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="light blue",activeforeground="purple",activebackground="light blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register button
        registerbtn = Button(frame, text="New User Register", command=self.register_window,font=("calibri",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="purple",activebackground="black")
        registerbtn.place(x=10,y=350,width=160)

        # forget password
        #forgetpwdbtn = Button(frame, text="Forget Password?", command=self.forgot_password_window, font=("calibri",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="purple",activebackground="black")
        #forgetpwdbtn.place(x=9,y=370,width=160)

        self.new_window = None
        self.forget_password_window = None

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpwd.get()=="":
            messagebox.showerror("Error !","All field are required !")
        elif self.txtuser.get()=="admin" and self.txtpwd.get()=="admin123":
            messagebox.showinfo("Succes !","Success ! Welcome to FRASys \(^-^)/ !!")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="9ef43cc3b6A6",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error!","Invalid username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.delete(0, 'end')
        self.txtpwd.delete(0,'end')

    #reset password
    def reset_pass(self):
        if self.combo_securityQ.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.forget_password_window)
        elif self.securityA_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.forget_password_window)
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.forget_password_window)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="9ef43cc3b6A6",database="mydata")
                my_cursor=conn.cursor()
                queries = ("select * from register where email=%s and securityQ=%s and securityA=%s")
                valuess=(self.txtuser.get(),self.combo_securityQ.get(),self.securityA_entry.get())
                my_cursor.execute(queries,valuess)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the correct answer",parent=self.forget_password_window)
                else:
                    query=("Update register set password=%s where email=%s")
                    value=(self.new_password_entry.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info","Your password has been reseted, please login new password",parent=self.forget_password_window)
                    
                    # Delay the destruction of the window
                    # self.forget_password_window.after(1000, self.forget_password_window.destroy)
                    self.forget_password_window.destroy()
                    # self.reset()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.forget_password_window)   
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="9ef43cc3b6A6",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter valid username")
            else:
                conn.close()
                self.forget_password_window = Toplevel()#self.root)  # Use self.forget_password_window here
                self.forget_password_window.title("Forgot Password")
                self.forget_password_window.geometry("340x450+610+170")

                l = Label(self.forget_password_window, text="Forget Password", font=("calibri", 20, "bold"), fg="purple")
                l.place(x=0, y=10, relwidth=1)

                securityQ=Label(self.forget_password_window,text="Security Question",font=("calibri",15,"bold"))
                securityQ.place(x=50,y=80)

                self.combo_securityQ=ttk.Combobox(self.forget_password_window,font=("calibri",14),state="readonly")
                self.combo_securityQ["values"]=("Select","Your birth place","Your mother's birth place","Your pet name","Your favourite color")
                self.combo_securityQ.place(x=50,y=110,width=250)
                self.combo_securityQ.current(0)

                securityA=Label(self.forget_password_window,text="Security Answer", font=("calibri",15,"bold"),fg="black")
                securityA.place(x=50,y=150)

                self.securityA_entry=ttk.Entry(self.forget_password_window,font=("calibri",14))
                self.securityA_entry.place(x=50,y=180,width=250)

                new_password=Label(self.forget_password_window,text="New Password", font=("calibri",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.new_password_entry=ttk.Entry(self.forget_password_window,font=("calibri",14))
                self.new_password_entry.place(x=50,y=250,width=250) 

                btn=Button(self.forget_password_window,text="Reset",font=("calibri",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="purple",activeforeground="light blue",activebackground="purple")   
                btn.place(x=100,y=290)
                    #minit 39.26 login and register system in python

#----------------------------------------------------------------------#

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

        loginNow=Button(frame1,text="Login Now",command=self.return_login,font=("calibri",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="light blue",activeforeground="purple",activebackground="light blue")
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

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    main()

