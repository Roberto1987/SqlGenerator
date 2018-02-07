from tkinter import *

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    def __init__(self, master=None):
        # parameters that you want to send through the Frame class
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the "file" and "edit" object
        # that will be displayed on the bar menu
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

        # creating and placing a button instance
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

    @staticmethod
    def client_exit():
        exit()






root = Tk()
# size of the window
root.geometry("400x300")
app = Window(root)
root.mainloop()
