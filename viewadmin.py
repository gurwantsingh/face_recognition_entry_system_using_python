import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.state('zoomed')
        self.root.title('View Admin')
        self.root.config(bg='#00002e')
        self.lb = tkinter.Label(self.root, text='View Admins',
                                   font=('capital', 20, 'bold', 'underline'),fg='#e8ebed',bg='#00002e')
        self.lb.pack(pady=20)

        self.tv = ttk.Treeview(self.root, columns=['email', 'role'])
        self.tv.heading('email', text='Email')
        self.tv.heading('role', text='Admin Role')
        self.tv['show'] = 'headings'
        self.treeStyle = ttk.Style()
        self.treeStyle.configure('Treeview', background='#00002e', foreground='white', rowheight=45,
                                 )
        self.treeStyle.map('Treeview', background=[('selected', '#00002e')])
        self.tv.pack(pady=20)
        self.tv.bind('<Double-1>', self.update)
        self.getData()

        self.root.mainloop()

    def update(self, event):
        self.data = self.tv.item(self.tv.selection())['values']
        print(self.data)
        self.root1 = tkinter.Toplevel()
        self.root1.geometry('500x500')
        self.title = tkinter.Label(self.root1, text='Update or Delete Admin',
                                   font=('calibri', 24, 'bold'))
        self.title.pack(pady=15)

        self.lb1 = tkinter.Label(self.root1, text='Admin Email:')
        self.lb1.pack(pady=10)
        self.txt1 = tkinter.Entry(self.root1, width=50)
        self.txt1.pack(pady=10)
        self.txt1.insert(0, self.data[0])
        self.txt1.config(state='readonly')

        self.lb2 = tkinter.Label(self.root1, text='Select Role:')
        self.lb2.pack(pady=10)
        self.txt2 = ttk.Combobox(self.root1, width=47,values=['Super Admin', 'Admin'], state='readonly')
        self.txt2.pack(pady=10)
        self.txt2.set(self.data[1])
        self.btn1 = tkinter.Button(self.root1, text='Update', command=self.updateAdmin)
        self.btn2 = tkinter.Button(self.root1, text='Delete', command=self.deleteAdmin)
        self.btn1.pack(pady=10)
        self.btn2.pack(pady=10)

        self.root1.mainloop()

    def updateAdmin(self):
        self.email = self.txt1.get()
        self.role = self.txt2.get()
        conn = connect()
        cr = conn.cursor()
        q = f'update admin set role = "{self.role}" where email="{self.email}"'
        cr.execute(q)
        conn.commit()
        msg.showinfo('','Updation Successful')
        self.root1.destroy()
        self.getData()

    def deleteAdmin(self):
        self.email = self.txt1.get()
        conn = connect()
        cr = conn.cursor()
        q = f'delete from admin where email="{self.email}"'
        cr.execute(q)
        conn.commit()
        msg.showinfo('','Deletion Successful')
        self.root1.destroy()
        self.getData()

    def getData(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select email, role from admin'
        cr.execute(q)
        result = cr.fetchall()
        # print(result)
        for j in self.tv.get_children():
            self.tv.delete(j)
        count = 0
        for i in result:
            self.tv.insert('', index=count, values=i)
            count += 1

#obj = main()