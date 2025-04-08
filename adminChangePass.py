import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg

import connection


class main:
    def __init__(self, email):
        self.root = tkinter.Tk()
        self.root.title('Change Password')
        self.root.geometry('500x500')

        self.head = tkinter.Label(self.root, text='Change Password',
                                  font=('calibri',28,'bold'))
        self.head.pack(pady=15)

        self.f = tkinter.Frame(self.root)
        self.f.pack()

        self.lb1 = tkinter.Label(self.f, text='Admin Email:')
        self.txt1 = tkinter.Entry(self.f, width=40)
        self.txt1.insert(0, email)
        self.txt1.config(state='readonly')
        self.lb1.grid(row=0, column=0, pady=10, padx=5)
        self.txt1.grid(row=0, column=1, pady=10, padx=5)

        self.lb2 = tkinter.Label(self.f, text='Enter Old Password:')
        self.txt2 = tkinter.Entry(self.f, width=40, show='*')
        self.lb2.grid(row=1, column=0, pady=10, padx=5)
        self.txt2.grid(row=1, column=1, pady=10, padx=5)

        self.lb3 = tkinter.Label(self.f, text='Enter New Password:')
        self.txt3 = tkinter.Entry(self.f, width=40, show='*')
        self.lb3.grid(row=2, column=0, pady=10, padx=5)
        self.txt3.grid(row=2, column=1, pady=10, padx=5)

        self.btn = tkinter.Button(self.root, text='Submit', command=self.changePass)
        self.btn.pack()

        self.root.mainloop()

    def changePass(self):
        self.email = self.txt1.get()
        self.oldPass = self.txt2.get()
        self.newPass = self.txt3.get()
        conn = connection.connect()
        cr = conn.cursor()
        q = f'select * from admin where email="{self.email}"'
        cr.execute(q)
        result = cr.fetchone()
        if result[1] == self.oldPass:
            q = f"update admin set password='{self.newPass}' where email='{self.email}'"
            cr.execute(q)
            conn.commit()
            msg.showinfo('','Password Changed Successfully')
        else:
            msg.showwarning('','Incorrect Old Password')

#obj = main()