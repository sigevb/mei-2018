from tkinter import *

class buttons:
    def __init__(self, master): #master geeft de main aan
        frame = Frame(master) #frame in the main window
        frame.pack()

        self.printButton = Button(frame, text='print dit', command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='quit', command=frame.quit)
        self.quitButton.pack(side=LEFT) #2e van links

    def printMessage(self):
        print('oke lol')

root = Tk()
b = buttons(root)
root.mainloop()

