import pygame, time
from TextOnScreen import TextOnScreen

class StartScreen(pygame.sprite.Sprite):
     def __init__(self, width, height, background, textStart):
          pygame.sprite.Sprite.__init__(self)
          self.background = pygame.image.load(background)
          self.startMessage = TextOnScreen(width/2, height/2, 45, (150,150,0), 'Arial', textStart)

     def initialize(self, window):
          window.blit(self.background, (0,0))
          window.blit(self.startMessage.text, self.startMessage.rect)

     def runEvents(self, events, keys, window):, 
          window.blit(self.background, (0,0))
          window.blit(self.startMessage.text, self.startMessage.rect)
          for event in events :
               if(event.type == pygame.KEYUP):
                    return {"nextScene": True}
          return{"nextScene": False}