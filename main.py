import pygame
pygame.init()
from ship import Ship
from laser import Laser

clock = pygame.time.Clock()


SCREEN_HEIGHT,SCREEN_WIDTH = 1280,720
window = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

pygame.display.set_caption('Asteroids')




background_image = pygame.image.load('graphics/background.png')

spaceship_group = pygame.sprite.Group()
lasers_group = pygame.sprite.Group()
ship = Ship(SCREEN_HEIGHT//2,SCREEN_WIDTH//2,spaceship_group)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    
    dt = clock.tick()/ 1000 


    # update

    spaceship_group.update(lasers_group)
    lasers_group.update(dt)

    # graphics

    window.blit(background_image,(0,0))
    spaceship_group.draw(window)
    lasers_group.draw(window)



        

    
    # draw the frame
    pygame.display.update()




