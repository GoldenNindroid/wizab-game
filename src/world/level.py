import pygame as pg


class Level:
    def __init__(self):
        self.ground = pg.Rect(0, 650, 1280, 70)

    def draw(self, screen):
        pg.draw.rect(screen, (100, 255, 100), self.ground)