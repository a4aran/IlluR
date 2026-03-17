window_size = (800, 600)
close_window = False

def set_window_size(size: tuple):
    global window_size
    window_size = size

def close():
    global close_window
    close_window = True