import pygame
pygame.init()



#consants
WIDTH = 1400
HEIGHT = 800
TITLE = "A Star Wars Adventure"
BACKGROUND_IMAGE = 'images/space-background.png'
#Background music for the majority of the game
pygame.mixer.music.load('music/main_theme.mp3')
pygame.mixer.music.play(0)

#background level 1
pygame.image.load('images/space-background.png')
background_image = pygame.image.load('images/space-background.png')
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
screen.blit(background_image, [0, 0])

novaclass = pygame.image.load('images/nova-ship.png')

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        #self.pos = image.get_rect(0, height)
        self.draw = pygame.image.load(self.image)
    #def move(self):
        #self.pos = self.pos.move(0, self.speed)
    #if self.pos.right > 600:
    #    self.pos.left = 0
novaship = GameObject('images/nova-ship.png', 80, 10)
novaship.draw()
