import sqlite3
from tkinter import messagebox
from tkinter import *

def createconnection():
    global conn,cursor
    conn = sqlite3.connect('Lab/week10_1660700384.db')
    cursor = conn.cursor()
def mainwindow() :
    root = Tk()
    #กำหนดขนาดหน้าจอ
    w = 1000
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#FCBEEC')
    root.title("Login Application: ")
    root.option_add('*font',"Garamond 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)#คิอการตีคารางเป็น16ช่อง
    root.columnconfigure((0,1,2,3),weight=1)
    return root

def loginlayout(root) :
    global userentry
    global pwdentry
    global loginframe
    
    loginframe = Frame(root,bg='#FCBEEC')
    loginframe.grid(row=1,column=1,columnspan=3,rowspan=3,sticky='news')

    picLB = Label(loginframe,image=pic,bg='#FCBEEC').grid(rowspan=4,column=0,sticky='w',padx=40)

    usernameLB = Label(loginframe,text='Username',bg='#FCBEEC',font='Arial 25').grid(
        row= 0,column=1,sticky='w')
    userentry = Entry(loginframe,bg='#FFFFFF',fg='#4a3933',width=25,textvariable=userinfo)
    userentry.grid(row=1,column=1,sticky='w',pady=10)

    passLB = Label(loginframe,text='Password',bg='#FCBEEC',font='Arial 25').grid(
        row= 2,column=1,sticky='w')
    pwdentry = Entry(loginframe,bg='#FFFFFF',fg='#4a3933',width=25,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=3,column=1,sticky='w',pady=5)

    Button(loginframe,text='Login',bg='#FCBEEC',command=loginclick).grid(row=4,column=1,pady=30)
#ระบบlogin
def loginclick() :
    global result
    global grade
    # เช็คว่ากรอกข้อมูลหรือยัง
    if userentry.get() == '' or pwdentry.get() == '' :
        messagebox.showwarning('Admin','Enter user or password first')
        userentry.focus_force()
    else:
    # ถ้ากรอกแล้ว มีข้อมูลใน DB ไหม
        sql = 'SELECT * FROM Students WHERE username=?'
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        print(result)
        sql = 'SELECT * FROM Students WHERE username=? AND password=?'
        cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
        result = cursor.fetchone()
        if result:
            print(result[0],result[1],result[2])
            messagebox.showinfo('Admin','Login Successful.')
            welcomepage()
        else:
            messagebox.showwarning('Admin','Username or Password is invalid.')
            userentry.focus_force()
            
def welcomepage() :
    score = result[3]

    if score > 49 :
        if score >= 80:
            grade = 'A'
        elif score >= 70:
            grade = 'B'
        elif score >= 60:
            grade = 'C'
        elif score >= 50:
            grade = 'D'
    else:
        grade = 'F'

    welcomeframe = Frame(root,bg='#B8E2F0')
    welcomeframe.rowconfigure((0,1,2,3,4,5),weight=1)
    welcomeframe.columnconfigure((0,1,2),weight=1)
    welcomeframe.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='news')

    Label(welcomeframe,image=pic,bg='#B8E2F0').grid(row=0,columnspan=4)
    
    Label(welcomeframe,text='Students ID',font=('Arial',30),bg='#B8E2F0').grid(row=1,column= 0,sticky='w',padx=90)
    Label(welcomeframe,text='' + str(result[0]),font=('Arial',30),bg='#B8E2F0').grid(row=1,column= 1,sticky='w')

    Label(welcomeframe,text='Name',font=('Arial',30),bg='#B8E2F0').grid(row=2,column= 0,sticky='w',padx=90)
    Label(welcomeframe,text='' + str(result[1]+' '+result[2]),font=('Arial',30),bg='#B8E2F0').grid(row=2,column= 1,sticky='w')

    Label(welcomeframe,text='Score',font=('Arial',30),bg='#B8E2F0').grid(row=3,column= 0,sticky='w',padx=90)
    Label(welcomeframe,text='' + str(result[3]),font=('Arial',30),bg='#B8E2F0').grid(row=3,column= 1,sticky='w')

    Label(welcomeframe,text='Grade',font=('Arial',30),bg='#B8E2F0').grid(row=4,column= 0,sticky='w',padx=90)
    Label(welcomeframe,text=grade,font=('Arial',30),bg='#B8E2F0').grid(row=4,column= 1,sticky='w')
    
    Button(welcomeframe,text='Log Out',bg='#FCBEEC',command=welcomeframe.destroy).grid(row=5,column=1,pady=30 ,sticky='w')
createconnection()
root = mainwindow()
pic = PhotoImage(file='Lab/images/profile.png')
userinfo = StringVar() #spy for getting user data
pwdinfo = StringVar()  #spy for getting password data
loginlayout(root)
root.mainloop()