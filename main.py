from  tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import datetime
from AddBooks import *
from DeleteBook import *
from ViewBooks import *
from SearchBook import *
from IssueBook import *
from SearchBook import searchBook

root = Tk()
root.title('JSPM Library')
root.iconbitmap('F:/Project/Icon.ico')
root.geometry("1360x768+0+0")
root.config(bg="#486A90")
mypass = "root"
mydatabase="lib_db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

def AdminLogin():
    global EMPID
    def blank():
        ID_login = Entry(login_frame, width=25)
        ID_login.grid(row=0, column=1, padx=10)
        ID_login.insert(END,"")

        password_login = Entry(login_frame, width=25)
        password_login.grid(row=1, column=1, pady=10, padx=10)
        password_login.insert(END,"")
    EMPID=ID_login.get()
    emp_exist = []
    cur.execute("select empid from emp")
    con.commit()
    for i in cur:
        emp_exist.append(i[0])
    print(*emp_exist)
    print(ID_login.get())

    if ID_login.get() in emp_exist:
        try:
            passkey = ""
            cur.execute("select password from emp where empid='" + ID_login.get() + "'")
            con.commit()
            for i in cur:
                passkey = i[0]
            if passkey == password_login.get():
                blank()
                empMenu()
            else:
                response = messagebox.showinfo("INVALID", "Wrong Password!")

        except:
            response = messagebox.showerror("INVALID", "Something Went Wrong!")

    else:
        response = messagebox.showerror("User Doesn't Exist", "Check your EmpID")

def Login():
    def blank():
        ID_login = Entry(login_frame, width=25)
        ID_login.grid(row=0, column=1, padx=10)
        ID_login.insert(END,"")

        password_login = Entry(login_frame, width=25)
        password_login.grid(row=1, column=1, pady=10, padx=10)
        password_login.insert(END,"")
    roll_exist=[];email_exist=[]
    cur.execute("select rollno from studetail")
    con.commit()
    for i in cur:
        roll_exist.append(i[0])
    print(*roll_exist)

    if ID_login.get() in roll_exist:
        try:
            passkey=""
            cur.execute("select password from studetail where rollno='"+ID_login.get()+"'")
            con.commit()
            for i in cur:
                passkey=i[0]
            if passkey==password_login.get():
                blank()
                stuMenu()
            else:
                response = messagebox.showerror("INVALID", "Wrong Password!")

        except:
            response = messagebox.showerror("INVALID", "Something Went Wrong!")

    else:
        response = messagebox.showerror("User Doesn't Exist", "Check your ROLLNO")


def SaveStudent():
    # DATA validation is done here first like,all fields are filled,password check,unique roll no

    flag = 0
    roll_call_list = []
    cur.execute("select rollno from studetail")
    con.commit()
    for i in cur:
        roll_call_list.append(i[0])

    if len(fname.get()) == 0 or len(lname.get()) == 0 or len(email.get()) == 0 or len(rollno.get()) == 0 or len(
            dob.get()) == 0 or len(phone.get()) == 0 or len(password.get()) == 0:
        response = messagebox.showerror("Error", "Please Fill all fields")

        flag = 1
    else:
        if not (phone.get()).isnumeric() or len(phone.get()) != 10:
            response = messagebox.showerror("Phone no", "Phone no must be of 10 digits and numeric")

            flag = 1
        if not (fname.get()).isalpha() or not (lname.get()).isalpha():
            response = messagebox.showerror("Invalid Entry", "Firstname ,Lastname must contain characters only")

            flag = 1
        if password.get() != repassword.get():
            response = messagebox.showerror("Error", "Password Does not matched")

            flag = 1
        if not (rollno.get()).isnumeric():
            response = messagebox.showerror("Roll no", "Roll number must be Number")

            flag = 1
        year,month,day=(dob.get()).split("/")
        try:
            datetime.datetime(int(year),int(month),int(day))
        except:
            flag=1
            response = messagebox.showerror("Date", "Please Enter valid date in format YYYY/MM/DD")
        if rollno.get() in roll_call_list:
            response = messagebox.showerror("Roll no", "Roll no is already used")

            flag=1
        if flag == 0:
            try:
                savestudentdetail="insert into studetail values ('"+rollno.get()+"','"+password.get()+"','"+depclicked.get()+"','"+semclicked.get()+"','"+fname.get()+"','"+lname.get()+"','"+phone.get()+"','"+email.get()+"','"+dob.get()+"')"
                cur.execute("insert into studetail values ('"+rollno.get()+"','"+password.get()+"','"+depclicked.get()+"','"+semclicked.get()+"','"+fname.get()+"','"+lname.get()+"','"+phone.get()+"','"+email.get()+"','"+dob.get()+"')")
                print(savestudentdetail)
                con.commit()
                response = messagebox.showinfo("Success", "Registration Successful")

                signup_window.destroy()
            except:
                response = messagebox.showerror("INVALID", "Check your Input",parent=signup_window)


def stuMenu():
    global headingFrame1, headingFrame2, headingLabel, SubmitBtn, Canvas1, btn1, btn2, btn3, btn4, btn5, backBtn
    #headingFrame1.destroy()
    #headingFrame2.destroy()
    #headingLabel.destroy()

    root = Tk()
    root.title('JSPM Library')
    root.iconbitmap('F:/Project/Icon.ico')
    root.geometry("1360x768+0+0")
    root.config(bg="#486A90")
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#dff9fb")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#333945", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Student MENU", fg='black')
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    btn1 = Button(root, text="View Book List", bg='black', fg='white', command=View)
    btn1.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Search Book", bg='black', fg='white', command=searchBook)
    btn2.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)

def StudentRegistration():

        global fname ,lname,email,phone,dob,rollno,password,repassword,signup_window,depclicked,semclicked
        signup_window=Toplevel()
        signup_window.title("Signup")
        signup_window.iconbitmap('F:/Project/Icon.ico')
        signup_window.geometry("1366x768+0+0")
        signup_window.config(bg="#486A90")
        semoptions=["I","II","III","IV","V","VI","VII","VIII"]
        depoptions=["IT","COMP","CIVIL","ELECTRONICS","ENTC","ELECTRICAL","MECHANICAL"]
        depclicked=StringVar()
        depclicked.set(depoptions[0])
        semclicked=StringVar()
        semclicked.set(semoptions[0])

        signup_frame = LabelFrame(signup_window, padx=60 ,pady=40, bd=4, width='300')
        signup_frame.grid(row=1,pady=180,padx=480)

        headingFrame1 = Frame(signup_window, bg="#333945", bd=5)
        headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

        headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
        headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

        headingLabel = Label(headingFrame2, text="Welcome to JSPM Library", fg='black', font=("brush script mt", 30))
        headingLabel.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)

        fname_label = Label(signup_frame, text="Firstname", font=("", 10), pady=5)
        fname_label.grid(row=0, column=0, sticky='w')

        lname_label = Label(signup_frame, text="Lastname", font=("", 10), pady=5)
        lname_label.grid(row=1, column=0, sticky='w')

        phone_label = Label(signup_frame, text="Phone no", font=("", 10), pady=5)
        phone_label.grid(row=2, column=0, sticky='w')

        Email_label = Label(signup_frame, text="Email", font=("", 10), pady=5)
        Email_label.grid(row=3, column=0, sticky='w')

        dob_label = Label(signup_frame, text="DOB", font=("", 10), pady=5)
        dob_label.grid(row=4, column=0, sticky='w')

        department_label = Label(signup_frame, text="Department", font=("", 10), pady=5)
        department_label.grid(row=5, column=0, sticky='w')

        Roll_label = Label(signup_frame, text="Roll No", font=("", 10), pady=5)
        Roll_label.grid(row=6, column=0, sticky='w')

        semester_label = Label(signup_frame, text="Semester", font=("", 10), pady=5)
        semester_label.grid(row=7, column=0, sticky='w')

        password_label = Label(signup_frame, text="Password", font=("", 10), pady=5)
        password_label.grid(row=8, column=0, sticky='w')

        repassword_label = Label(signup_frame, text="Confirm Password", font=("", 10), pady=5)
        repassword_label.grid(row=9, column=0, sticky='w')

        fname = Entry(signup_frame, width=25)
        fname.grid(row=0, column=1, padx=10)

        lname = Entry(signup_frame, width=25)
        lname.grid(row=1, column=1, padx=10)

        phone = Entry(signup_frame, width=25)
        phone.grid(row=2, column=1, padx=10)

        email = Entry(signup_frame, width=25)
        email.grid(row=3, column=1, padx=10)

        dob = Entry(signup_frame, width=25)
        dob.grid(row=4, column=1, padx=10)

        depdrop = OptionMenu(signup_frame, depclicked, *depoptions)
        depdrop.grid(row=5, column=1)

        rollno = Entry(signup_frame, width=25)
        rollno.grid(row=6, column=1, padx=10)

        semdrop = OptionMenu(signup_frame, semclicked, *semoptions)
        semdrop.grid(row=7,column=1)

        password = Entry(signup_frame, width=25)
        password.grid(row=8, column=1, padx=10)

        repassword = Entry(signup_frame, width=25)
        repassword.grid(row=9, column=1, padx=10)

        submit_button = Button(signup_frame, text="Submit", bd=0.7, padx=115, bg='green', fg='white',command=SaveStudent)
        submit_button.grid(row=10, column=0, columnspan=2, sticky='w', pady=5)

def SaveEmp():
        # DATA validation is done here first like,all fields are filled,password check,unique roll no
        flag = 0   ; day=0 ;month =0 ;year=0
        emp_id_list = []
        cur.execute("select empid from emp")
        con.commit()
        for i in cur:
            emp_id_list.append(i[0])
        if len(eid.get()) == 0 or len(name.get()) == 0 or len(salary.get()) == 0 or len(e_dep.get()) == 0 or len(
                doj.get()) == 0 or len(e_password.get()) == 0 or len(e_repassword.get()) == 0:
            response = messagebox.showerror("Error", "Please Fill all fields")

            flag = 1
        else:
            if not (eid.get()).isnumeric():
                response = messagebox.showerror("Emp ID", "Please Enter Valid Employee ID")

                flag = 1
            if not (name.get()).isalpha():
                response = messagebox.showerror("Invalid Entry", "Enter Valid Name")

                flag = 1
            if e_password.get() != e_repassword.get():
                response = messagebox.showerror("Error", "Password Does not matched")

                flag = 1
            """
            t = list(doj.get())
            if not (t[2] == "/" and t[5] == "/" and t[0].isnumeric() and t[1].isnumeric() and t[3].isnumeric() and t[4].isnumeric() and t[6].isnumeric() and t[7].isnumeric() and t[8].isnumeric() and t[9].isnumeric() and len(doj.get()) == 10) :
                response = messagebox.showerror("DOJ", "DOJ must be  in YYYY/MM/DD format and should be valid")
                Label(Registration_window, text=response).grid()
                flag=1
            """
            year,month,day=(doj.get()).split("/")
            try:
                newDate = datetime.datetime(int(year),int(month),int(day))
            except ValueError:
                flag = 1
                response = messagebox.showerror("DOJ", "DOJ must be  in DD/MM/YYYY format and should be valid")


            if eid.get() in emp_id_list:
                response = messagebox.showerror("Emp ID ", "Emp ID is taken by Another user")

            if not (e_dep.get()).isalpha() :
                response = messagebox.showerror("Department ", "Enter Valid Department name")

                flag=1
            if flag == 0:
                try:
                    insertemp="insert into emp values ('"+eid.get()+"','"+name.get()+"','"+e_password.get()+"','"+e_dep.get()+"','"+doj.get()+"','"+salary.get()+"')"
                    cur.execute(insertemp)
                    con.commit()
                    response = messagebox.showinfo("Success", "Registration Successful")

                    Registration_window.destroy()
                except:
                    response = messagebox.showerror("Invalid", "Check Your Inputs")


def EmployeeRegistration():
    global eid,name,salary,doj,e_dep,e_password,e_repassword
    global Registration_window
    Registration_window = Toplevel()
    Registration_window.title("Signup")
    Registration_window.iconbitmap('F:/Project/Icon.ico')
    Registration_window.geometry("1366x768+0+0")
    Registration_window.config(bg="#486A90")

    Registration_frame = LabelFrame(Registration_window, padx=60, pady=40, bd=4, width='300')
    Registration_frame.grid(row=1, pady=180, padx=480)

    headingFrame1 = Frame(Registration_window, bg="#333945", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Welcome to JSPM Library", fg='black', font=("brush script mt", 30))
    headingLabel.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)

    eid_label = Label(Registration_frame, text="Emp ID", font=("", 10), pady=5)
    eid_label.grid(row=0, column=0, sticky='w')

    Name_label = Label(Registration_frame, text="Name", font=("", 10), pady=5)
    Name_label.grid(row=1, column=0, sticky='w')

    dep_label = Label(Registration_frame, text="Department", font=("", 10), pady=5)
    dep_label.grid(row=2, column=0, sticky='w')

    salary_label = Label(Registration_frame, text="Salary", font=("", 10), pady=5)
    salary_label.grid(row=3, column=0, sticky='w')

    doj_label = Label(Registration_frame, text="DOJ", font=("", 10), pady=5)
    doj_label.grid(row=4, column=0, sticky='w')

    password_label = Label(Registration_frame, text="Password", font=("", 10), pady=5)
    password_label.grid(row=5, column=0, sticky='w')

    repassword_label = Label(Registration_frame, text="Confirm Password", font=("", 10), pady=5)
    repassword_label.grid(row=6, column=0, sticky='w')

    eid = Entry(Registration_frame, width=25)
    eid.grid(row=0, column=1, padx=10)

    name = Entry(Registration_frame, width=25)
    name.grid(row=1, column=1, padx=10)

    e_dep = Entry(Registration_frame, width=25)
    e_dep.grid(row=2, column=1, padx=10)

    salary = Entry(Registration_frame, width=25)
    salary.grid(row=3, column=1, padx=10)

    doj = Entry(Registration_frame, width=25)
    doj.grid(row=4, column=1, padx=10)

    e_password = Entry(Registration_frame, width=25)
    e_password.grid(row=5, column=1, padx=10)

    e_repassword = Entry(Registration_frame, width=25)
    e_repassword.grid(row=6, column=1, padx=10)

    submit_button = Button(Registration_frame, text="Submit", bd=0.7, padx=115, bg='green', fg='white',command=SaveEmp)
    submit_button.grid(row=7, column=0, columnspan=2, sticky='w', pady=5)

def empMenu():
    global headingFrame1, headingFrame2, headingLabel, SubmitBtn, Canvas1, labelFrame, backBtn
    #headingFrame1.destroy()
    #headingFrame2.destroy()
    #headingLabel.destroy()
    #login_frame.destroy()

    root = Toplevel()
    root.title('JSPM Library')
    root.iconbitmap('F:/Project/Icon.ico')
    root.geometry("1360x768+0+0")
    root.config(bg="#486A90")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#456F8A", width=1366, height=768)
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#333945", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="Employee MENU", fg='black',font=("",20))
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    btn1 = Button(root, text="Add Book Details", bg='black', fg='white',command=addBooks)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    btn2 = Button(root, text="Delete Book", bg='black', fg='white',command=delete)
    btn2.place(relx=0.28, rely=0.41, relwidth=0.45, relheight=0.1)

    btn3 = Button(root, text="View Book List", bg='black', fg='white',command=View)
    btn3.place(relx=0.28, rely=0.52, relwidth=0.45, relheight=0.1)

    btn4 = Button(root, text="Search Book", bg='black', fg='white',command=searchBook)
    btn4.place(relx=0.28, rely=0.63, relwidth=0.45, relheight=0.1)

    btn5 = Button(root, text="Issue Book to Student", bg='black', fg='white',command=issueBook)
    btn5.place(relx=0.28, rely=0.74, relwidth=0.45, relheight=0.1)



global password_login ,Email_login,ID_login
headingFrame1 = Frame(root, bg="#333945", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome to JSPM Library", fg='black',font=("brush script mt",30))
headingLabel.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)

login_frame  = LabelFrame(root,padx=80,pady=60,bd=4,width='300')
login_frame.place(x=480,y=210)


ID_label  = Label(login_frame,text="Rollno/EmpID",font=("",10))
ID_label.grid(row=0,column=0,sticky='w',pady=10)

password_label  = Label(login_frame,text="Password",font=("",10))
password_label.grid(row=1,column=0,sticky='w')

ID_login = Entry(login_frame,width=25)
ID_login.grid(row=0,column=1,padx=10)


password_login = Entry(login_frame,width=25)
password_login.grid(row=1,column=1,pady=10,padx=10)

login_button = Button(login_frame,text="Login",bd=0.7,padx=130,bg='blue',fg='white',command=Login)
login_button.grid(row=2,column=0,columnspan=2,sticky='w')

admin_login = Button(login_frame,text="Admin Login",bd=0.7,padx=110,bg='black',fg='white',command=AdminLogin)
admin_login.grid(row=3,column=0,columnspan=2,sticky='w',pady=10)

signup_button = Button(login_frame,text="Student Registration",bd=0.7,padx=10,bg='green',fg='white',command=StudentRegistration)
signup_button.grid(row=4,column=0,sticky='w')

signup_button = Button(login_frame,text="Employee Registration",bd=0.7,padx=12,bg='green',fg='white',command=EmployeeRegistration)
signup_button.grid(row=4,column=1,columnspan=2)


root.mainloop()