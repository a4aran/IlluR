from Custom.Scenes.test import TestSC
from Illu.Managers.GameManager import GameManager


class Game(GameManager):
    def __init__(self):
        super().__init__()

        self.add_scene(TestSC)