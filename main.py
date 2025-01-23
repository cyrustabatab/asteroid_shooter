import pygame,random,sys

pygame.init()
from ship import Ship
from laser import Laser
from meteor import Meteor
from score import Score

clock = pygame.time.Clock()


SCREEN_WIDTH,SCREEN_HEIGHT = 1280,720
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Asteroids')


METEOR_SPAWN_INTERVAL = 1000


background_image = pygame.image.load('graphics/background.png')

spaceship_group = pygame.sprite.Group()
lasers_group = pygame.sprite.Group()
meteors_group = pygame.sprite.Group()
ship = Ship(SCREEN_HEIGHT//2,SCREEN_WIDTH//2,spaceship_group)

score = Score((SCREEN_WIDTH//2,SCREEN_HEIGHT - 50))


METEOR_EVENT = pygame.USEREVENT + 2

pygame.time.set_timer(METEOR_EVENT,METEOR_SPAWN_INTERVAL)

met_image_width,met_image_height = pygame.image.load('graphics/meteor.png').get_size()

def get_meteor_position():
    

    return random.randint(-100,SCREEN_WIDTH + 100),random.randint(-150,-50)


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == METEOR_EVENT:
            Meteor(*get_meteor_position(),meteors_group)



    
    dt = clock.tick()/ 1000 


    # update

    spaceship_group.update(lasers_group)
    lasers_group.update(dt)
    meteors_group.update(dt)

    # graphics

    window.blit(background_image,(0,0))
    score.display(window)
    lasers_group.draw(window)
    meteors_group.draw(window)
    spaceship_group.draw(window)



        

    
    # draw the frame
    pygame.display.update()




