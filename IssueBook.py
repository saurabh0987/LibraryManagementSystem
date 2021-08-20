
from tkinter import *
from PIL import ImageTk ,Image
from tkinter import messagebox
import pymysql


mypass = "root"
mydatabase ="lib_db"

con = pymysql.connect(host="localhost" ,user="root" ,password=mypass ,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "issuedetail"  # Issue Table
bookTable = "books"  # Book Table
stuTable = "studetail"  # Student Table
empTable = "emp"  # Employee Table

allRoll = []  # List To store all Roll Numbers
allEmpId = []  # List To store all Employee IDs
allBid = []  # List To store all Book IDs

def issue():

    global issueBtn ,labelFrame ,lb1 ,en1 ,en2 ,en3 ,quitBtn ,root ,Canvas1 ,status

    bid = en1.get()
    issueto = en2.get()
    issueby = en3.get()
    #issueBtn.destroy()
    #quitBtn.destroy()
    #labelFrame.destroy()
    #lb1.destroy()
    #en1.destroy()
    #en2.destroy()
    #en3.destroy()

    def showit():
        root2 = Tk()
        root2.title("JSPM Library")
        root2.iconbitmap('F:/Project/Icon.ico')
        root2.minsize(width=800, height=800)
        root2.geometry("1366x768+0+0")
        labelFrame = Frame(root2, bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.771,relheight=0.5)

        bid1 = Button(labelFrame, text='Book ID', bd=1, bg="#456F8A", fg="white", width=49)
        bid1.grid(row=0, column=0, pady=5)
        bid1 = Button(labelFrame, text='Issue To', bg="#456F8A", fg="white", bd=1, width=49)
        bid1.grid(row=0, column=1, pady=5)
        bid1 = Button(labelFrame, text='Issue By', bg="#456F8A", fg="white", bd=1, width=49)
        bid1.grid(row=0, column=2, pady=5)

        rows = cur.execute("select count(*) from issuedetail")
        x = cur.fetchall()
        con.commit()
        print(rows)
        print(x)
        print(x[0][0])

        no_rec = x[0][0]  # Total number of rows in table
        limit = 8  # No of records to be shown per page.
        backBtn = Button(root2, text="< Back", bg='#455A64', fg='white', command=root2.destroy)
        backBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

        def my_display(offset):

            q = "SELECT * from issuedetail LIMIT " + str(offset) + "," + str(limit)
            cur.execute(q)
            r_set = cur.fetchall()
            i = 1  # row value inside the loop
            b = len(r_set[0])
            for student in r_set:
                for j in range(len(student)):
                    e = Entry(labelFrame, width=30, fg='white', bg="black", font=("", 10))
                    e.grid(row=i, column=j)
                    e.insert(END, student[j])
                i = i + 1
            while (i < limit + 1):  # required to blank the balance rows if they are less
                for j in range(b):
                    e = Entry(labelFrame, width=30, fg='White', bg="black", font=("", 10))
                    e.grid(row=i, column=j)
                    e.insert(END, "")
                i = i + 1
            # Show buttons
            back = offset - limit  # This value is used by Previous button
            next = offset + limit  # This value is used by Next button
            b1 = Button(labelFrame, text='Next >', command=lambda: my_display(next))
            b1.grid(row=13, column=2, pady=5)
            b2 = Button(labelFrame, text='< Prev', command=lambda: my_display(back))
            b2.grid(row=13, column=1, pady=5)
            if (no_rec <= next):
                b1["state"] = "disabled"  # disable next button
            else:
                b1["state"] = "active"  # enable next button

            if (back >= 0):
                b2["state"] = "active"  # enable Prev button
            else:
                b2["state"] = "disabled"  # disable Prev button

        my_display(0)

        root2.mainloop()


    extractBid = "select bid from  " +bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from  " +bookTable +" where bid =  " +bid +""
            cur.execute(checkAvail)
            tm=cur.fetchall()
            con.commit()
            print(tm)
            check=tm[0][0]

            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error" ,"Book ID not present",parent=root1)
    except:
        messagebox.showinfo("Error" ,"Can't fetch Book IDs",parent=root1)

    extractRollno = "select rollno from  " +stuTable
    try:
        cur.execute(extractRollno)
        con.commit()
        for i in cur:
            allRoll.append(i[0])

        if issueto in allRoll:
            pass
        else:
            messagebox.showinfo("Error" ,"Roll No not present",parent=root1)
    except:
        messagebox.showinfo("Error" ,"Can't fetch Roll No",parent=root1)

    extractEmpID = "select empid from  " + empTable
    try:
        cur.execute(extractEmpID)
        con.commit()
        for i in cur:
            allEmpId.append(i[0])

        if issueby in allEmpId:
            pass
        else:
            messagebox.showinfo("Error" ,"Emp ID not present",parent=root1)
    except:
        messagebox.showinfo("Error" ,"Can't fetch Emp IDs",parent=root1)


    issueSql = "insert into  " +issueTable +" values (' " +bid +"',' " +issueto +"',' " +issueby +"')"
    show = "select * from  " +issueTable

    updateStatus = "update  " +bookTable +" set status = 'issued' where bid = '" +bid +"'"
    try:
        if bid in allBid and issueto in allRoll and issueby in allEmpId and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            showit()
        else:
            allBid.clear()
            allEmpId.clear()
            allRoll.clear()
            response = messagebox.showerror("Failed", "Book is already issued to someone",parent=root1 )
            Label(root, text=response).pack()
            return
        con.commit()

    except:
        messagebox.showinfo("Search Error" ,"The value entered is wrong, Try again",parent=root1)

    print(bid)
    print(issueto)
    print(issueby)

    allBid.clear()
    allEmpId.clear()
    allRoll.clear()




def issueBook():

    global en1 ,en2 ,en3 ,issueBtn ,lb1 ,labelFrame ,quitBtn ,Canvas1 ,root1 ,status

    root1 = Tk()
    root1.title("JSPM Library")
    root1.iconbitmap('F:/Project/Icon.ico')
    root1.minsize(width=800 ,height=800)
    root1.geometry("1366x768+0+0")



    Canvas1 = Canvas(root1)

    Canvas1.config(bg="#706fd3")
    Canvas1.pack(expand=True,fill =BOTH)

    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely =0.3,relwidth=0.784,relheight=0.5)

    headingFrame1 = Frame(root1,bg="#333945",bd=5 )
    headingFrame1.place(relx=0.25,rely =0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely =0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="ISSUE BOOK", fg='black')
    headingLabel.place(relx=0.25,rely =0.15, relwidth=0.5, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame,text ="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely =0.2)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely =0.2, relwidth=0.62)

    # Issued To Roll Number
    lb2 = Label(labelFrame,text ="Issued To(rollno) : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely =0.4)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely =0.4, relwidth=0.62)

    # Issued By Employee Number
    lb3 = Label(labelFrame,text ="Issued By(empid) : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely =0.6)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely =0.6, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root1,text ="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely =0.75, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root1,text ="Quit",bg='#aaa69d', fg='black', command=root1.destroy)
    quitBtn.place(relx=0.53,rely =0.75, relwidth=0.18,relheight=0.08)

    root1.mainloop()