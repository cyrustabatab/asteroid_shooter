import pygame


SCREEN_HEIGHT,SCREEN_WIDTH = 1280,720
window = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

pygame.display.set_caption('Asteroids')







while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    



    pygame.display.update()




