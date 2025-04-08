
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect
from tkinter import filedialog
import cv2

class main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('600x600')
        self.root.config(bg='#00002e')
        self.title = tkinter.Label(self.root, text='Add Participants', font=('arial', 20, 'bold'),bg='#00002e',fg='#e8ebed')
        self.title.pack(pady=10)

        # container widgets
        self.f = tkinter.Frame(self.root,bg='#00002e')
        self.f.pack()



        self.lb1 = tkinter.Label(self.f, text='Name',fg='#e8ebed',bg='#00002e')
        self.lb1.grid(row=1, column=0, padx=5, pady=10)
        self.txt1 = tkinter.Entry(self.f, width=50)
        self.txt1.grid(row=1, column=1, padx=5, pady=10)

        self.lb2 = tkinter.Label(self.f, text='Email',fg='#e8ebed',bg='#00002e')
        self.lb2.grid(row=2, column=0, padx=5, pady=10)
        self.txt2 = tkinter.Entry(self.f, width=50)
        self.txt2.grid(row=2, column=1, padx=5, pady=10)

        self.lb3 = tkinter.Label(self.f, text='Mobile',fg='#e8ebed',bg='#00002e')
        self.lb3.grid(row=3, column=0, padx=5, pady=10)
        self.txt3 = tkinter.Entry(self.f, width=50)
        self.txt3.grid(row=3, column=1, padx=5, pady=10)

        self.lb4 = tkinter.Label(self.f, text='Photo',fg='#e8ebed',bg='#00002e')
        self.lb4.grid(row=4, column=0, padx=5, pady=10)
        self.txt4 = tkinter.Entry(self.f, width=50)
        self.txt4.grid(row=4, column=1, padx=5, pady=10)

        self.btn1 = tkinter.Button(self.f, text='Select Image', command=self.selectImage,activebackground='#288f76',activeforeground='white')
        self.btn1.grid(row=4, column=2, padx=5)
        self.txt4.grid(row=4, column=1, padx=5, pady=10)

        self.lb5 = tkinter.Label(self.f, text='Party ID',fg='#e8ebed',bg='#00002e')
        self.lb5.grid(row=5, column=0, padx=5, pady=10)

        self.txt5 = ttk.Combobox(self.f, width=47, values=self.getParty(), state='readonly')
        self.txt5.grid(row=5, column=1, padx=5, pady=10)


        self.btn = tkinter.Button(self.root, text='Submit', command=self.insertParty,width=15,activebackground='#288f76',activeforeground='white')
        self.btn.pack()

        self.root.mainloop()

    def selectImage(self):
        path = filedialog.askopenfilename()
        print(path)
        self.txt4.config(state='normal')
        self.txt4.delete(0,'end')
        self.txt4.insert(0, path)
        self.txt4.config(state='readonly')

        self.img = cv2.imread(path)
        self.checkImage()

    def checkImage(self):
        face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(self.img, 1.1, 4)
        if len(faces) == 0:
            msg.showwarning("",'Invalid Image')
            self.txt4.config(state='normal')
            self.txt4.delete(0, 'end')

    def insertParty(self):
        self.name = self.txt1.get()
        self.email = self.txt2.get()
        self.mobile = self.txt3.get()
        path = f"photos/{self.name}.png"
        cv2.imwrite(path, self.img)
        self.photo = path
        if  len(self.name) == 0 or len(self.email) == 0 or len(self.txt5.get()) == 0 or len(self.mobile)==0 or len(self.photo)==0:
            msg.showwarning('', 'Please Input All Fields')
        else:
            conn = connect()
            cr = conn.cursor()
            q = f"select ID from party where Title='{self.txt5.get()}'"
            cr.execute(q)
            self.partyID = cr.fetchone()[0]
            # q = f'select * from participants where name="{self.name}"'
            # cr.execute(q)
            # result = cr.fetchone()
            # if result is None:
            q = f'insert into participants values(null,"{self.name}","{self.email}","{self.mobile}","{self.photo}","{self.partyID}")'
            cr.execute(q)
            conn.commit()
            msg.showinfo('', 'Participant added successfuly')


    def getParty(self):
        conn = connect()
        cr = conn.cursor()
        q = 'select Title from party'
        cr.execute(q)
        result = cr.fetchall()
        print(result)
        x = []
        for i in result:
            x.append(i[0])
        return x


#obj = main()