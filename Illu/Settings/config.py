class ConfigManager:
    def __init__(self):
        self.__idTracker = 0

    def getId(self) -> int:
        self.__idTracker +=1
        return self.__idTracker

config = ConfigManager()
