import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.state('zoomed')
        self.root.title('View Party')
        self.root.config(bg='#00002e')
        self.lb = tkinter.Label(self.root, text='View Party',
        font=('capital', 20, 'bold', 'underline'),fg='#e8ebed',bg='#00002e')
        self.lb.pack(pady=20)

        self.tv = ttk.Treeview(self.root, columns=['Title','Date','Participant_count','Location'])
        self.tv.heading('Title', text='Title')
        self.tv.heading('Date', text='Date')
        self.tv.heading('Participant_count', text='Participant_count')
        self.tv.heading('Location', text='Location')
        self.tv['show'] = 'headings'
        self.treeStyle = ttk.Style()
        self.treeStyle.configure('Treeview', background='#00002e', foreground='white', rowheight=45,
                                 )
        self.treeStyle.map('Treeview', background=[('selected', '#00002e')])
        self.tv.pack(pady=20)

        self.getData()

        self.root.mainloop()

        self.root.mainloop()

    def getData(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select Title,Date,Participant_count,Location from party'
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        for j in self.tv.get_children():
            self.tv.delete(j)
        count = 0
        for i in result:
            self.tv.insert('', index=count, values=i)
            count += 1

#obj = main()