#Создай собственный Шутер!
from random import*
from pygame import*
font.init()
window = display.set_mode((700,500))
display.set_caption("fff")

hero1 = transform.scale(image.load('rocket.png'), (100,100))
background = transform.scale(image.load("galaxy.jpg"),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,66))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Igrok(GameSprite):

    def upravlenie(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT]:
            self.rect.x += 10
        if keys_pressed[K_LEFT]:
            self.rect.x -= 10
        if keys_pressed[K_SPACE]:
            bullet.rect.y = hero1.rect.y
            bullet.rect.x = hero1.rect.x



hero1 = Igrok("rocket.jpg", 10,399)

class Enemy(GameSprite):
    def patrol(self):
        if self.rect.y > 700:
            self.rect.y = 0
            self.rect.x = randint(0,650)
        else:
            self.rect.y += 5
vrag = Enemy("ufo.png", 0,140)

h = 3
hb = 0
fort1 = font.Font(None, 51)

class Pulya(GameSprite):
    def fire(self):
        if self.rect.y >-50:
            self.rect.y -= 7
bullet =Pulya("bullet.png", -10, -10)
game=True
FPS = 61
clock = time.Clock()
while game:
    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    hero1.reset()
    hero1.upravlenie()
    vrag.reset()
    vrag.patrol()
    bullet.reset()
    bullet.fire()
    if sprite.collide_rect(hero1, vrag):
        h -= 1
        vrag.rect.y = 0
        vrag.rect.x = randint(0,650)
    if h == 0:
        game = False
    
    if sprite.collide_rect(vrag, bullet):
        bullet.rect.y = -99
        vrag.rect.y = 0
        vrag.rect.x = randint(0,650)
        hb += 1
    if hb >= 10:
        txt1 = fort1.render("Ты Победил", 1, (241,156,187))
        window.blit(txt1, (300,200))
    display.update()
    clock.tick(FPS)