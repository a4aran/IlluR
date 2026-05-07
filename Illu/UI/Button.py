from enum import Enum
from typing import Callable

import pygame

from Illu.Core.HoverableObject import HoverableObject
from Illu.Helpers.DeltaTimer import DeltaTimer


class Button(HoverableObject):
    def __init__(self, center_pos: tuple, size: tuple, sprites: list[pygame.Surface]):
        super().__init__()
        self._hoverbox = pygame.Rect((0,0),size)
        self._hoverbox.center = center_pos
        if len(sprites) < 3:
            raise Exception("Button needs at least 3 sprites")
        self._sprites = sprites
        self._state = self._States.DEFAULT
        self._enabled = True
        self._cooldown = DeltaTimer(0.2)
        self._cooldown.setOnCompletionEvent(self.onClick)
        self._clickEventSource = None

    class _States(Enum):
        DEFAULT = 0
        HOVERED = 1
        PRESSED = 2

    def changeClickCooldown(self,cooldown):
        self._cooldown.changeTime(cooldown)

    def update(self,frameData):
        super().update(frameData)
        self._state = self._States.DEFAULT if not self._cooldown.isRunning() else self._States.PRESSED
        if self.getHovered() and self._enabled and self._state == self._States.DEFAULT:
            if frameData.mouse_buttons_click[0]:
                self._state = self._States.PRESSED
                self._cooldown.restart()
            else:
                self._state = self._States.HOVERED
        self._cooldown.update(frameData)

    def onClick(self):
        if self._clickEventSource is not None:
            self._clickEventSource()

    def setClickEventSource(self,function: Callable):
        self._clickEventSource = function

    def draw(self,screen: pygame.Surface):
        i = self._state.value if self._enabled else 2
        screen.blit(self._sprites[i],self._hoverbox.topleft)