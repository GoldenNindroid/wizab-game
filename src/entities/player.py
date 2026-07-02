import pygame as pg


class Player:
    def __init__(self):

        # setting up the image for the player sprite
        self.wizarb_image = pg.image.load("images/assets/wizarb.png")

        # player hitbox
        self.rect = self.wizarb_image.get_rect()
        self.rect.x = 41
        self.rect.y = 72

        self.vel_y = 0
        self.speed = 5
        self.gravity = 0.5
        self.jump_height = 16

    #def is_airborne(self):
    #    if self.vel_y != 0:
    #        return True
    #    else:
    #        return False

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pg.K_RIGHT]:
            self.rect.x += self.speed

        if keys[pg.K_UP]:
            self.rect.y -= self.jump_height
            #airborne = self.is_airborne()
           # while airborne:
        self.vel_y += self.gravity
        self.rect.y += self.vel_y


    def draw(self, screen):
        screen.blit(self.wizarb_image, self.rect)