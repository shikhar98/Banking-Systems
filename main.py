from Tkinter import *
import tkMessageBox
import sqlite3
con=sqlite3.Connection('Bank')
cur=con.cursor()
def bank():
    main.destroy()
    t=0
    def new():
        new=Toplevel()
        new.configure(bg='cyan3')
        new.title("OpenAccount")
        new.geometry=("1800x600+0+0")
        def don():
            if len(z.get()) == 0:
                tkMessageBox.showerror("Error", "ACCOUNT NUMBER CANT BE EMPTY")
            elif len(x.get()) == 0:
                tkMessageBox.showerror("Error", "NAME CANT BE EMPTY")
            elif len(c.get()) == 0:
                tkMessageBox.showerror("Error", "MOBILE NUMBER CANT BE EMPTY")
            elif len(v.get()) == 0:
                tkMessageBox.showerror("Error", "ADDRESS CANT BE EMPTY")
            elif len(b.get()) == 0:
                tkMessageBox.showerror("Error", "CITY CANT BE EMPTY")
            elif len(k.get()) == 0:
                tkMessageBox.showerror("Error", "Balance CANT BE EMPTY")
            elif len(n.get()) == 0:
                tkMessageBox.showerror("Error", "STATE CANT BE EMPTY")
            elif len(a.get()) == 0:
                tkMessageBox.showerror("Error", "EMAIL CANT BE EMPTY")
            elif len(m.get()) == 0:
                tkMessageBox.showerror("Error", "PASSWORD CANT BE EMPTY")
            else:
                 done()
        def done():
            global t
            cur.execute('create table if not exists bank(acno varchar2(20) PRIMARY KEY,name varchar2(20),mobile number,address varchar2(80),city varchar2(10),state varchar2(15),gender varchar2(10),email varchar2(50),balance number,password varchar2(20))')
            cur.execute('select 1 from bank where acno=?',(z.get(),))
            cu=cur.fetchall()
            ui=0
            for row in cu:
                ui=row[0]
            if ui==0:
                if int(v1.get())==1:    
                    t='Male'
                elif int(v1.get())==2:
                    t='Female'
                cur.execute('insert into bank(acno,name,mobile,address,city,state,gender,email,balance,password) values(?,?,?,?,?,?,?,?,?,?)',(z.get(),x.get(),c.get(),v.get(),b.get(),n.get(),t,a.get(),k.get(),m.get()))
                con.commit()
                tkMessageBox.showinfo("Performed", "Your account has been created")
            elif ui==1:
                tkMessageBox.showerror("Duplicacy", "Account already exist with this acoount number")
        l2=Label(new,text="Enter your details",bg="cyan3",fg="white",font='times 50').grid(row=0,sticky=W)
        l1=Label(new,text="Choose account number for the account",bg="cyan3",fg="white",font='20').grid(row=1,column=0,sticky=W)
        z=Entry(new,font='20')
        z.grid(row=1,column=1,sticky=W)
        l3=Label(new,text="Enter your name",bg="cyan3",fg="white",font='20').grid(row=2,column=0,sticky=W)
        x=Entry(new,font='20')
        x.grid(row=2,column=1,sticky=W)
        l4=Label(new,text="Enter your mobile number",bg="cyan3",fg="white",font='20').grid(row=3,column=0,sticky=W)
        c=Entry(new,font='20')
        c.grid(row=3,column=1,sticky=W)
        l5=Label(new,text="Enter your address",bg="cyan3",fg="white",font='20').grid(row=4,column=0,sticky=W)
        v=Entry(new,font='20')
        v.grid(row=4,column=1,sticky=W)
        l6=Label(new,text="Enter your city",bg="cyan3",fg="white",font='20').grid(row=5,column=0,sticky=W)
        b=Entry(new,font='20')
        b.grid(row=5,column=1,sticky=W)
        l7=Label(new,text="Enter your state",bg="cyan3",fg="white",font='20').grid(row=6,column=0,sticky=W)
        n=Entry(new,font='20')
        n.grid(row=6,column=1,sticky=W)
        l9=Label(new,text="Enter your opening balance",bg="cyan3",fg="white",font='20').grid(row=7,column=0,sticky=W)
        k=Entry(new,font='20')
        k.grid(row=7,column=1,sticky=W)
        v1=IntVar();
        l10=Label(new,text="Choose your gender",bg="cyan3",fg="white",font='20').grid(row=8,column=0,sticky=W)
        Radiobutton(new,text='Male',variable=v1,value=1,bg='cyan3',font='20').grid(row=8,column=1,sticky=W)
        Radiobutton(new,text='Female',variable=v1,value=2,bg='cyan3',font='20').grid(row=9,column=1,sticky=W)
        l11=Label(new,text="Enter your email",bg="cyan3",fg="white",font='20').grid(row=10,column=0,sticky=W)
        a=Entry(new,font='20')
        a.grid(row=10,column=1,sticky=W)
        l8=Label(new,text="Make your password",bg="cyan3",fg="white",font='20').grid(row=15,column=0,sticky=W)
        m=Entry(new,show='*',font='20')
        m.grid(row=15,column=1,sticky=W)
        b1=Button(new,text="Proceed",command=don,font='times 20').grid(row=50,column=2,sticky=W)
        new.mainloop()
    def change():
        login=Tk()
        login.configure(bg='cyan3')
        login.title("Account")
        login.geometry=("1000x1000+2+2")
        login.minsize(1000,1000)
        Label(login,text="Welcome to netbanking",font='times 20',bg='cyan3',fg='white').grid(row=0,column=0,columnspan=5)
        cur.execute("select name from bank where acno=? and password=?",(e.get(),y.get()))
        for row in cur:
            Label(login,text=row[0],font='times 20',bg='cyan3',fg='white').grid(row=1,column=0,columnspan=5)
        def pri():
            cur.execute("select acno,name,mobile,address,city,state,email,gender from bank where acno=? and password=?",(e.get(),y.get()))
            for row in cur:
                Label(login,text=("Account number = "),bg='cyan3',fg='white',font='times 15').grid(row=20,column=0,columnspan=6,sticky=W)
                Label(login,text=(row[0]),bg='cyan3',fg='white',font='times 15').grid(row=20,column=1,columnspan=6,sticky=W)
                Label(login,text=("Name = "),bg='cyan3',fg='white',font='times 15').grid(row=21,column=0,columnspan=6,sticky=W)
                Label(login,text=(row[1]),bg='cyan3',fg='white',font='times 15').grid(row=21,column=1,columnspan=6,sticky=W)
                Label(login,text=("Phone = "),bg='cyan3',fg='white',font='times 15').grid(row=22,column=0,columnspan=6,sticky=W)
                Label(login,text=(row[2]),bg='cyan3',fg='white',font='times 15').grid(row=22,column=1,columnspan=6,sticky=W)
                Label(login,text=("Address = "),bg='cyan3',fg='white',font='times 15').grid(row=23,column=0,columnspan=6,sticky=W)
                Label(login,text=(row[3]),bg='cyan3',fg='white',font='times 15').grid(row=23,column=1,columnspan=6,sticky=W)
                Label(login,text=(row[4]),bg='cyan3',fg='white',font='times 15').grid(row=24,column=1,columnspan=6,sticky=W)
                Label(login,text=(row[5]),bg='cyan3',fg='white',font='times 15').grid(row=25,column=1,columnspan=6,sticky=W)
                Label(login,text=("Email ="),bg='cyan3',fg='white',font='times 15').grid(row=27,column=0,columnspan=6,sticky=W)
                Label(login,text=(row[6]),bg='cyan3',fg='white',font='times 15').grid(row=27,column=1,columnspan=6,sticky=W)
                Label(login,text=("Gender ="),bg='cyan3',fg='white',font='times 15').grid(row=28,column=0,columnspan=6,sticky=W)
                Label(login,text=(row[7]),bg='cyan3',fg='white',font='times 15').grid(row=28,column=1,columnspan=6,sticky=W)
        def balance():
            cur.execute("select balance from bank where acno=? and password=?",(e.get(),y.get()))
            Label(login,text="Balance = ",bg='cyan3',fg='white',font='times 15').grid(row=29,column=0,sticky=W,columnspan=6)
            Label(login,text=cur.fetchall(),bg='cyan3',fg='white',width=50,font='times 15').grid(row=29,column=1,sticky=W,columnspan=6)
        def debit():
            Label(login,text="How much money you want to Withdraw = ",bg="cyan3",fg="white",font='20').grid(row=10,column=0)
            h=Entry(login,font='20')
            h.grid(row=10,column=1)
            def deb():
                cur.execute('select balance from bank where acno=? and password=?',(e.get(),y.get()))
                for row in cur:
                    bal=row[0]
                if int(h.get())< bal:
                    cur.execute("update bank set balance=(balance-?) where acno=? and password=?",(h.get(),e.get(),y.get(),))
                    tkMessageBox.showinfo("Performed", "Your account has been debited")
                    con.commit();
                else:
                    tkMessageBox.showerror("Error", "Insufficient balance to be debited")            
            Button(login,text="Confirm",command=deb,font='times 15',bd=5).grid(row=12,column=2,sticky=W)
        def credit():
            Label(login,text="How much money you want to Deposit = ",bg="cyan3",fg="white",font='20').grid(row=13,column=0)
            h=Entry(login,font='20')
            h.grid(row=13,column=1)
            def cre():
                cur.execute("update bank set balance=(balance+?) where acno=? and password=?",(h.get(),e.get(),y.get(),))
                tkMessageBox.showinfo("Performed", "Your account has been credited")
                con.commit();
            Button(login,text="Confirm",command=cre,font='times 15',bd=5).grid(row=14,column=2,sticky=W)
        def transfer():
            Label(login,text="Account number of your beneficiary = ",bg="cyan3",fg="white",font='20').grid(row=15,column=0)
            i=Entry(login,font='20')
            i.grid(row=15,column=1)
            Label(login,text="How much money you want to transfer = ",bg="cyan3",fg="white",font='20').grid(row=16,column=0)
            j=Entry(login,font='20')
            j.grid(row=16,column=1)
            def tra():
                cur.execute('select balance from bank where acno=? and password=?',(e.get(),y.get()))
                for row in cur:
                    bal=row[0]
                if int(j.get())< bal:
                    cur.execute('select 1 from bank where acno=?',(i.get(),))
                    cu=cur.fetchall()
                    iu=0
                    for row in cu:
                        iu=row[0]
                    if iu==1:
                        cur.execute("update bank set balance=(balance+?) where acno=?",(j.get(),i.get(),))
                        cur.execute("update bank set balance=(balance-?) where acno=?",(j.get(),e.get(),))
                        con.commit()
                        tkMessageBox.showinfo("Performed", "Money has been transferred")
                    else:
                        tkMessageBox.showerror("Cancelled", "Account number of your beneficiary doesnot exist")
                else:
                    tkMessageBox.showerror("Error", "Insufficient balance to be debited")   
            Button(login,text='Confirm',command=tra,font='times 15',bd=5).grid(row=17,column=2,sticky=W)
        Button(login,text="Withdraw",command=debit,font='times 15',bd=5).grid(row=8,column=0,sticky=E,columnspan=1)
        Button(login,text="Credit",command=credit,font='times 15',bd=5).grid(row=8,column=1,sticky=E,columnspan=1)
        Button(login,text="Show Balance",command=balance,font='times 15',bd=5).grid(row=8,column=2,sticky=E,columnspan=1)
        Button(login,text="Transfer",command=transfer,font='times 15',bd=5).grid(row=8,column=3,sticky=E,columnspan=1)
        Button(login,text="Show personal details",command=pri,font='times 15',bd=5).grid(row=8,column=4,sticky=E,columnspan=1)
        Button(login,text="Log out",command=lambda:login.destroy(),font='times 15',bd=5).grid(row=50,column=4,sticky=E,columnspan=1)
        login.mainloop()
    def check():
        i=0
        cur.execute("select * from bank where acno=? and password=?",(e.get(),y.get()))
        row=cur.fetchall()
        for i in row:
            i=1
        if i==1: 
            change()
        else:
            tkMessageBox.showerror("Error","Incorrent password or Userid doesnot exist")
    def about():
        root=Tk()
        root.configure(bg='cyan3')
        root.title("About")
        Label(root,text="Hello My name is Shikhar Arora(161B212).This is my project in python and this is the netbanking system,",font='times 20',bg='cyan3',fg='white').grid(row=0,column=0)
        Label(root,text="which can credit,debit in your account and you can open new account, you can view your balance,",font='times 20',bg='cyan3',fg='white').grid(row=1,column=0)
        Label(root,text="transfer money to your beneficiary's account and also check your personal details ",font='times 20',bg='cyan3',fg='white').grid(row=2,column=0)
        Button(root,text="Close",command=lambda:root.destroy(),font='times 20',bd=5).grid(row=50,column=4,sticky=E,columnspan=1)
        root.mainloop()
    app=Tk()
    app.configure(bg='cyan3')
    app.title("Bank")
    app.minsize(1000,1000)
    app.geometry=("1000x1000+2+2")
    Label(app,text="Shikhar Bank of India",bg="blue",fg="white",font='algerian 80').grid(row=0,column=0,sticky=E,columnspan=3)
    pk=PhotoImage(file='bank.gif')
    Label(app,image=pk).grid(row=0,column=3,sticky=E)
    Label(app,text=("Welcome To NetBanking"),bg="cyan3",fg="purple",font='times 30 ').grid(row=1,column=0,columnspan=3)
    Label(app,text=("Dear Sir/Mam please Login to continue"),bg="cyan3",fg="purple",font='times 30 ').grid(row=9,column=0,columnspan=3)
    Label(app,text="Enter your details",bg="cyan3",fg="purple",font='times 30').grid(row=10,column=0,sticky=W,columnspan=3)
    Label(app,text="Enter your account number",bg="cyan3",fg="white",font ='times 15').grid(row=11,column=0,sticky=W)
    e=Entry(app,font='times 15',bd=5)
    e.grid(row=11,column=1,sticky=W)
    Label(app,text="Enter your password",bg="cyan3",fg="white",font='times 15').grid(row=12,column=0,sticky=W)
    y=Entry(app,show='*',font='times 15',bd=5)
    y.grid(row=12,column=1,sticky=W)
    Button(app,text="Log in",command=check,font='times 10',bd=5).grid(row=13,column=1,sticky=W)
    Label(app,text="Dont have an account click button create account to create one",bg="cyan3",fg="white",font='times 15').grid(row=14,column=0,sticky=W)    
    Button(app,text="Click here to open new account",command=new,font='times 10',bd=5).grid(row=14,column=1,sticky=W)
    Button(app,text="Click to close",command=lambda:app.destroy(),font='times 20',bd=5).grid(row=15,column=2,sticky=E,columnspan=1)
    Label(app,text="Username of one user of netbanking =253642    Password=python",bg='cyan3',fg='red',font='times 30').grid(row=15,column=0,columnspan=2)
    Button(app,text="About",command=about,font='times 20',bd=5).grid(row=16,column=2,sticky=E,columnspan=1)
    app.mainloop()
main=Tk()
main.minsize(1000,1000)
main.configure(bg='cyan3')
Label(main,text="Topic = NetBanking Systems",font='ravie 30',bg='dark orange',fg='white').grid(row=1,column=0,columnspan=10)
pm=PhotoImage(file='nb.gif')
Label(main,image=pm).grid(row=2,column=0,sticky=W,columnspan=3)
Label(main,text="Name = Shikhar Arora",font='ravie 15',bg='cyan3',fg='white').grid(row=4,column=0,sticky=W)
Label(main,text="Wait for 5 seconds\nMy Project will open automatically",font='ravie 15',bg='cyan3',fg='white').grid(row=4,column=1,sticky=E,rowspan=5)
Label(main,text="Enroll Number = 161B212",font='ravie 15',bg='cyan3',fg='white').grid(row=5,column=0,sticky=W)
Label(main,text="Email = shikhararora98@gmail.com",font='ravie 15',bg='cyan3',fg='white').grid(row=6,column=0,sticky=W)
Label(main,text="Branch = CSE",font='ravie 15',bg='cyan3',fg='white').grid(row=8,column=0,sticky=W)
main.after(5000,bank)
main.mainloop()
