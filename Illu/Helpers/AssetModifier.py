import pygame


def scaleImage(image: pygame.Surface,scaleFactor: float):
    return pygame.transform.scale(image, (int(image.width * scaleFactor), int(image.height * scaleFactor)))

def changeImageSize(image: pygame.Surface, size: tuple):
    return pygame.transform.scale(image, size)