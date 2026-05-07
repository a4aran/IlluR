import pygame

from Illu.Helpers.BucketStorage import BucketStorage
from Illu.Settings.FrameData import FrameData


class Scene:
    def __init__(self):
        self.primaryBucket = BucketStorage()
        self.background_color = (0, 0, 0)
        self.__changeScene = False
        self.__sceneToChangeTo = 0

    def update(self, frameData: FrameData):
        self.primaryBucket.updateAll(frameData)

    def draw(self, surface: pygame.Surface):
        self.primaryBucket.drawAll(surface)

    def onEnter(self,previousScene):
        pass

    def onExit(self,previousScene):
        self.resetSceneChangeData()
        pass

    def _requestSceneChange(self,sceneToChange):
        self.__changeScene = True
        self.__sceneToChangeTo = sceneToChange

    def getChangeSceneData(self):
        if self.__changeScene:
            return self.__sceneToChangeTo
        else:
            return None

    def resetSceneChangeData(self):
        self.__changeScene = False