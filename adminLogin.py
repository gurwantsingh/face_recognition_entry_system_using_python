import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

import adminDashboard
from connection import connect

class Login:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Admin Login')
        self.root.geometry('500x500')
        self.root.config(background='#00002e')
        self.lb = tkinter.Label(self.root, text='Admin Login', font=('calibri',26,
                                                                     'bold'),fg='#e8ebed',bg='#00002e')
        self.lb.pack(pady=15)
        self.f = tkinter.Frame(self.root, padx=15, pady=15,bg='#00002e',highlightbackground='white',
                               highlightthickness=1)
        self.f.pack()

        self.lb1 = tkinter.Label(self.f, text='Enter Email:',fg='white',bg='#00002e')
        self.txt1 = tkinter.Entry(self.f, width=40)
        self.lb1.grid(row=0, column=0, pady=10, padx=5, sticky='w')
        self.txt1.grid(row=0, column=1, pady=10, padx=5)

        self.lb2 = tkinter.Label(self.f, text='Enter Password:',fg='white',bg='#00002e')
        self.txt2 = tkinter.Entry(self.f, width=40, show='*')
        self.lb2.grid(row=1, column=0, pady=10, padx=5, sticky='w')
        self.txt2.grid(row=1, column=1, pady=10, padx=5)

        self.btn = tkinter.Button(self.root, text='LOGIN', command=self.checkAdmin, width=15,activebackground='#288f76',activeforeground='white')
        self.btn.pack(pady=15)

        self.root.mainloop()

    def checkAdmin(self):
        self.email = self.txt1.get()
        self.password = self.txt2.get()
        conn = connect()
        cr = conn.cursor()
        q = f"select * from admin where email='{self.email}' and password='{self.password}'"
        cr.execute(q)
        result = cr.fetchone()
        if result is None:
            msg.showwarning('','Invalid Email/Password')
        else:
            msg.showinfo('','Login Successfull')
            self.root.destroy()
            print(result)
            adminDashboard.dashboard(email=self.email, role=result[3])

obj = Login()