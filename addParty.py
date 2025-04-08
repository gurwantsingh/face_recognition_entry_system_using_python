
import tkinter
import tkcalendar
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect


class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('600x600')
        self.root.config(bg='#00002e')
        self.title = tkinter.Label(self.root, text='Add Party', font=('arial', 20, 'bold'),padx=10,pady=15,fg='#e8ebed',bg='#00002e')
        self.title.pack(pady=10)

        # container widgets
        self.f = tkinter.Frame(self.root,bg='#00002e')
        self.f.pack()



        self.lb1 = tkinter.Label(self.f, text='Title',fg='#e8ebed',
                           bg='#00002e')
        self.lb1.grid(row=1, column=0, padx=5, pady=10)
        self.txt1 = tkinter.Entry(self.f, width=50)
        self.txt1.grid(row=1, column=1, padx=5, pady=10)

        self.lb2 = tkinter.Label(self.f, text='Date',fg='#e8ebed',
                           bg='#00002e')
        self.lb2.grid(row=2, column=0, padx=5, pady=10)
        self.txt2 = tkcalendar.DateEntry(self.f, width=50)
        self.txt2.grid(row=2, column=1, padx=5, pady=10)


        self.lb3 = tkinter.Label(self.f, text='Participant_count',fg='#e8ebed',
                           bg='#00002e')
        self.lb3.grid(row=3, column=0, padx=5, pady=10)
        self.txt3 = tkinter.Entry(self.f, width=50)
        self.txt3.grid(row=3, column=1, padx=5, pady=10)

        self.lb4 = tkinter.Label(self.f, text='Location',fg='#e8ebed',
                           bg='#00002e')
        self.lb4.grid(row=4, column=0, padx=5, pady=10)
        locList = self.getLocations()
        self.txt4 = ttk.Combobox(self.f, width=47, values=locList, state='readonly')
        self.txt4.grid(row=4, column=1, padx=5, pady=10)


        self.btn = tkinter.Button(self.root, text='Submit', command=self.insertParty)
        self.btn.pack()

        self.root.mainloop()

    def insertParty(self):
        self.Title = self.txt1.get()
        self.Date = self.txt2.get()
        self.Participant_count = self.txt3.get()
        self.Location = self.txt4.get()
        if  len(self.Title) == 0 or len(self.Date) == 0 or len(self.Participant_count)==0 or len(self.Location)==0:
            msg.showwarning('', 'Please Input All Fields')
        else:
            conn = connect()
            cr = conn.cursor()
            q = f'select * from party where Title ="{self.Title}"'
            cr.execute(q)
            result = cr.fetchone()
            if result is None:
                q = f'insert into party values(null,"{self.Title}","{self.Date}","{self.Participant_count}","{self.Location}")'
                cr.execute(q)
                conn.commit()
                msg.showinfo('', 'Party added successfuly')
            else:
                msg.showwarning('', 'Party Already Exists')

    def getLocations(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select * from location'
        cr.execute(q)
        result = cr.fetchall()
        # print(result)
        x = []
        for i in result:
            x.append(i[0])
        return x
#obj = main()