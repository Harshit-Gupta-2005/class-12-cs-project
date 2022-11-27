import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

try:
    db=pymysql.connect(host='localhost',user='root',password='bruh',db='grocery_store')
    print('connected')
except Exception as e:
    print(e)

board=Tk()
board.title('grocery management system')
def showall():
    nb=Toplevel(board)
    nb.geometry('1100x800')
    trv = ttk.Treeview(nb, selectmode ='browse')
    trv.grid(row=1,column=1,padx=20,pady=20)

    trv["columns"] = ("1", "2", "3","4")

    trv['show'] = 'headings'

    trv.column("1", width = 100, anchor ='c')
    trv.column("2", width = 300, anchor ='w')
    trv.column("3", width = 40, anchor ='c')
    trv.column("4", width = 80, anchor ='c')

    trv.heading("1", text ="Bar code")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Price")
    trv.heading("4", text ="Quantity")
    def exit2():
     res = messagebox.askyesno('confirmation', 'Do you want to kill this window?') 
     if res == True:
         nb.destroy()
    try:
        cr=db.cursor()
        cr.execute('select * from store_items')
        db.commit()
        table=cr.fetchall()
    except Exception as ex:
        messagebox.showerror('Error', ex) 
    
    for dt in table:
        trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3]))
    b2 =Button(nb, text="EXIT", command=exit2)
    b2.grid(row=25,column=2,padx=20,pady=20)

    
def showbar():
    nb=Toplevel(board)
    v=IntVar()

    trv = ttk.Treeview(nb, selectmode ='browse')
    trv.grid(row=1,column=1,padx=20,pady=20)
    
    trv["columns"] = ("1", "2", "3","4")

    trv['show'] = 'headings'
 
    trv.column("1", width = 100, anchor ='c')
    trv.column("2", width = 300, anchor ='w')
    trv.column("3", width = 40, anchor ='c')
    trv.column("4", width = 80, anchor ='c')

    trv.heading("1", text ="Bar code")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Price")
    trv.heading("4", text ="Quantity")
    def exit2():
     res = messagebox.askyesno('confirmation', 'Do you want to kill this window?') 
     if res == True:
         nb.destroy()
    def showit1():
        try:
            query='select * from store_items where bar_code={}'.format(v.get())
            cr=db.cursor()
            cr.execute(query)
            db.commit()
            value=cr.fetchall()
            if value==():
                messagebox.showerror('Error',"value doesn't exist. ENTER A VAID VALUE")
            else:
                for dt in value:
                    trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3]))

        except Exception as ex:
            messagebox.showerror('Error',ex)    

    m = Label(nb,text = "barcode number")
    e = Entry(nb,textvariable=v)
    b=Button(nb,text='calculate',command=showit1)
    b2 =Button(nb, text="EXIT", command=exit2)
    m.grid(row=20,column=1,padx=20,pady=20) 
    e.grid(row=20,column=3,padx=20,pady=20)
    b.grid(row=25,column=1,padx=20,pady=20)
    b2.grid(row=25,column=2,padx=20,pady=20)
    nb.mainloop()

    
def sell():
    nb=Toplevel(board)
    v1=IntVar()
    v2=IntVar()
    def exit2():
     res = messagebox.askyesno('confirmation', 'Do you want to kill this window?') 
     if res == True:
         nb.destroy()
    def showit2():
        try:
            query1='select * from store_items where bar_code={}'.format(v2.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                messagebox.showerror('Error',"value doesn't exist. ENTER A VAID VALUE")
            else:
                print(value)
                query2='update store_items set quantity=quantity-{} where bar_code={}'.format(v1.get(),v2.get())
                cr.execute(query2)
                db.commit()
                print('updated')
        except Exception as ex:
            messagebox.showerror('Error', ex)
    m2 = Label(nb,text = "barcode no.")
    e2 = Entry(nb,textvariable=v2)
    m1 = Label(nb,text = "quantity sold")
    e1 = Entry(nb,textvariable=v1)
    b=Button(nb,text='calculate',command=showit2)
    b2 =Button(nb, text="EXIT", command=exit2)
    m2.pack()
    e2.pack()
    m1.pack()
    e1.pack()
    b.pack()
    b2.pack()
    nb.mainloop()


def buy():
    nb=Toplevel(board)
    v1=IntVar()
    v2=IntVar()
    def exit2():
     res = messagebox.askyesno('confirmation', 'Do you want to kill this window?') 
     if res == True:
         nb.destroy()
    def showit3():
        try:
            query1='select * from store_items where bar_code={}'.format(v2.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                messagebox.showerror('Error',"value doesn't exist. ENTER A VAID VALUE")
            else:
                print(value)
                query2='update store_items set quantity=quantity+{} where bar_code={}'.format(v1.get(),v2.get())
                cr.execute(query2)
                db.commit()
                print('updated')
        except Exception as ex:
            messagebox.showerror('Error',ex)
    m2 = Label(nb,text = "barcode no.")
    e2 = Entry(nb,textvariable=v2)
    m1 = Label(nb,text = "quantity sold")
    e1 = Entry(nb,textvariable=v1)
    b=Button(nb,text='calculate',command=showit3)
    b2 =Button(nb, text="EXIT", command=exit2)
    m2.pack()
    e2.pack()
    m1.pack()
    e1.pack()
    b.pack()
    b2.pack()
    nb.mainloop()

 
def add_new():
    nb=Toplevel(board)
    v1=IntVar()
    v2=StringVar()
    v3=IntVar()
    v4=IntVar()
    def exit2():
     res = messagebox.askyesno('confirmation', 'Do you want to kill this window?') 
     if res == True:
         nb.destroy()
    def showit4():
        try:
            query1='select * from store_items where bar_code={}'.format(v1.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                if v2.get()=='' or v3.get()==0 or v4.get()==0:
                    messagebox.showerror('Error',"some feilds are unfilled .FILL ALL THE FEILDS")
                else:
                    query='insert into store_items values({},"{}",{},{})'.format(v1.get(),v2.get(),v3.get(),v4.get())
                    cr=db.cursor()
                    cr.execute(query)
                    db.commit()
                    print('added')
            else:
                messagebox.showerror('Error',"value already exists")
        except Exception as ex:
            messagebox.showerror('Error',ex)
    m1 = Label(nb,text = "barcode no.")
    e1 = Entry(nb,textvariable=v1)
    m2 = Label(nb,text = "name of the item")
    e2 = Entry(nb,textvariable=v2)
    m3 = Label(nb,text = "price")
    e3 = Entry(nb,textvariable=v3)
    m4 = Label(nb,text = "quantity")
    e4 = Entry(nb,textvariable=v4)
    b=Button(nb,text='calculate',command=showit4)
    b2 =Button(nb, text="EXIT", command=exit2)
    m1.pack()
    e1.pack()
    m2.pack()
    e2.pack()
    m3.pack()
    e3.pack()
    m4.pack()
    e4.pack()
    b.pack()
    b2.pack()
    nb.mainloop()


def delit():
    nb=Toplevel(board)
    v=IntVar()
    def exit2():
     res = messagebox.askyesno('confirmation', 'Do you want to kill this window?') 
     if res == True:
         nb.destroy()
    def showit5():
        try:
            query1='select * from store_items where bar_code={}'.format(v.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                messagebox.showerror('Error',"value doesn't exist. ENTER A VAID VALUE")
            else:
                answer = messagebox.askyesno('confirmation','Are you sure that you want to delete it?')
                if answer:
                    query='delete from store_items where bar_code={}'.format(v.get())
                    cr=db.cursor()
                    cr.execute(query)
                    db.commit()
                    print('deleted')
        except Exception as ex:
            messagebox.showerror('Error', ex)
    m = Label(nb,text = "barcode number")
    e = Entry(nb,textvariable=v)
    b=Button(nb,text='calculate',command=showit5)
    b2 =Button(nb, text="EXIT", command=exit2)
    m.pack()
    e.pack()
    b.pack()
    b2.pack()
    nb.mainloop()
    
def exit1():
     res = messagebox.askyesno('confirmation', 'Do you want to exit this application?')
     if res == True:
         board.destroy()


bb=0
labl=Label(board,text = "WELCOME",font=('Franklin Gothic Demi',110,"bold"))
labl.grid(row=0, pady=5,columnspan=3)
btn =Button(board, text="show all the elements", command=showall,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn.grid(column=0, row=1)
btn2 =Button(board, text="show elements using their barcode", command=showbar,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn2.grid(column=1, row=1, padx=5)
btn3 =Button(board, text="sell items to a customer", command=sell,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn3.grid(column=2, row=1, padx=5)
btn4 =Button(board, text="restock", command=buy,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn4.grid(column=0, row=2, padx=5)
btn5 =Button(board, text="add a new item to stock", command=add_new,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn5.grid(column=1, row=2, padx=5)
btn6 =Button(board, text="delete an item from the stock", command=delit,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn6.grid(column=2, row=2, padx=5)
btn7 =Button(board, text="EXIT", command=exit1,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn7.grid(column=1, row=3, padx=5)
board.mainloop()
