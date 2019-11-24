from tkinter import Tk
from pages import  win_splah
from components.view import  MainPage

class App(Tk):

    def __init__(self):
        win_splah.Splah()
        Tk.__init__(self)

        MainPage(self)

        self.mainloop()



if __name__ == "__main__":
    App()
