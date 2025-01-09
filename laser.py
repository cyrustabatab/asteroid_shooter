import pygame


class Laser(pygame.sprite.Sprite):


    def __init__(self,midbottom_x,midbottom_y,groups):
        super().__init__(groups)


        self.image = pygame.image.load('graphics/laser.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom=(midbottom_x,midbottom_y))

        # float-based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 600




    def update(self,dt): 

        self.pos += self.direction * self.speed * dt
        self.rect.topleft = list(map(round,self.pos))







