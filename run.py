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

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            window.close()

    gameMaster.update(frameData, display)

    gameOn = not window.close_window