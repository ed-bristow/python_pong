import pygame

#ball class attributes
#- speed (stays the same)
#- direction (gradient)

clock = pygame.time.Clock()
pygame.init()
FPS = 20
clock.tick(FPS)
dt = clock.tick(80)
delay = 1

black = (0, 0, 0)
purple = (128, 0, 128)
red = (255, 0, 0)

bat_length = 80

screen = pygame.display.set_mode((640,480))
#icon = pygame.image.load('U:\Downloads\smiley-face-7.png')
pygame.display.set_caption("Pong Game")

class bats:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = (255,255,255)

class ball:
    def __init__(self):
        self.xpos = 320
        self.ypos = 240
        self.colour = (255,255,255)
        self.speed = 1
        self.gradient = 1

ball = ball()
bat1 = bats(20,240)
bat2 = bats(610,240)

def default_ball():
    ball.xpos = 320
    ball.ypos = 240

while True:

    delta = clock.tick() / 50.0
    delay -= delta

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_w]:
                bat1.ypos -= 30
                pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_s]:
                bat1.ypos += 30
                pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_o]:
                bat2.ypos -= 30
                pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_l]:
                bat2.ypos += 30
                pygame.display.update()

    if delay <= 0:
        if ball.gradient == 2:
            ball.xpos += (ball.speed * dt)
            ball.ypos += (ball.speed * dt)
        if ball.gradient == 1:
            ball.xpos += (ball.speed * dt)
            ball.ypos -= (ball.speed * dt)
        if ball.gradient == -1:
            ball.xpos -= (ball.speed * dt)
            ball.ypos += (ball.speed * dt)
        if ball.gradient == -2:
            ball.xpos -= (ball.speed * dt)
            ball.ypos -= (ball.speed * dt)
        delay = 1

    if ball.xpos <= 0:
        print("game over")
        default_ball()
    elif ball.xpos >= 640:
        print("game over")
        default_ball()
    if ball.ypos <= 0:
        if ball.gradient == 1:
            ball.gradient = 2
        elif ball.gradient == -2:
            ball.gradient = -1
    elif ball.ypos >= 480:
        if ball.gradient == 2:
            ball.gradient = 1
        elif ball.gradient == -1:
            ball.gradient = -2

    if ball.xpos <= bat1.xpos and ball.xpos >= (bat1.xpos-10) and ball.ypos >= bat1.ypos and ball.ypos <= (bat1.ypos + bat_length):
        if ball.gradient == -2:
            ball.gradient = 1
        elif ball.gradient == -1:
            ball.gradient = 2
    if ball.xpos >= bat2.xpos and ball.xpos <= (bat2.xpos+10) and ball.ypos >= bat2.ypos and ball.ypos <= (bat2.ypos + bat_length):
        if ball.gradient == 2:
            ball.gradient = -1
        elif ball.gradient == 1:
            ball.gradient = -2


    screen.fill(black)
    pygame.draw.circle(screen, ball.colour, (ball.xpos, ball.ypos), 5, 5)
    pygame.draw.rect(screen, bat1.colour, (bat1.xpos, bat1.ypos, 10, bat_length))
    pygame.draw.rect(screen, bat2.colour, (bat2.xpos, bat2.ypos, 10, bat_length))
    pygame.display.update()
