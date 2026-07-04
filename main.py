import pygame as pg
from src.entities.player import Player
from src.world.level import Level

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()

player = Player()
level = Level()

running = True
while running:
    clock.tick(60)

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            # jump
            if event.key == pg.K_UP and player.on_ground and player.jump_counter < player.allowed_jump_count:
                player.vel_y = -player.jump_height
                player.jump_counter += 1

            # dash
            if event.key == pg.K_x and player.dash_counter < player.allowed_dash_count and player.dash_cooldown > 45:
                if player.direction_facing == "right":
                    player.rect.x += 100
                else:
                    player.rect.x -= 100
                player.dash_counter += 1
                player.dash_cooldown = 0
                pg.mixer.Sound("sounds/RBD.mp3").play().set_volume(0.75)
                player.show_circle = True

    if player.show_circle and player.dash_timer >= player.dash_duration:
        player.show_circle = False
    player.update(level)

    screen.fill((30, 30, 30))

    level.draw(screen)
    player.draw(screen)

    pg.display.flip()

pg.quit()