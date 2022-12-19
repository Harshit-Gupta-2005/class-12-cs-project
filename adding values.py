import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
try:
    db=pymysql.connect(host='localhost',user='root',password='bruh',db='grocery_store')
    print('connected')
except Exception as e:
    print(e)

board=Tk()
board.title('grocery management system')

def showall():
    nb=Toplevel(board)
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

    m = Label(nb,text = "Enter barcode number--->")
    e = Entry(nb,textvariable=v)
    b=Button(nb,text='SHOW',command=showit1)
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
    trv.heading("4", text ="Quantity bought by the customer")
    global bb
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
                for i in value:
                    if i[3]<200:
                        messagebox.showwarning("Warning","Stock of this product is near depletion (only {} left) please restock".format(i[3]))
                query2='update store_items set quantity=quantity-{} where bar_code={}'.format(v1.get(),v2.get())
                cr.execute(query2)
                db.commit()
                for dt in value:
                    trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],v1.get()))
                    global bb
                for child in trv.get_children():
                    bb = bb + (trv.item(child)["values"][2])*(trv.item(child)["values"][3])
    
                    m10 = Label(nb,text =bb)
                    m10.grid(row=10,column=2,padx=20,pady=20)
        except Exception as ex:
            messagebox.showerror('Error', ex)
    

    m11 = Label(nb,text ='TOTAL')
            
    m2 = Label(nb,text = "barcode no.")
    e2 = Entry(nb,textvariable=v2)
    m1 = Label(nb,text = "quantity sold")
    e1 = Entry(nb,textvariable=v1)
    b=Button(nb,text='sell',command=showit2)
    b2 =Button(nb, text="EXIT", command=exit2)
    m2.grid(row=20,column=1,padx=20,pady=20)
    e2.grid(row=20,column=2,padx=20,pady=20)
    m1.grid(row=22,column=1,padx=20,pady=20)
    m11.grid(row=10,column=1,padx=20,pady=20)
    e1.grid(row=22,column=2,padx=20,pady=20)
    b.grid(row=23,column=1,padx=20,pady=20)
    b2.grid(row=23,column=10,padx=20,pady=20)
    nb.mainloop()



def buy():
    nb=Toplevel(board)
    v1=IntVar()
    v2=IntVar()
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
    trv.heading("4", text ="Quantity bought")
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
                for dt in value:
                    trv.insert("", 'end',iid=dt[0], text=dt[0],values =(dt[0],dt[1],dt[2],v1.get()))

        except Exception as ex:
            messagebox.showerror('Error',ex)
    m2 = Label(nb,text = "barcode no.")
    e2 = Entry(nb,textvariable=v2)
    m1 = Label(nb,text = "quantity bought for restock")
    e1 = Entry(nb,textvariable=v1)
    b=Button(nb,text='ADD TO STOCK',command=showit3)
    b2 =Button(nb, text="EXIT", command=exit2)
    m2.grid(row=20,column=1,padx=20,pady=20)
    e2.grid(row=20,column=2,padx=20,pady=20)
    m1.grid(row=22,column=1,padx=20,pady=20)
    e1.grid(row=22,column=2,padx=20,pady=20)
    b.grid(row=23,column=1,padx=20,pady=20)
    b2.grid(row=23,column=10,padx=20,pady=20)
    nb.mainloop()

 
def add_new():
    nb=Toplevel(board)
    v1=IntVar()
    v2=StringVar()
    v3=IntVar()
    v4=IntVar()
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
    trv.heading("4", text ="Quantity bought")
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
                    trv.insert("", 'end',iid=v1.get(), text=v1.get(),values =(v1.get(),v2.get(),v3.get(),v4.get()))

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
    b=Button(nb,text='ADD TO STOCK',command=showit4)
    b2 =Button(nb, text="EXIT", command=exit2)
    m1.grid(row=20,column=1,padx=20,pady=20)
    e1.grid(row=20,column=2,padx=20,pady=20)
    m2.grid(row=22,column=1,padx=20,pady=20)
    e2.grid(row=22,column=2,padx=20,pady=20)
    m3.grid(row=23,column=1,padx=20,pady=20)
    e3.grid(row=23,column=2,padx=20,pady=20)
    m4.grid(row=24,column=1,padx=20,pady=20)
    e4.grid(row=24,column=2,padx=20,pady=20)
    b.grid(row=30,column=1,padx=20,pady=20)
    b2.grid(row=30,column=10,padx=20,pady=20)
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
    b=Button(nb,text='DELETE',command=showit5)
    b2 =Button(nb, text="EXIT", command=exit2)
    m.grid(row=20,column=1,padx=20,pady=20)
    e.grid(row=20,column=2,padx=20,pady=20)
    b.grid(row=23,column=1,padx=20,pady=20)
    b2.grid(row=23,column=10,padx=20,pady=20)
    nb.mainloop()
    
def exit1():
     res = messagebox.askyesno('confirmation', 'Do you want to exit this application?')
     if res == True:
         board.destroy()


bb=0
labl=Label(board,text = "WELCOME",font=('Franklin Gothic Demi',110,"bold"))
labl.grid(row=0, pady=5,columnspan=3)
btn =Button(board, text="Show all the elements", command=showall,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn.grid(column=0, row=1)
btn2 =Button(board, text="Show elements using their barcode", command=showbar,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn2.grid(column=1, row=1, padx=5)
btn3 =Button(board, text="Sell items to a customer", command=sell,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn3.grid(column=2, row=1, padx=5)
btn4 =Button(board, text="Restock", command=buy,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn4.grid(column=0, row=2, padx=5)
btn5 =Button(board, text="Add a new item to stock", command=add_new,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn5.grid(column=1, row=2, padx=5)
btn6 =Button(board, text="Delete an item from the stock", command=delit,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn6.grid(column=2, row=2, padx=5)
btn7 =Button(board, text="EXIT", command=exit1,height= 5, width=25,wraplength=250,font=('Franklin Gothic Medium',20))
btn7.grid(column=1, row=3, padx=5)
board.mainloop()
