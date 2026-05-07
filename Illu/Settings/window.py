window_size = (800, 600)
close_window = False

def set_window_size(size: tuple):
    global window_size
    window_size = size

def get_window_center() -> tuple[float,float]:
    global window_size
    return window_size[0] / 2, window_size[1] / 2

def close():
    global close_window
    close_window = True