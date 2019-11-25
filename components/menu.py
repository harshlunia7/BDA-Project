from tkinter import Menu

from components import frames


class MainMenu:


    def __init__(self, master):
        self.master = master
        self.root = master.root
        self.page_frame = {
            "home":frames.myHome,
            "create": frames.myCreate,
            "read": frames.myRead,
            "update": frames.myUpdate,
            "delete": frames.myDelete,
            "graphs": frames.myGraphs
        }
        self.init_menu()

    def init_menu(self):

        self.menubar = Menu(self.root)

        self.root.config(menu=self.menubar)
        self.current_frame = None
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Create", command=self.file_create)
        filemenu.add_command(label="Read", command=self.file_read)
        filemenu.add_command(label="Update", command=self.file_update)
        filemenu.add_command(label="Delete", command=self.file_delete)
        filemenu.add_command(label="Gaphs", command=self.file_graph)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

        self.menubar.add_cascade(label="CRUD", menu=filemenu)

    def open_page(self, frame_name, title):
        self.root.title(title)
        self.root.config(bg = 'cyan')
        if self.current_frame is not None and (hasattr(self.current_frame.destroy, '__call__')):
            self.current_frame.destroy()

        self.current_frame = self.page_frame[frame_name](self.root)
        self.current_frame.pack()

    def file_read(self):
        self.open_page("read", "Read")

    def file_create(self):
        self.open_page("create", "Create")

    def file_update(self):
        self.open_page("update", "Update")

    def file_delete(self):
        self.open_page("delete", "Delete")

    def file_graph(self):
        self.open_page("graphs", "Graphs")

