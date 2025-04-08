import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.state('zoomed')
        self.root.config(bg='#00002e')

        self.title = tkinter.Label(self.root, text='View Locations',font=('calibri', 20, 'bold', 'underline'),fg='#e8ebed',bg='#00002e')
        self.title.pack(pady=10)

        self.tv = ttk.Treeview(self.root, columns=['location'])
        self.tv.heading('location', text='Location')

        self.tv['show'] = 'headings'
        self.treeStyle = ttk.Style()
        self.treeStyle.configure('Treeview', background='#00002e', foreground='white', rowheight=45,
                                 )
        self.treeStyle.map('Treeview', background=[('selected', '#00002e')])
        self.tv.pack(pady=20)
        self.getData()

        self.tv.bind('<Double-Button-1>', self.deleteLocation)

        self.root.mainloop()

    def deleteLocation(self, event):
        self.data = self.tv.item(self.tv.selection())['values']
        print(self.data)
        self.root1 = tkinter.Toplevel()
        self.root1.geometry('500x500')
        self.title = tkinter.Label(self.root1, text='Are you sure to delete this Location?',
                                       font=('calibri', 24, 'bold'))
        self.title.pack(pady=15)

        self.deletebutton=tkinter.Button(self.root1, text="DELETE", command=self.delete)
        self.deletebutton.pack()

        self.cancelbutton = tkinter.Button(self.root1, text="CANCEL", command=self.root1.destroy)
        self.cancelbutton.pack()

        self.root1.mainloop()

    def delete(self):
        self.city = self.data[0]
        conn = connect()
        cr = conn.cursor()
        Q = f"delete from location where location='{self.city}'"
        print(Q)
        cr.execute(Q)
        conn.commit()
        msg.showinfo('', 'Deletion Successful')
        self.root1.destroy()
        self.getData()


    def getData(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select location from location'
        cr.execute(q)
        result = cr.fetchall()
        # print(result)
        for j in self.tv.get_children():
            self.tv.delete(j)
        count = 0
        for i in result:
            self.tv.insert('', index=count, values=i)
            count += 1


obj = main()