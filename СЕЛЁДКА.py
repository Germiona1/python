from pygame import*

okno = display.set_mode((500,500))
game = True

class Wall(sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = Surface((50,50))
        self.image.fill((241,156,187))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def put(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        press = key.get_pressed()
        if press[K_UP]:
            self.rect.y += 5
        if press[K_DOWN]:
            self.rect.y -= 5

lab = sprite.Group()
level = [
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
    "--WW--WW--",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "---W--W---",
    "W---WW---W",
    "--WW--WW--",
    "W---WW---W",
    "WW--WW--WW",
]

lab = sprite.Group()
x1 = 0
y1 = 0
for i in level:
    x1 = 0
    for j in i:
        if j=="W":
            w1 = Wall(x1,y1)
            lab.add(w1)
        x1 += 50
    y1 += 50

   
while game:
    okno.fill((255,255,255))
    for i in event.get():
        if i.type==QUIT:
            game = False
    for i in lab:
        i.put()
        i.move()
    display.update()
    
    Hi  beach
