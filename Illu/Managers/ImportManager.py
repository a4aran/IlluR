class ImportManager:
    def __init__(self):
        self.__assets = {
            "images": {"general":{}},
            "animated": {"general":{}},
            "sounds": {"general":{}}
        }

    def getAssetsByName(self,assetName):
        for a in self.__assets:
            for b in self.__assets[a]:
                for c in self.__assets[a][b]:
                    if c == assetName:
                        return self.__assets[a][b][c]
        return None

    def __getAsset(self, assetType, category, name):
        try:
            return self.__assets[assetType][category][name]
        except KeyError:
            if assetType == "images":
                self.__loadImage(category, name)
            elif assetType == "animated":
                return None
            elif assetType == "sounds":
                self.__loadSound(category, name)

    def getStillImage(self, category, name):
        return self.__getAsset("images", category, name)

    def getAnimatedImage(self, category, name):
        return self.__getAsset("animated", category, name)

    def getSound(self, category, name):
        return self.__getAsset("sounds", category, name)

    def __loadImage(self, storageCategory: str, name: str):
        pass

    def loadAnimatedImage(self, path, storageCategory: str, storageName: str, rows: int, columns: int):
        pass

    def __loadSound(self, storageCategory: str, name: str):
        pass