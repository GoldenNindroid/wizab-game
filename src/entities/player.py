import pygame as pg


class Player:
    def __init__(self):

        # player sprite

        self.image_right = pg.image.load(
            "images/assets/wizarb - right.png"
        ).convert_alpha()

        self.image_left = pg.image.load(
            "images/assets/wizarb - left.png"
        ).convert_alpha()

        self.wizarb_image = self.image_right

        # player things
        self.rect = self.wizarb_image.get_rect()
        self.rect.x = 41
        self.rect.y = 72

        self.direction_facing = "right"
        self.on_ground = False

        # physics
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.gravity = 0.5
        self.current_time = 0

        # jumping
        self.jump_height = 14
        self.jump_counter = 0
        self.allowed_jump_count = 1

        # dashing
        self.dash_counter = 0
        self.allowed_dash_count = 1
        self.dash_cooldown = 0

        #dash sprite
        self.dash_magic_circle_image = pg.image.load("images/assets/magic_circle.png").convert_alpha()
        self.dash_magic_circle_image = pg.transform.scale(self.dash_magic_circle_image, (100,100))
        self.dash_timer = 0
        self.dash_duration = 15
        self.show_circle = False

    def update(self, level):
        keys = pg.key.get_pressed()


        # horizontal movement
        self.vel_x = 0
        self.current_time = pg.time.get_ticks()

        if keys[pg.K_LEFT]:
            self.vel_x = -self.speed
            self.direction_facing = "left"
            self.wizarb_image = self.image_left

        if keys[pg.K_RIGHT]:
            self.vel_x = self.speed
            self.direction_facing = "right"
            self.wizarb_image = self.image_right

        self.rect.x += self.vel_x

        # horizontal collisions
        for collider in level.platforms:
            if self.rect.colliderect(collider):
                if self.vel_x > 0:
                    self.rect.right = collider.left

                elif self.vel_x < 0:
                    self.rect.left = collider.right

        # vertical movement
        self.on_ground = False

        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # vertical collisions
        for collider in level.platforms:
            if self.rect.colliderect(collider):

                # platform collision
                if self.vel_y > 0:
                    self.rect.bottom = collider.top
                    self.vel_y = 0
                    self.on_ground = True

                    self.jump_counter = 0
                    self.dash_counter = 0

                # bottom of platform collision
                elif self.vel_y < 0:
                    self.rect.top = collider.bottom
                    self.vel_y = 0

        self.dash_cooldown += 1
        self.dash_timer += 1
        if not self.show_circle:
            self.dash_timer = 0

    def draw(self, screen):
        screen.blit(self.wizarb_image, self.rect)
        if self.show_circle:
            circle_rect = self.dash_magic_circle_image.get_rect(center=self.rect.center)
            screen.blit(self.dash_magic_circle_image, circle_rect)