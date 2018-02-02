import tkinter as tk

#http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/glossary.html

class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton.grid()


app = Application()
app.master.title('Sample application')
app.mainloop()