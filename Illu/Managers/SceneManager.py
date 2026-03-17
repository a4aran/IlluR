import pygame

from Illu.DeafultObjects.Scene import Scene
from Illu.Settings.FrameData import FrameData


class SceneManager:
    def __init__(self):
        self.__current_scene = 0
        self.__previous_scene = 0

        self.__scenes = []

    def add_scene(self, scene: type[Scene]):
        self.__scenes.append(scene())

    def changeScene(self, scene):
        if scene is None: return
        cur = self.__scenes[self.__current_scene]
        if isinstance(cur,Scene):
            cur.onExit(self.__previous_scene)

        self.__previous_scene = self.__current_scene
        self.__current_scene = scene

        cur = self.__scenes[self.__current_scene]
        if isinstance(cur,Scene):
            cur.onExit(self.__previous_scene)

    def update(self,frameData: FrameData):
        s = self.__scenes[self.__current_scene]
        if isinstance(s,Scene):
            s.update(frameData)
            self.changeScene(s.getChangeSceneData())

    def draw(self,surface: pygame.Surface):
        s = self.__scenes[self.__current_scene]
        if isinstance(s,Scene):
            s.draw(surface)