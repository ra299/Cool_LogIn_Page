from tkinter import*
from tkinter import messagebox
from PIL import ImageTk


class Login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+0")
        #=== all Image======
        self.bg_icon=ImageTk.PhotoImage(file="images/bck.jpg")
        self.user_icon=PhotoImage(file="images/lock.png")
        self.pass_icon=PhotoImage(file="images/male.png")
        self.logo_icon=PhotoImage(file="images/touch.png")

        #========variables============

        self.uname = StringVar()
        self.pass_ = StringVar()



        bg_lbl = Label(self.root, image = self.bg_icon)
        bg_lbl.pack()

        title = Label(self.root,text="Login System",font=("time new roman",40,"bold"), bg = "green",fg="white",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="light blue")
        Login_Frame.place(x=400,y=150)

        logolbl=Label(Login_Frame, image = self.logo_icon,bg="light blue",bd=0)
        logolbl.grid(row=0,columnspan=2,pady=20)
    
        lbluser = Label(Login_Frame,text ="Username",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="light blue")
        labuser.grid(row=1,column=0,padx=20,pady=10)
        textuser = Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15))
        textuser.grid(row=1,column=1,padx=20)

        lblpass = Label(Login_Frame,text ="Password",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="light blue").grid(row=2,column=0,padx=20,pady=10)
        textpass = Entry(Login_Frame,bd=5, relief=GROOVE,textvariable=self.pass_, font=("",15)).grid(row=2,column=1,padx=20)

        btn_log = Button(Login_Frame, text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,pady=10)

    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All fields are requerds!!")

        elif self.uname.get()=="Rahul" and self.pass_.get()=="rahul":
            messagebox.showerror("successfull",f"welcome{self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid username or password")

        

root = Tk()
obj=Login_system(root)
root.mainloop()