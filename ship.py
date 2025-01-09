import pygame
from laser import Laser


class Ship(pygame.sprite.Sprite):

    def __init__(self,x,y,groups,cool_off=500):

        super().__init__(groups)

        self.image = pygame.image.load('graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x,y))
        self.cool_off = cool_off
        self.last_laser_shot = None
        self.can_shoot = False

    
    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos



    



    

    def laser_shoot(self,lasers_group):
        current_time = pygame.time.get_ticks()
        if  not self.can_shoot and (not self.last_laser_shot or (current_time - self.last_laser_shot >= self.cool_off)):
            self.can_shoot = True
            self.last_laser_shot = current_time
        if self.can_shoot and pygame.mouse.get_pressed()[0]: 
            Laser(*self.rect.midtop,lasers_group)
            self.can_shoot = False




    def update(self,lasers_group):
        self.input_position()
        self.laser_shoot(lasers_group)



