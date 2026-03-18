import pygame

from Illu.DeafultObjects.Scene import Scene
from Illu.Managers.ManagerCollector import ManagerCollector
from Illu.Settings.FrameData import FrameData


class GameManager:
    def __init__(self):
        self.collector = ManagerCollector()

        self.collector.scene_manager.add_scene(Scene)

    def update(self,frameData: FrameData,surface: pygame.Surface):
        self.collector.scene_manager.update(frameData)
        self.collector.scene_manager.draw(surface)