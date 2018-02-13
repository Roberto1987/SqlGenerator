import subprocess
from tkinter import *

from src.main.CsvReader import CsvReader


def loadcoreBusiness():
    csvReader = CsvReader()
    csvReader.configManager.setRelativePath('../..')
    csvReader.initialize()
    return csvReader


class GUI(Frame):
    # -------------------------------
    # Init main element of the GUI
    # -------------------------------
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master = master

        self.csvReader = loadcoreBusiness()

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.createBarMenu()

        self.buttonFrame = Frame(root, self, width=300, height=50)
        self.buttonFrame.pack(side=TOP, anchor='nw')

        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(self.canvas)
        self.listbox = Listbox(self.canvas)
        self.queryInsert = Entry(self.canvas, width=100)

        self.init_widget()

    # ---------------------------------
    # init the widget
    # ----------------------

    def init_widget(self):
        self.createCanvas()
        self.createScrollbar()
        self.createListbox()
        self.createButton()
        self.createQueryEntry()

    # ---------------------------------
    # init the canvas
    # ---------------------------------
    def createCanvas(self):
        self.canvas.pack(fill='both', expand=1)

    # ---------------------------------
    # init the scrollbar
    # ---------------------------------
    def createScrollbar(self):
        self.scrollbar.pack(side=RIGHT)
        self.scrollbar.config(command=self.listbox.yview)

    # ---------------------------------
    # init the listbox
    # ---------------------------------
    def createListbox(self):
        self.listbox.pack(fill='both', expand=1)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

    def addElementsToListBox(self):
        for i in range(2, 12):
            self.listbox.insert(END, " , ".join(self.csvReader.csvRetriever.getCsvRow(i, self.csvReader.sourcePath)))

    def createBarMenu(self):
        file = Menu(self.menu)
        edit = Menu(self.menu)
        info = Menu(self.menu)

        # add commands to file.
        file.add_command(label='Exit', command=sys.exit)
        edit.add_command(label="Undo")
        info.add_command(label='About')

        # add the two objects "file","edit" to the bar menu
        self.menu.add_cascade(label='File', menu=file)
        self.menu.add_cascade(label='Edit', menu=edit)
        self.menu.add_cascade(label='Info', menu=info)

    def createButton(self):
        showHeader = Button(self.buttonFrame, text='Show Header', command=self.showHeader)
        showFirstTenLines = Button(self.buttonFrame, text='Show first 10 lines', command=self.addElementsToListBox)
        windowsExplorer = Button(self.buttonFrame, text='Find source', command=self.findFolder, state='disabled')
        startQueryCreation = Button(self.buttonFrame, text='Create Query', command=self.runQuery)

        showHeader.grid(row=0, column=0)
        showFirstTenLines.grid(row=0, column=1)
        windowsExplorer.grid(row=0, column=2)
        startQueryCreation.grid(row=0, column=3)

    def showHeader(self):
        tableFields = self.csvReader.csvRetriever.getHeaderValues(self.csvReader.sourcePath)
        fieldLabels = []
        img = PhotoImage(file='../../res/gdot.png').subsample(7, 7)

        for i in range(len(tableFields)):
            l = Label(self.buttonFrame, text=tableFields[i], image=img, justify='left', padx='5',
                      font=('Helvetica', 10), compound=LEFT)
            l.image = img.subsample
            fieldLabels.append(l)

        for i in range(len(tableFields)):
            fieldLabels[i].grid(row=1, column=i)

    def createQueryEntry(self):
        self.queryInsert.pack(side=BOTTOM, ipady=15, anchor='sw')
        self.queryInsert.insert(0, self.csvReader.insertStatement)

    @staticmethod
    def findFolder():
        subprocess.Popen('C:\\')

    def runQuery(self):
        print(self.csvReader.insertStatement)
        self.csvReader.insertStatement = self.queryInsert.get()
        print(self.csvReader.insertStatement)
        self.csvReader.run()


root = Tk()
root.geometry("600x300")
GUI(root)
app = mainloop()
