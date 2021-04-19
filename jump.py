import pygame,time,random
pygame.init()
dx,dy = (1000,400)
display = pygame.display.set_mode((dx,dy))
pygame.display.set_caption("Jump")
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (220,0,0)
blue = (0,0,255)
orange = (220,0,220)
font = pygame.font.SysFont("Gadugi",25)
font2 = pygame.font.SysFont("Gadugi",40)
font3 = pygame.font.SysFont("Gadugi",150)
velocity = list([-7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0,
                 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5])

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


class blok:
    def __init__(self,x,y,color,speed=10,size=30):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
    def draw(self):
        pygame.draw.rect(display,black,(self.x,self.y,self.size,self.size))

class player:
    def __init__(self, x, y, py, size,color):
        self.x = x
        self.y = y
        self.size = size
        self.jumping = False
        self.velocity_index = 0
        self.platform_y = py
        self.color = color
    
    def do_jumping(self):
        if self.jumping:
            self.y += velocity[self.velocity_index]
            self.velocity_index += 1
            if self.velocity_index >= len(velocity) - 1:
                self.velocity_index = len(velocity) - 1
            if self.y > self.platform_y:
                self.y = self.platform_y
                self.jumping = False
                self.velocity_index = 0
    
    def draw(self):
            pygame.draw.rect(display, self.color, (self.x,self.y,self.size,self.size))
	
    def do(self):
            self.do_jumping()
            self.draw()
def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop()
                if event.key == pygame.K_q:
##                    intro = False
                    pygame.quit()
                    quit()
        display.fill(white)
        yazi2("Press Space to start to the game, press Q to quit...",50,150,black)
        yazi("Jump with SPACE, go down instantly with S key. Good luck.",50,250,black)
        pygame.display.update()
        clock.tick(5)
def yazi(msg,x,y,color):
    text = font.render(msg,True,color)
    display.blit(text,[x,y])
def yazi2(msg,x,y,color):
    text = font2.render(msg,True,color)
    display.blit(text,[x,y])
def yazi3(msg,x,y,color):
    text = font3.render(msg,True,color)
    display.blit(text,[x,y])

p = player(50,325,325,25,red)
blok1 = blok(1000,320,black)
blok2= blok(1500,320,black)
blok3 = blok(2000,320,black)
def loop():
    skor = 0
    x = 175
    y = 250
    cikis = False
    bitti = False
    r_x1 = random.randrange(250,601, 100)
    r_x2 = random.randrange(250,601, 100)
    r_x3 = random.randrange(250,601, 100)
    while not cikis:
        while bitti == True:
            display.fill(black)
            yazi3("Game Over",90,30,white)
            yazi2("Score: ",100,200,white)
            yazi2(str(skor),220,200,white)
            yazi("Press R to play again, Q  to quit...",100,250,white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cikis = True
                    bitti = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        cikis = True
                        bitti = False
                    if event.key == pygame.K_r:
                        loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cikis = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            p.jumping = True
        if keys[pygame.K_s]:
            if p.jumping:
                p.y += velocity[p.velocity_index]
                p.velocity_index += 3
                if p.velocity_index >= len(velocity) - 1:
                    p.velocity_index = len(velocity) - 1
                if p.y > p.platform_y:
                    p.y = p.platform_y
                    p.jumping = False
                    p.velocity_index = 0

        display.fill(white)
        pygame.draw.rect(display,black,(0,350,1000,5))
        p.do()
        blok1.draw()
        blok2.draw()
        blok3.draw()
        blok1.x -= blok1.speed
        blok2.x -= blok2.speed
        blok3.x -= blok3.speed

        yazi2("Score:",20,20,black)
        yazi2(str(skor),140,20,black)
        if blok1.x <= -50:
            r_x1 = random.randrange(250,601, 100)
            blok1.x = blok3.x + r_x1
##            blok1.x = blok2_rx
            blok1.y = random.randrange(290,321,30)
            blok1.speed += 0.1
            skor += 1
        if blok2.x <= -50:
            r_x2 = random.randrange(250,601, 100)
            blok2.x = blok1.x + r_x2
##            blok2.x = blok2_rx
            blok2.y = random.randrange(290,321,30)
            blok2.speed += 0.1
            skor += 1
            
        if blok3.x <= -50:
            r_x3 = random.randrange(250,601, 100)
            blok3.x = blok2.x + r_x3
##            blok2.x = blok2_rx
            blok3.y = random.randrange(290,321,30)
            blok3.speed += 0.1
            skor += 1


        
        if blok1.y <= p.y <= blok1.y + blok1.size or blok1.y <= p.y + p.size <= blok1.y + blok1.size:
            if blok1.x <= p.x <= blok1.x + blok1.size or blok1.x <= p.x + p.size <= blok1.x + blok1.size:
                bitti = True
                blok1.x = 1000
                blok2.x = blok1.x + 500
                blok3.x = blok2.x + 500
##                break
        if blok2.y <= p.y <= blok2.y + blok2.size or blok2.y <= p.y + p.size <= blok2.y + blok2.size:
            if blok2.x <= p.x <= blok2.x + blok2.size or blok2.x <= p.x + p.size <= blok2.x + blok2.size:
                bitti = True
                blok1.x = 1000
                blok2.x = blok1.x + 500
                blok3.x = blok2.x + 500
##                break
        if blok3.y <= p.y <= blok3.y + blok3.size or blok3.y <= p.y + p.size <= blok3.y + blok3.size:
            if blok3.x <= p.x <= blok3.x + blok3.size or blok3.x <= p.x + p.size <= blok3.x + blok3.size:
                bitti = True
                blok1.x = 1000
                blok2.x = blok1.x + 500
                blok3.x = blok2.x + 500

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
intro()
loop()
