import pygame

from Illu.Settings.FrameData import FrameData


class Scene:
    def __init__(self):
        self.objects = []
        self.background_color = (0, 0, 0)
        self.__changeScene = False
        self.__sceneToChangeTo = 0

    def update(self, frameData: FrameData):
        for obj in self.objects:
            obj.update(frameData)

    def draw(self, surface: pygame.Surface):
        for obj in self.objects:
            obj.draw(surface)

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