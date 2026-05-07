import pygame

import Illu.Settings.config
from Illu.Settings.FrameData import FrameData


class IlluObject:
    def __init__(self):
        self.__id = Illu.Settings.config.config.getId()

    def update(self, frameData: FrameData):
        pass

    def draw(self, surface: pygame.Surface):
        pass

    def getObjectId(self) -> int:
        return self.__id