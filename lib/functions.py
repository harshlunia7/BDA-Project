def set_window_center(window, width, height):
    w_s = window.winfo_screenwidth()
    h_s = window.winfo_screenheight()
    x_co = (w_s - width) / 2
    y_co = (h_s - height) / 2 - 50
    window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
    window.minsize(width, height)


