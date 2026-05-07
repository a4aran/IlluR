import pygame

from Custom.Scenes.test import TestSC
from Illu.Core.Scene import Scene
from Illu.Managers.ManagerCollector import ManagerCollector
from Illu.Settings.FrameData import FrameData


class GameManager:
    def __init__(self):
        self.collector = ManagerCollector()

    def update(self,frameData: FrameData,surface: pygame.Surface):
        self.collector.scene_manager.update(frameData)
        self.collector.scene_manager.draw(surface)

    def add_scene(self,scene: type[Scene]):
        self.collector.scene_manager.add_scene(scene)
