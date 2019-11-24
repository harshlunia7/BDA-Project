from components import frames, menu
from lib.functions import set_window_center


class MainPage():

    def __init__(self, master=None):
        self.root = master
        set_window_center(self.root, 800, 600)
        menu.MainMenu(self)
        self.current_frame = None
        self.page_frame = {
            "home":frames.myHome,
            "create": frames.myCreate,
            "read": frames.myRead,
            "update": frames.myUpdate,
            "delete": frames.myDelete
        }
        self.open_home()

    def open_page(self, frame_name, title):
        self.root.title(title)
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def open_home(self):
        self.open_page("home", "CRUD Operations")

