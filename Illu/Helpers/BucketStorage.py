import pygame

from Illu.Core.HoverableObject import HoverableObject
from Illu.Core.IlluObject import IlluObject
from Illu.Settings.FrameData import FrameData


class BucketStorage:
    def __init__(self):
        self._storage = {}
        self._shouldCheck = True

    def setStorage(self,compilation: list[IlluObject] | dict[[int,IlluObject]]):
        self._storage = {}

        if isinstance(compilation,dict):
            compilation = compilation.values()

        for o in compilation:
            self._storage[o.getObjectId()] = o

        self._shouldCheck = True

    def getObject(self,objectId: int) -> IlluObject:
        return self._storage[objectId]

    def getAll(self) -> list:
        return self._storage.values()

    def deleteObject(self,objectId: int):
        self._storage.pop(objectId)

    def addObject(self,object: IlluObject):
        self._storage[object.getObjectId()] = object
        self._shouldCheck = True

    def __checkQuality(self):
        self._storage = {o.getObjectId(): o for o in self._storage.values() if isinstance(o,IlluObject)}

    def updateAll(self,frameData: FrameData):
        if self._shouldCheck:
            self.__checkQuality()
            self._shouldCheck = False
        for o in self._storage.values():
            o.update(frameData)

    def drawAll(self,surface: pygame.Surface):
        for o in self._storage.values():
            o.draw(surface)

    def updateAndDraw(self,frameData: FrameData, surface: pygame.Surface):
        self.updateAll(frameData)
        self.drawAll(surface)