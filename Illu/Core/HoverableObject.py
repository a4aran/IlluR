import pygame

from Illu.Core.IlluObject import IlluObject
from Illu.Settings.FrameData import FrameData


class HoverableObject(IlluObject):
    def __init__(self):
        super().__init__()
        self._hoverbox = None
        self.__isHovered = False

    def update(self, frameData: FrameData):
        super().update(frameData)
        self.__isHovered = False
        if isinstance(self._hoverbox,pygame.Rect) and self._hoverbox.collidepoint(frameData.mouse_position):
            self.__isHovered = True

    def getHovered(self) -> bool:
        return self.__isHovered