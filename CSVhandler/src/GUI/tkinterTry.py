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
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        edit = Menu(menu)
        info = Menu(menu)

        # add commands to file.
        file.add_command(label='Exit', command=self.client_exit)
        edit.add_command(label="Undo")
        info.add_command(label='About')

        # add the two objects "file","edit" to the bar menu
        menu.add_cascade(label='File', menu=file)
        menu.add_cascade(label='Edit', menu=edit)
        menu.add_cascade(label='Info', menu=info)
        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        self.master.title('SQL generator')

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        csvRetriever = CsvRetriever()

        configManager = ConfigManager()
        configManager.setRelativePath('../..')
        configManager.extractProperties()
        sourcePath = os.path.join(os.path.join(
            configManager.relative_path,
            configManager.resourceFolder),
            configManager.filename
        )
        print(sourcePath)

        self.tableFields = csvRetriever.getHeaderValues(sourcePath)  # ['mockCol1', 'mockCol2', 'mockCol3']
        self.displayfields(self.tableFields)

    def displayfields(self, tablefields):
        numberOfFields = len(self.tableFields)
        fieldLabels = []
        greyDot = PhotoImage('../../res/gdot.png')
        for i in range(numberOfFields):
            fieldLabels.append(Label(text=self.tableFields[i], justify='left', padx='50'))

        print('fieldLabels size ' + str(len(fieldLabels)))
        for i in range(numberOfFields):
            fieldLabels[i].pack(side='top')

    @staticmethod
    def client_exit():
        exit()


root = Tk()
# size of the window
root.geometry("400x300")
app = Window(root)
root.mainloop()
