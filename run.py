import pygame

import game
from Illu.Settings import window
from Illu.Settings.FrameData import FrameData

pygame.init()

sound_device_available = False
try:
    pygame.mixer.init()
except pygame.error:
    pass

display = pygame.display.set_mode(window.window_size)

gameMaster = game.Game()
frameData = FrameData()

clock = pygame.time.Clock()
gameOn = True
while gameOn:
    dt = clock.tick(240) / 1000
    frameData.delta_time = dt
    frameData.mouse_position = pygame.mouse.get_pos()
    frameData.mouse_buttons_click = [False,False,False]

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            window.close()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                frameData.mouse_buttons_click[0] = True
            if e.button == 2:
                frameData.mouse_buttons_click[1] = True
            if e.button == 3:
                frameData.mouse_buttons_click[2] = True

    gameMaster.update(frameData, display)

    gameOn = not window.close_window

    pygame.display.flip()