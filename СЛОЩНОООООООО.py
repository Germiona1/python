from pygame import*
from random import randint

scr = display.set_mode((500,500))
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        scr.blit(self.image, (self.rect.x, self.rect.y))
class Wall(sprite.Sprite):
    def __init__(self, x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface((50,50))
        self.image.fill((0,250,0))
        self.rect = rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def risovat(self):
        scr.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT]:
            self.rect.x += 10
        if keys_pressed[K_LEFT]:
            self.rect.x -= 10
clock = time.Clock()
FPS = 61
spisok = [randint(-50,50) for i in range(100)]
pol = sprite.Group()
for i in range (100):
    t1 = Wall(i*51, spisok[i] + 400)
    pol.add(t1)

dobo = GameSprite("dino.jpg", 250,250,1)
while game:
    scr.fill((241,156,187))
    for e in event.get():
        if e.type == QUIT:
            game = False
    for i in pol:
        i.risovat()
        i.move()
    dobo.reset()
    if sprite.spritecollideany(dobo, pol):
        dobo.rect.y -= 1
    else:
        dobo.rect.y += 1
    display.update()
    clock.tick(FPS)