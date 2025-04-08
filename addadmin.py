import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('600x600')
        self.root.config(bg='#00002e')
        self.heading= tkinter.Label(self.root, text='Add Admin', font=('capital', 30, 'bold'),fg='white',bg='#00002e')
        self.heading.pack(pady=20)

        # container widgets
        self.f = tkinter.Frame(self.root,bg='#00002e')
        self.f.pack()

        self.lb1 = tkinter.Label(self.f, text='Enter Email',fg='white',bg='#00002e')
        self.lb1.grid(row=0, column=0, padx=10, pady=20)
        self.txt1 = tkinter.Entry(self.f, width=50)
        self.txt1.grid(row=0, column=1, padx=5, pady=10)

        self.lb2 = tkinter.Label(self.f, text='Enter Password',fg='white',bg='#00002e')
        self.lb2.grid(row=1, column=0, padx=10, pady=20)
        self.txt2 = tkinter.Entry(self.f, width=50)
        self.txt2.grid(row=1, column=1, padx=5, pady=10)

        self.lb3 = tkinter.Label(self.f, text='Select Role',fg='white',bg='#00002e',activebackground='#264348',activeforeground='white')
        self.lb3.grid(row=2, column=0, padx=10, pady=20)
        self.txt3 = ttk.Combobox(self.f, width=47, values=['Super Admin', 'Admin'], state='readonly')
        self.txt3.grid(row=2, column=1, padx=5, pady=10)

        self.btn = tkinter.Button(self.root, text='Submit',activebackground='#264348',activeforeground='white',pady = 2, command=self.insertAdmin)
        self.btn.pack()

        self.root.mainloop()

    def insertAdmin(self):
        self.email = self.txt1.get()
        self.password = self.txt2.get()
        self.role = self.txt3.get()
        if len(self.email)==0 or len(self.password) == 0 or len(self.role) == 0:
            msg.showwarning('', 'Please Input All Fields')
        else:
            conn = connect()
            cr = conn.cursor()
            q = f'select * from admin where email="{self.email}"'
            cr.execute(q)
            result = cr.fetchone()
            if result is None:
                q = f'insert into admin values(null, "{self.email}","{self.password}","{self.role}")'
                cr.execute(q)
                conn.commit()
                msg.showinfo('', 'Admin inserted successfuly')
            else:
                msg.showwarning('', 'Email Already Exists')

#obj = main()