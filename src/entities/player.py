import pygame as pg


class Player:
    def __init__(self):

        # setting up the image for the player sprite
        self.on_ground = None
        self.wizarb_image = pg.image.load("images/assets/wizarb.png")

        # player hitbox
        self.rect = self.wizarb_image.get_rect()
        self.rect.x = 41
        self.rect.y = 72

        self.vel_y = 0
        self.vel_x = 0
        self.speed = 5
        self.gravity = 0.5
        self.jump_height = 14
        self.jump_counter = 0
        self.allowed_jump_count = 1

    def update(self, level):

        # horizontal movement
        keys = pg.key.get_pressed()

        self.vel_x = 0

        if keys[pg.K_LEFT]:
            self.vel_x = -self.speed

        if keys[pg.K_RIGHT]:
            self.vel_x = self.speed

        self.rect.x += self.vel_x


        for collider in level.platforms:
            if self.rect.colliderect(collider):
                if self.vel_x > 0:
                    self.rect.right = collider.left
                elif self.vel_x < 0:
                    self.rect.left = collider.right

        # vertical movement
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        for collider in level.platforms:
            if self.rect.colliderect(collider):
                if self.vel_y > 0:
                    self.rect.bottom = collider.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.jump_counter = 0

                elif self.vel_y < 0:
                    self.rect.top = collider.bottom
                    self.vel_y = 0


    def draw(self, screen):
        screen.blit(self.wizarb_image, self.rect)