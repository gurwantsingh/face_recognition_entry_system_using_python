import os

import cv2
from PIL import Image, ImageTk
from tkinter import Tk, Label, Frame, Button, Toplevel
from deepface import DeepFace
from tkinter.ttk import Labelframe
import connection
import partychecker
import tkinter.messagebox as msg

class main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x600')
        # Container Widgets -> PanedWindow, Frame, Canvas

        self.videFrame = Labelframe(self.root, text='Camera Video', width=500, height=500)
        self.videFrame.pack()
        self.btnFrame = Frame(self.root)
        self.btnFrame.pack(anchor="s")
        self.bt1 = Button(self.btnFrame, text='Start', command=self.startVid)
        self.bt1.pack()
        self.count = 0
        self.bt1 = Button(self.btnFrame, text='Stop', command=self.stopVid)
        self.bt1.pack()

        self.flag = False

        self.label = Label(self.videFrame)
        self.label.pack()
        self.root.mainloop()

    def stopVid(self):
        self.flag = False
        self.count = 0

    def startVid(self):
        self.video = cv2.VideoCapture(0)
        self.flag = True
        self.recoBtn = Button(self.root, text='Capture', command=self.recface)
        self.recoBtn.pack()
        self.show_frames()

    def recface(self):
        self.count += 1
        if self.count >= 5:
            msg.showwarning('', 'Person Not Invited....')
        else:

            images = os.listdir('photos')
            for i in images:
                # print(f'images12/{i}')
                result = DeepFace.verify(img1_path=self.frame, img2_path=f'photos/{i}')
                print(result)
                if result['verified']:
                    self.count = 0
                    self.savedImage = i
                    self.mainImage = self.frame
                    cv2.imwrite('mainimage.png', self.mainImage)
                    name = i.split('.')
                    print(name)
                    self.getDetails(name[0])

    def show_frames(self):
        if self.flag is True:
            self.frame = self.video.read()[1]
            self.img = cv2.flip(self.frame, 1)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
            self.img = Image.fromarray(self.img)

            self.finalImg = ImageTk.PhotoImage(self.img)
            self.label.image = self.finalImg
            self.label.config(image=self.finalImg)
            self.label.after(10, self.show_frames)
        else:
            self.label.config(image='')
            self.video.release()

    def getDetails(self, name):
        # self.personName = self.finalImg.split()[0]
        conn = connection.connect()
        cr = conn.cursor()
        q = f"select * from participants where name = '{name}'"
        cr.execute(q)
        self.data = cr.fetchone()
        print(self.data)
        # partychecker.viewStatus(f'photos/{self.finalImg}', self.frame)
        self.showDetails()


    def showDetails(self):
        self.root1 = Toplevel()
        self.root1.title('Party Checker')
        self.root1.state('zoomed')
        self.root1.config(background='#4b4e6d')

        self.title =Label(self.root1, text='Party Checker', font=('Constantia', 35), padx=10, pady=5, fg='#e8ebed', bg='#4b4e6d')
        self.title.pack()

        # Frames
        self.ImageFrame = Frame(self.root1, bg='#4b4e6d',)
        self.ImageFrame.pack()

        self.InfoFrame = Frame(self.root1, bg='#4b4e6d', highlightbackground='#e8ebed', highlightthickness=3)
        self.InfoFrame.pack(pady=20)

        # INSIDE IMAGE FRAME WILL BE THE SAVED IMAGE AND THE CURRENT IMAGE WHICH ARE SAVED IN THE DATABASE

        savedPic = Image.open(f'photos/{self.savedImage}')
        savedPic = savedPic.resize((350, 350))
        savedImage = ImageTk.PhotoImage(savedPic)
        self.label1 = Label(self.ImageFrame, image=savedImage)
        self.label1.grid(row=0, column=0, padx=40)

        currentPic = Image.open('mainimage.png')
        # currentPic = Image.open(self.finalImg)
        currentPic = currentPic.resize((350, 350))
        currentImage = ImageTk.PhotoImage(currentPic)
        self.label1 = Label(self.ImageFrame, image=currentImage)
        self.label1.grid(row=0, column=1, padx=40)


        # INSIDE INFO FRAME WILL BE THE INFORMATION DISPLAYED

        self.nameLabel = Label(self.InfoFrame, text='NAME :', font=('Constantia', 18), padx=20, pady=10, bg='#4b4e6d', fg='#e8ebed')
        self.nameLabel.grid(row=0, column=0, sticky='w', padx=20, pady=10)

        self.namevalue = Label(self.InfoFrame, text=self.data[1], font=('Constantia', 17), padx=20, pady=10, bg='#4b4e6d', fg='#e8ebed')
        self.namevalue.grid(row=0, column=1, sticky='w', padx=20, pady=10)


        self.ageLabel = Label(self.InfoFrame, text='MOBILE :', font=('Arial', 18), padx=20, pady=10, bg='#4b4e6d', fg='#e8ebed')
        self.ageLabel.grid(row=1, column=0, sticky='w', padx=20, pady=10)

        self.agevalue = Label(self.InfoFrame, text=self.data[3], font=('Constantia', 17), padx=20, pady=10, bg='#4b4e6d', fg='#e8ebed')
        self.agevalue.grid(row=1, column=1, sticky='w', padx=20, pady=10)


        self.statusLabel = Label(self.InfoFrame, text='INVITATION STATUS :', font=('Constantia', 18), padx=20, pady=10, bg='#4b4e6d', fg='#e8ebed')
        self.statusLabel.grid(row=2, column=0, sticky='w', padx=20, pady=10)

        self.statusvalue = Label(self.InfoFrame, text="Invited", font=('Constantia', 17), padx=20, pady=10, bg='#3a3d41', fg='#e8ebed')
        self.statusvalue.grid(row=2, column=1, sticky='w', padx=20, pady=10)


        self.root1.mainloop()



obj = main()
