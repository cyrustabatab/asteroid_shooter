import pygame,random




class Meteor(pygame.sprite.Sprite):
    
    SCALES = [0.5,0.75,1,1.5,1.75,2]

    ROTATION_SPEED = 10

    def __init__(self,topleft_x,topleft_y,groups):

        super().__init__(groups)


        image = pygame.image.load('graphics/meteor.png').convert_alpha()

        self.image = pygame.transform.rotozoom(image,0,random.choice(self.SCALES))
        self.original_image = self.image




        self.rect = self.image.get_rect(topleft=(topleft_x,topleft_y))

        self.direction = pygame.math.Vector2(random.random() * random.choice([-1,1]),1 )

        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.speed = random.randint(400,600)

        self.angle = 0
        self.rotate_direction = random.choice([-1,1])
    
    def rotate(self,dt):


        self.angle +=  self.rotate_direction * self.ROTATION_SPEED * dt
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect(center=center)








        



    def update(self,dt):

        self.pos += self.direction * self.speed * dt
        self.rotate(dt)
        self.rect.topleft = tuple(map(round,self.pos))





