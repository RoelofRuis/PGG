from Tkinter import *
from canvas import Screen

# The program is a simple object working with the Tkinter package for
# displaying windows.
class Program():
    def __init__(self):
        self.window = Tk()

    def getWindow(self):
        return self.window

    def getScreen(self):
        return Screen(self.window)

    def run(self):
        mainloop()
