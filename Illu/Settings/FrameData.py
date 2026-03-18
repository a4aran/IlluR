import pygame


class FrameData:
    def __init__(self):
        self.delta_time = 0
        self.mouse_position = pygame.Vector2()
        self.mouse_buttons_click = (False,False,False)