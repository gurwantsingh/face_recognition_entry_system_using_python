import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('600x600')
        self.root.config(bg='#00002e')
        self.title = tkinter.Label(self.root, text='Add Location', font=('arial', 20, 'bold'),fg='#e8ebed',bg='#00002e')
        self.title.pack(pady=10)

        # container widgets
        self.f = tkinter.Frame(self.root,bg='#00002e')
        self.f.pack()

        self.lb1 = tkinter.Label(self.f, text='Enter Location',fg='#e8ebed',bg='#00002e')
        self.lb1.grid(row=0, column=0, padx=5, pady=10)
        self.txt1 = tkinter.Entry(self.f, width=50)
        self.txt1.grid(row=0, column=1, padx=5, pady=10)

        self.btn = tkinter.Button(self.root, text='Submit',activebackground='#288f76',activeforeground='white', command=self.insertLocation)
        self.btn.pack()

        self.root.mainloop()

    def insertLocation(self):
        self.location = self.txt1.get()

        if len(self.location)==0:
            msg.showwarning('', 'Please enter valid location')
        else:
            conn = connect()
            cr = conn.cursor()
            q = f'select * from location where location="{self.location}"'
            cr.execute(q)
            result = cr.fetchone()
            if result is None:
                q = f'insert into location values("{self.location}")'
                cr.execute(q)
                conn.commit()
                msg.showinfo('', 'Location inserted successfuly')
            else:
                msg.showwarning('', 'Location Already Exists')

obj = main()