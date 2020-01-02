from tkinter import *
from threading import *

class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Avert Climate Doomsday Catastrophe")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

    ##BUTTON
        # creating a button instance
        quitButton = Button(self, text="Exit",command=self.client_exit)
        # placing the button on my window
        quitButton.place(x=0, y=0)

        # creating a button instance
        changeTextButton = Button(self, text="Change Text",command=self.changeText)
        # placing the button on my window
        changeTextButton.place(x=100, y=100)

    ##TEXT
        self.timerReadout = Label(text="Hello World", bg="red", fg="white")
        self.timerReadout.place(x=50, y=0)

        def hello():
            self.changeText()

        t = Timer(2.0, hello())
        t.start()  # after 2 seconds, "hello, world" will be printed





    def changeText(self):
        self.timerReadout['text'] = 'change the value'

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()