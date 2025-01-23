import pygame


class Score:

    
    FONT = pygame.font.Font('graphics/subatomic.ttf',50)
    def __init__(self,midbottom):


        self.midbottom = midbottom


    def display(self,surface):

        seconds = f"Score: {pygame.time.get_ticks()//1000}"
        score = self.FONT.render(seconds,True,(255,255,255))

        score_rect = score.get_rect(midbottom=self.midbottom)
        surface.blit(score,score_rect)
        pygame.draw.rect(surface,(255,) * 3,score_rect.inflate(30,30),width=5,border_radius=8)







