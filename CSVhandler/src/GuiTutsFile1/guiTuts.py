from tkinter import *

from src.main.CsvReader import CsvReader
from src.main.CsvRetriever import CsvRetriever


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

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.main_frame()

        self.buttonFrame = Frame(root, self, width=300, height=50)
        self.buttonFrame.pack(side=TOP, anchor='nw')

        self.canvas = Canvas(root)
        self.scrollbar = Scrollbar(self.canvas)
        self.listbox = Listbox(self.canvas)
        self.createButton()

        self.csvReader = loadcoreBusiness()

        self.init_widget()

    # ---------------------------------
    # init the widget
    # ---------------------------------
    def init_widget(self):
        self.createCanvas()
        self.createScrollbar()
        self.createListbox()

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

        for i in range(1, 100):
            self.listbox.insert(END, self.csvReader.csvRetriever.getCsvRow(i, self.csvReader.sourcePath))

    def main_frame(self):
        file = Menu(self.menu)
        edit = Menu(self.menu)
        info = Menu(self.menu)

        # add commands to file.
        file.add_command(label='Exit', command=sys.exit)
        file.add_command(label='View Header')
        edit.add_command(label="Undo")
        info.add_command(label='About')

        # add the two objects "file","edit" to the bar menu
        self.menu.add_cascade(label='File', menu=file)
        self.menu.add_cascade(label='Edit', menu=edit)
        self.menu.add_cascade(label='Info', menu=info)

    def createButton(self):
        showHeader = Button(self.buttonFrame, text='Show Header')
        showFirstTenLines = Button(self.buttonFrame, text='Show first 10 lines')

        showHeader.grid(row=0, column=0)
        showFirstTenLines.grid(row=0, column=1)


root = Tk()
root.geometry("600x300")
l = GUI(root)
app = mainloop()
