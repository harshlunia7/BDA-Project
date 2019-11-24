from tkinter import Canvas, Label, Tk
from lib.functions import set_window_center

class Splah(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Program loading")
        self.w = 300
        self.h = 300
        set_window_center(self, self.w, self.h)
        self.resizable(False, False)
        self.splash()

    def splash(self):

        canvas = Canvas(self, width=self.w, height=250, bg="white")
        canvas.create_text(
            self.w / 2, 250 / 2, text="BDA Project : Suicide Rates", font="time 20", tags="string"
        )

        canvas.pack(fill="both")
        Label(self, text="welcome", bg="green", fg="#fff", height=2).pack(
            fill="both", side="bottom"
        )

        self.after(4000, self.destroy)
        self.mainloop()
