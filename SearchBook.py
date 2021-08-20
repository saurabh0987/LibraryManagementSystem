
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


mypass = "root"
mydatabase = "lib_db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"  # Book Table


def search():
    global SearchBtn, labelFrame, lb1, en1, quitBtn, root, Canvas1

    title = en1.get()

    SearchBtn.destroy()
    quitBtn.destroy()
    lb1.destroy()
    en1.destroy()
    labelFrame.destroy()

    labelFrame = Frame(root, bg="#F8EFBA")
    labelFrame.place(relx=0.09, rely=0.3, relwidth=0.784, relheight=0.5)

    bid = Button(labelFrame, text='Book ID', bd=0, bg="#456F8A", fg="white", width=29)
    bid.grid(row=0, column=0, pady=5)
    bid = Button(labelFrame, text='Title', bg="#456F8A", fg="white", bd=0, width=29)
    bid.grid(row=0, column=1, pady=5)
    bid = Button(labelFrame, text='Subject', bg="#456F8A", fg="white", bd=0, width=29)
    bid.grid(row=0, column=2, pady=5)
    bid = Button(labelFrame, text='Author', bg="#456F8A", fg="white", bd=0, width=29)
    bid.grid(row=0, column=3, pady=5)
    bid = Button(labelFrame, text='Status', bg="#456F8A", fg="white", bd=0, width=29)
    bid.grid(row=0, column=4, pady=5)

    searchSql = "select count(*) from " + bookTable
    try:
        rows = cur.execute(searchSql)
        x = cur.fetchall()
        con.commit()
        print(rows)
        print(x[0][0])

        no_rec = x[0][0]  # Total number of rows in table
        limit = 8;  # No of records to be shown per page.

        def my_display(offset):

            q =  "select * from " + bookTable + " where title = '" + title + "' LIMIT " + str(offset) + "," + str(limit)
            cur.execute(q)
            r_set = cur.fetchall()
            i = 1  # row value inside the loop
            b=len(r_set[0])
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
            b1.grid(row=13, column=3, pady=5)
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
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")



    quitBtn = Button(root, text="< Back", bg='#455A64', fg='white', command=searchBook)
    quitBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)


def searchBook():
    global en1, SearchBtn, lb1, labelFrame, quitBtn, Canvas1, root

    root = Tk()
    root.title("JSPM Library")
    root.iconbitmap('F:/Project/Icon.ico')
    root.minsize(width=400, height=400)
    root.geometry("1366x768+0+0")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="white")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.784,relheight=0.5)

    headingFrame1 = Frame(root, bg="#333945", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="SEARCH BOOK", fg='black')
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Enter Title : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SearchBtn = Button(root, text="Search", bg='#264348', fg='white', command=search)
    SearchBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#455A64', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()