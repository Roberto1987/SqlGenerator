from tkinter import *
from PIL import Image, ImageTk

# inheriting from the Frame  class.
# #Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
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
        self.globalRow = 2

        self.init_frame()
        self.init_window()

    def createButton(self):
        showHeader = Button(text='Show Header', command=self.displayHeader)
        showFirstTenLines = Button(text='Show first 10 lines', command=lambda: self.displayNextNRow(10))

        showHeader.grid(row=0, column=0)
        showFirstTenLines.grid(row=0, column=1)

    # -----------------------------------------------------
    # Windows GUI definition
    #     Creating bar menu with : ('file','edit','info')
    #        Add to 'file' cascading menu: 'Exit', with exit command
    #        Add to 'edit' cascading menu: 'Undo'
    #        Add to 'info' cascading menu: 'Info'
    # ------------------------------------------------------
    def init_frame(self):
        file = Menu(self.menu)
        edit = Menu(self.menu)
        info = Menu(self.menu)

        # add commands to file.
        file.add_command(label='Exit', command=self.client_exit)
        file.add_command(label='View Header', command=self.displayHeader)
        edit.add_command(label="Undo")
        info.add_command(label='About')

        # add the two objects "file","edit" to the bar menu
        self.menu.add_cascade(label='File', menu=file)
        self.menu.add_cascade(label='Edit', menu=edit)
        self.menu.add_cascade(label='Info', menu=info)
        self.csvReaderInitializer()

    def init_window(self):
        self.master.title('SQL generator')
        self.createButton()

    # --------------------------------------------------------
    # Proper initialization of the reader object
    # --------------------------------------------------------
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

    def displayNextNRow(self, n):
        for i in range(self.globalRow, n + self.globalRow):
            self.displayRow(i)

    # -----------------------------------------------------
    # Display the csv's row 'n'
    # -----------------------------------------------------
    def displayRow(self, row):
        linerow = self.csvRetriever.getCsvRow(row, self.sourcePath)
        lenRow = len(linerow)
        rowElems = []
        for i in range(lenRow):
            j = Label(text=linerow[i], justify='left', padx='5', font=('Helvetica', 10))
            rowElems.append(j)

        for i in range(lenRow):
            rowElems[i].grid(row=self.globalRow, column=i)
        self.globalRow += 1

    # ----------------------------------------------------------
    # Displaying headers
    # ----------------------------------------------------------
    def displayHeader(self):
        tableFields = self.csvRetriever.getHeaderValues(self.sourcePath)
        numberOfFields = len(tableFields)
        fieldLabels = []
        img = PhotoImage(file='../../res/gdot.png').subsample(7, 7)
        for i in range(numberOfFields):
            l = Label(text=tableFields[i], image=img, justify='left', padx='5', font=('Helvetica', 10), compound=LEFT)
            l.image = img.subsample
            fieldLabels.append(l)

        for i in range(numberOfFields):
            fieldLabels[i].grid(row=1, column=i)

        print('fieldLabels size ' + str(len(fieldLabels)))

    @staticmethod
    def client_exit():
        exit()


root = Tk()
# size of the window
root.geometry("600x300")
root.pack_slaves()

app = Window(root)
root.mainloop()
