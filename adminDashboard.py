import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import addadmin
import adminChangePass
import viewadmin
import addParty
import viewParty
import addParticipants


class dashboard:
    def __init__(self, email, role):
        self.root = tkinter.Tk()
        self.root.title('Admin Dashboard')
        self.root.state('zoomed')
        self.root.config(bg='#00002e')

        self.rootMenu = tkinter.Menu()
        self.root.config(menu=self.rootMenu)
        self.email = email
        print(role)

        if role == 'Super Admin':
          self.adminMenu = tkinter.Menu(self.rootMenu, tearoff=0)
          self.rootMenu.add_cascade(label='Manage Admin', menu=self.adminMenu)
          self.adminMenu.add_command(label='Add Admin', command=self.addAdmin)
          self.adminMenu.add_command(label='View Admin', command=lambda: viewadmin.main())

        self.profileMenu = tkinter.Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Profile', menu=self.profileMenu)
        self.profileMenu.add_command(label='Change Password', command=lambda: adminChangePass.main(email))
        self.profileMenu.add_command(label='Logout', command=lambda: self.root.destroy())

        self.partyMenu = tkinter.Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Manage Parties', menu=self.partyMenu)
        self.partyMenu.add_command(label='Add Party', command=self.addParty)
        self.partyMenu.add_command(label='View Party', command=lambda: viewParty.main())

        self.participantsMenu = tkinter.Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Manage Participants', menu=self.participantsMenu)
        self.participantsMenu.add_command(label='Add Participants', command=self.addParticipants)

        self.lb = tkinter.Label(self.root, text='Welcome to Admin Dashboard', font=(
            'calibri', 28, 'bold'
        ),bg='#00002e',fg='#e8ebed')
        self.lb.pack(pady=20)

        self.root.mainloop()

    def addAdmin(self):
        addadmin.main()
    def addParty(self):
        addParty.main()
    def addParticipants(self):
        addParticipants.main()
#obj = dashboard()
