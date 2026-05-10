from __future__ import annotations

import math

import pygame


class Circle:
    def __init__(self,pos:pygame.Vector2,radius:float):
        self.center = pygame.Vector2(pos[0],pos[1])
        self.r = radius

    def draw(self,surface: pygame.Surface,color: tuple[int,int,int]):
        pygame.draw.circle(surface,color,self.center,self.r)

    def pointCollision(self, point: pygame.Vector2 | tuple[float, float]) -> bool:
        x = self.center[0] - point[0]
        y = self.center[1] - point[1]
        return x ** 2 + y ** 2 <= self.r ** 2

    def circleCollision(self, other: "Circle"):
        x = self.center[0] - other.center[0]
        y = self.center[1] - other.center[1]
        return x ** 2 + y ** 2 <= (self.r + other.r) ** 2
