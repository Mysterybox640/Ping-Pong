from pygame import *

# Variables
FPS = 60

win = display.set_mode((700,500))
display.set_caption("Ping-Pong game")
clock = time.Clock()

# Classes
class GameSprite(sprite.Sprite):
    def __init__(self,sprite_image,sprite_x,sprite_y,sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(25,25))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()