import pygame as pg


class Level:
    def __init__(self):
        self.platforms = []

        self.platforms.append(pg.Rect(0, 650, 1280, 70))   # floor
        self.platforms.append(pg.Rect(300, 500, 200, 30))  # platform
        self.platforms.append(pg.Rect(700, 400, 150, 30))  # platform

    def draw(self, screen):
        for rect in self.platforms:
            pg.draw.rect(screen, (100, 255, 100), rect)