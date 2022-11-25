import pymysql
from tkinter import *
from tkinter import ttk

try:
    db=pymysql.connect(host='localhost',user='root',password='bruh',db='grocery_store')
    print('connected')
except Exception as e:
    print(e)

board=Tk()
board.geometry('900x700')
board.title('grocery management system')
def showall():
    nb=Toplevel(board)
    # Using treeview widget
    trv = ttk.Treeview(nb, selectmode ='browse')
    trv.grid(row=1,column=1,padx=20,pady=20)
    # number of columns
    trv["columns"] = ("1", "2", "3","4")
    # Defining heading
    trv['show'] = 'headings'
    # width of columns and alignment 
    trv.column("1", width = 100, anchor ='c')
    trv.column("2", width = 300, anchor ='w')
    trv.column("3", width = 40, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    # Headings  
    # respective columns
    trv.heading("1", text ="Bar code")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Price")
    trv.heading("4", text ="Quantity")  
    try:
        cr=db.cursor()
        cr.execute('select * from store_items')
        db.commit()
        table=cr.fetchall()
    except Exception as ex:
        print(ex)
    
    for dt in table:
        trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],dt[3]))
    nb.mainloop()

    
def showbar():
    nb=Toplevel(board)
    v=IntVar()
    def showit1():
        try:
            query='select * from store_items where bar_code={}'.format(v.get())
            cr=db.cursor()
            cr.execute(query)
            db.commit()
            value=cr.fetchall()
            if value==():
                print('does not exist')
            else:
                print(value)
        except Exception as ex:
            print(ex)

    m = Label(nb,text = "barcode number")
    e = Entry(nb,textvariable=v)
    b=Button(nb,text='calculate',command=showit1)
    m.pack()
    e.pack()
    b.pack()
    
    
def sell():
    nnb=Toplevel(board)
    v1=IntVar()
    v2=IntVar()
    def showit2():
        try:
            query1='select * from store_items where bar_code={}'.format(v2.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                print('does not exist')
            else:
                print(value)
                query2='update store_items set quantity=quantity-{} where bar_code={}'.format(v1.get(),v2.get())
                cr.execute(query2)
                db.commit()
                print('updated')
        except Exception as ex:
            print(ex)
    m2 = Label(nnb,text = "barcode no.")
    e2 = Entry(nnb,textvariable=v2)
    m1 = Label(nnb,text = "quantity sold")
    e1 = Entry(nnb,textvariable=v1)
    b=Button(nnb,text='calculate',command=showit2)
    m2.pack()
    e2.pack()
    m1.pack()
    e1.pack()
    b.pack()
    nnb.mainloop()



def buy():
    nnb=Toplevel(board)
    v1=IntVar()
    v2=IntVar()
    def showit3():
        try:
            query1='select * from store_items where bar_code={}'.format(v2.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                print('does not exist')
            else:
                print(value)
                query2='update store_items set quantity=quantity+{} where bar_code={}'.format(v1.get(),v2.get())
                cr.execute(query2)
                db.commit()
                print('updated')
        except Exception as ex:
            print(ex)
    m2 = Label(nnb,text = "barcode no.")
    e2 = Entry(nnb,textvariable=v2)
    m1 = Label(nnb,text = "quantity sold")
    e1 = Entry(nnb,textvariable=v1)
    b=Button(nnb,text='calculate',command=showit3)
    m2.pack()
    e2.pack()
    m1.pack()
    e1.pack()
    b.pack()
    nnb.mainloop()

 
def add_new():
    nb=Toplevel(board)
    v1=IntVar()
    v2=StringVar()
    v3=IntVar()
    v4=IntVar()
    def showit4():
        try:
            query1='select * from store_items where bar_code={}'.format(v1.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                if v2.get()=='' or v3.get()==0 or v4.get()==0:
                    print('fill in all the details')
                else:
                    query='insert into store_items values({},"{}",{},{})'.format(v1.get(),v2.get(),v3.get(),v4.get())
                    cr=db.cursor()
                    cr.execute(query)
                    db.commit()
                    print('added')
            else:
                print('already exists')
        except Exception as ex:
            print(ex)
    m1 = Label(nb,text = "barcode no.")
    e1 = Entry(nb,textvariable=v1)
    m2 = Label(nb,text = "name of the item")
    e2 = Entry(nb,textvariable=v2)
    m3 = Label(nb,text = "price")
    e3 = Entry(nb,textvariable=v3)
    m4 = Label(nb,text = "quantity")
    e4 = Entry(nb,textvariable=v4)
    b=Button(nb,text='calculate',command=showit4)
    m1.pack()
    e1.pack()
    m2.pack()
    e2.pack()
    m3.pack()
    e3.pack()
    m4.pack()
    e4.pack()
    b.pack()
    nb.mainloop()




def delit():
    nb=Toplevel(board)
    v=IntVar()
    def showit5():
        try:
            query1='select * from store_items where bar_code={}'.format(v.get())
            cr=db.cursor()
            cr.execute(query1)
            db.commit()
            value=cr.fetchall()
            if value==():
                print('does not exist')
            else:
                query='delete from store_items where bar_code={}'.format(v.get())
                cr=db.cursor()
                cr.execute(query)
                db.commit()
                print('deleted')
        except Exception as ex:
            print(ex)
    m = Label(nb,text = "barcode number")
    e = Entry(nb,textvariable=v)
    b=Button(nb,text='calculate',command=showit5)
    m.pack()
    e.pack()
    b.pack()
    
    



bb=0
btn =Button(board, text="Press1", command=lambda:showall())
btn.pack()
btn2 =Button(board, text="Press2", command=lambda:showbar())
btn2.pack()
btn3 =Button(board, text="Press3", command=lambda:sell())
btn3.pack()
btn4 =Button(board, text="Press4", command=lambda:buy())
btn4.pack()
btn5 =Button(board, text="Press5", command=lambda:add_new())
btn5.pack()
btn6 =Button(board, text="Press6", command=lambda:delit())
btn6.pack()
btn6 =Button(board, text="EXIT", command=board.destroy)
btn6.pack()
board.mainloop()
