# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroids_field = AsteroidField()



    Player.containers = (updatable, drawable)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        for obj in updatable:
            obj.update(dt)


        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over")
                sys.exit()


        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        player.draw(screen)
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000   #limit fps to 60

if __name__ == "__main__":
    main()