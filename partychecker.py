from tkinter import *
from PIL import Image, ImageTk

class viewStatus:
    def __init__(self, img1, img2):
        self.root = Tk()
        self.root.title('Party Checker')
        self.root.state('zoomed')
        self.root.config(background='#43464a')

        self.title =Label(self.root, text='Party Checker', font=('Constantia', 35),
                           padx=10, pady=5, fg='#e8ebed',
                           bg='#43464a')
        self.title.pack()

        # Frames
        self.ImageFrame = Frame(self.root, bg='#43464a',)
        self.ImageFrame.pack()

        self.InfoFrame = Frame(self.root, bg='#3a3d41', highlightbackground='#e8ebed',
                                highlightthickness=3)
        self.InfoFrame.pack(pady=20)

        # INSIDE IMAGE FRAME WILL BE THE SAVED IMAGE AND THE CURRENT IMAGE WHICH ARE SAVED IN THE DATABASE

        savedPic = Image.open(img1)
        savedPic = savedPic.resize((350,350))
        savedImage = ImageTk.PhotoImage(savedPic)
        self.label = Label(self.ImageFrame, image=savedImage)
        self.label.grid(row=0, column=0, padx=40)

        # currentPic = Image.open('programmer.png')
        # currentPic = currentPic.resize((350, 350))
        currentImage = ImageTk.PhotoImage(img2)
        self.label = Label(self.ImageFrame, image=currentImage)
        self.label.grid(row=0, column=1, padx=40)


        # INSIDE INFO FRAME WILL BE THE INFORMATION DISPLAYED

        self.nameLabel = Label(self.InfoFrame, text='NAME :',
                                font=('Arial', 18), padx=20, pady=10,
                                bg='#3a3d41', fg='#e8ebed')
        self.nameLabel.grid(row=0, column=0, sticky='w', padx=20, pady=10)

        self.namevalue = Label(self.InfoFrame, text='_______________',
                               font=('Arial', 17), padx=20, pady=10,
                               bg='#3a3d41', fg='#e8ebed')
        self.namevalue.grid(row=0, column=1, sticky='w', padx=20, pady=10)


        self.ageLabel = Label(self.InfoFrame, text='AGE :',
                               font=('Arial', 18), padx=20, pady=10,
                               bg='#3a3d41', fg='#e8ebed')
        self.ageLabel.grid(row=1, column=0, sticky='w', padx=20, pady=10)

        self.agevalue = Label(self.InfoFrame, text='_______________',
                               font=('Arial', 17), padx=20, pady=10,
                               bg='#3a3d41', fg='#e8ebed')
        self.agevalue.grid(row=1, column=1, sticky='w', padx=20, pady=10)


        self.statusLabel = Label(self.InfoFrame, text='INVITATION STATUS :',
                               font=('Arial', 18), padx=20, pady=10,
                               bg='#3a3d41', fg='#e8ebed')
        self.statusLabel.grid(row=2, column=0, sticky='w', padx=20, pady=10)

        self.statusvalue = Label(self.InfoFrame, text='_______________',
                               font=('Arial', 17), padx=20, pady=10,
                               bg='#3a3d41', fg='#e8ebed')
        self.statusvalue.grid(row=2, column=1, sticky='w', padx=20, pady=10)


        self.root.mainloop()
# viewStatus()