from tkinter import *

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
import os

from src.main.ConfigManager import ConfigManager
from src.main.CsvRetriever import CsvRetriever


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.csvRetriever = CsvRetriever()
        self.sourcePath = ''

        self.init_frame()
        self.init_window()

    # -----------------------------------------------------
    # Windows GUI definition
    #     Creating bar menu with : ('file','edit','info')
    #        Add to 'file' cascading menu: 'Exit', with exit command
    #        Add to 'edit' cascading menu: 'Undo'
    #        Add to 'info' cascading menu: 'Info'
    #------------------------------------------------------
    def init_frame(self):
        file = Menu(self.menu)
        edit = Menu(self.menu)
        info = Menu(self.menu)

        # add commands to file.
        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='View Header', command=self.displayfields)
        edit.add_command(label="Undo")
        info.add_command(label='About')

        # add the two objects "file","edit" to the bar menu
        self.menu.add_cascade(label='File', menu=file)
        self.menu.add_cascade(label='Edit', menu=edit)
        self.menu.add_cascade(label='Info', menu=info)

    def init_window(self):
        self.master.title('SQL generator')

        # allowing the widget to take the full space of the root window
        # self.pack(fill=BOTH, expand=1)

        # self.displayfields()
    #--------------------------------------------------------
    # Proper initialization of the reader object
    #--------------------------------------------------------
    def csvReaderInitializer(self):
        configManager = ConfigManager()
        configManager.setRelativePath('../..')
        configManager.extractProperties()

        self.sourcePath = os.path.join(os.path.join(
            configManager.relative_path,
            configManager.resourceFolder),
            configManager.filename
        )
        print(self.sourcePath)

    #----------------------------------------------------------
    # Displaying fields
    #----------------------------------------------------------
    def displayfields(self):
        self.csvReaderInitializer()
        tableFields = self.csvRetriever.getHeaderValues(self.sourcePath)
        numberOfFields = len(tableFields)
        fieldLabels = []
        # greyDot = PhotoImage('../../res/gdot.png')
        for i in range(numberOfFields):
            fieldLabels.append(Label(text=tableFields[i], justify='left', padx='5', font=('Helvetica', 10)))

        print('fieldLabels size ' + str(len(fieldLabels)))

        for i in range(numberOfFields):
            fieldLabels[i].grid(row=0, column=i)

    @staticmethod
    def client_exit():
        exit()


root = Tk()
# size of the window
root.geometry("600x300")
root.pack_slaves()
app = Window(root)
root.mainloop()
