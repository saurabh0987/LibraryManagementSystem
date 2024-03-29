
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


mypass = "root"
mydatabase="lib_db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


bookTable = "books" #Book Table


def deleteBook():
    bid_list=[]
    bid = en1.get()
    cur.execute("select bid from "+bookTable)
    con.commit()
    for i in cur:
        bid_list.append(i[0])
    if bid in bid_list:
        deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
        try:
            cur.execute(deleteSql)
            con.commit()
            messagebox.showinfo("Success", "Book Deleted Successfully")
        except:
            messagebox.showinfo("Check Credentials","Please check Book ID",parent=root)
    else:
        messagebox.showinfo("INVALID", "Book ID Doesn't Exist",parent=root)

    print(bid)

    en1.delete(0, END)

    
def delete(): 
    
    global en1,en2,en3,en4,en5,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("JSPM Library")
    root.iconbitmap('F:/Project/Icon.ico')
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#636e72")
    Canvas1.pack(expand=True,fill=BOTH)
        
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)
        
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="DELETE BOOK", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)
    
    root.mainloop()