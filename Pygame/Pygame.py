import pygame, sys

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
sound1 = pygame.mixer.Sound('Sound1.wav')
sound2 = pygame.mixer.Sound('Sound2.wav')
sound3 = pygame.mixer.Sound('Sound3.wav')
sound4 = pygame.mixer.Sound('Sound4.wav')
pygame.init()
win = pygame.display.set_mode((800, 600))
background_image = pygame.image.load('Background.jpg')
pygame.display.set_caption("Arkanoid")
clock = pygame.time.Clock()

Black = (0, 150, 100)
Grey = (147, 147, 147)
Orange = (150, 0, 150)
Blue = (0, 147, 147)

punkts = [(355, 280, u'Start', (0, 0, 0), (250,250, 250), 0),
          (360, 340, u'Quit', (0, 0, 0), (250, 250, 250), 1)]

class pade():
    def __init__(self, x, y, w, h, color, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.speed = speed
        
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))

class circle():
    def __init__(self, x, y, color, r, speed):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.speed = speed
        
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.r)

class brick():
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))

bricks=[]


ball_x = True
ball_y = True
run = True
rub = True

class Menu():
    def __init__(self, punkts = [120, 140, u'Punkt', (250,250,30), (250,30,250)]):
        self.punkts = punkts
    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True
        font_menu = pygame.font.Font('Font.otf', 50)
        punkt = 0
        while done:
            win.fill((150, 0, 0))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 100 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
                    
            self.render(win, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                            sound1.play(0)
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                            sound1.play(0)
                    if e.key == pygame.K_RETURN: 
                        if punkt == 0:
                            done=False
                            sound2.play(0)
                        elif punkt == 1:
                            pygame.quit()
                            sys.exit()
               
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: 
                    if punkt == 0:
                        done = False
                        sound2.play(0)
                    elif punkt == 1:
                        pygame.quit()
                        sys.exit()
            win.blit(win, (0,0))
            pygame.display.flip()
punkts2 = [(350, 220, u'You lost', (211, 215, 0), (211,215, 0), 0),(355, 280, u'Restart' , (0, 0, 0), (250,250, 250), 0)
          ,(360, 340, u'Quit', (0, 0, 0), (250, 250, 250), 1)]

class Result():
    def __init__(self, punkts2 = [120, 140, u'Punkts', (250,250,30), (250,30,250)]):
        self.punkts2 = punkts2
    def render(self, poverhnost, font, num_punkt2):
        for i in self.punkts2:
            if num_punkt2 == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def result(self):
        done = True
        font_menu = pygame.font.Font('Font.otf', 50)
        punkt2 = 0
        while done:
            win.fill((150, 0, 0))
            mp = pygame.mouse.get_pos()
            for i in self.punkts2:
                if mp[0] > i[0] and mp[0] < i[0] + 100 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt2 = i[5]
                    #sound1.play(0)
                    
            self.render(win, font_menu, punkt2)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    
                    if e.key == pygame.K_UP:
                        if punkt2 > 0:
                            punkt2 -= 1
                            sound1.play(0)
                    if e.key == pygame.K_DOWN:
                        if punkt2 < len(self.punkts2) - 1:
                            if punkt2 < 1:
                                punkt2 += 1
                            sound1.play(0)
                    if e.key == pygame.K_RETURN: 
                        if punkt2 == 0:
                            done = False
                            sound2.play(0)
                        elif punkt2 == 1:
                            pygame.quit()
                            sys.exit()
                        elif punkt2 == 2:
                            game.menu()
               
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: 
                    if punkt2 == 0:
                        done = False
                        sound2.play(0)
                    elif punkt2 == 1:
                        pygame.quit()
                        sys.exit()
            win.blit(win, (0,0))
            pygame.display.flip()

game2 = Result(punkts2)
game = Menu(punkts)
game.menu()
Start = True
while Start:
    bricks.clear()
    k = 1
    x_b = 0
    y_b = 0
    w_b = 40
    h_b = 20

    for i in range(104):
        if x_b < 800:
            if k % 2:
                bricks.append(brick(x_b, y_b, w_b, h_b, Grey)) 
                k += 1
            else: 
                bricks.append(brick(x_b, y_b, w_b, h_b, Blue))
                k += 1
            x_b += 40
        else:
            k += 1
            x_b = 0
            y_b += 20

    k = 100
    lives = 3
    while lives > 0:
        run = True
        p1 = pade(380, 500, 60, 10, Black, 10)
        p2 = circle(300, 400, Orange, 10, 5)
        if ball_x == True:
            ball_x = False
        else: 
            ball_x = True
        ball_y = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            win.blit(background_image, (0, 0))
    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and p1.x > 0:
                p1.x -= p1.speed
            if keys[pygame.K_RIGHT] and p1.x < 800 - p1.w:
                p1.x += p1.speed
    
            p1.draw()
            p2.draw()
    
            for i in range (k):
                bricks[i].draw(win)
            
            for i in range(k):
                if p2.y - p2.r < bricks[i].y + bricks[i].h and p2.x + p2.r < bricks[i].x + bricks[i].w and p2.x - p2.r > bricks[i].x:
                    ball_y = True
                    bricks.pop(i)
                    k -= 1
                    sound1.play(0)
                    break
    
            if ball_x == True:
                p2.x += p2.speed
                if p2.x > 800 - p2.r or p2.x + p2.r > p1.x and p2.x + p2.r < p1.x + p1.w and p2.y > p1.y and p2.y < p1.y + p1.h:
                    ball_x = False
                    sound2.play(0)
            else:
                p2.x -= p2.speed
                if p2.x < 0 + p2.r or p2.x - p2.r < p1.x + p1.w and p2.x + p2.r > p1.x and p2.y > p1.y and p2.y < p1.y + p1.h:
                    ball_x = True
                    sound2.play(0)

            if ball_y == True:
                p2.y += p2.speed
                if p2.y > 640 - (3 * p2.r) / 2:
                    run = False
                    sound4.play(0)
                elif lives > 0 and len(bricks) < 1:
                    sound3.play(0)
                    run = False

                    
                elif p2.y + p2.r > p1.y and p2.x > p1.x and p2.x < (p1.x + p1.w) and p2.y + p2.r < p1.y + p1.h:
                    ball_y = False
                    sound2.play(0)
            else:
                p2.y -= p2.speed
                if p2.y < 0 + p2.r:
                    ball_y = True
                    sound4.play(0)
            pygame.display.update()
            clock.tick(60)
        lives -= 1
        
        
        if lives > 0 and len(bricks) < 1:
            punkts2[0] = (350, 220, u'You won' , (211, 215, 0), (211,215, 0), 0)
            lives = -1
            p2.y = 1000
        else:
            punkts2[0] = (200, 220, u'You lost, your score - '+str(100-len(bricks)), (211, 215, 0), (211,215, 0), 0)
    game2.result()
   
    