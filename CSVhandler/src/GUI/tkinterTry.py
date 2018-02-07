from tkinter import *


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame) :

    def __init__(self, master=None):

        # parameters that you want to send through the Frame class
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title('SQL generator')

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit", command=self.client_exit)

        # placing the button on my window
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()



root = Tk()
# size of the window
root.geometry("400x300")
app = Window(root)
root.mainloop()
