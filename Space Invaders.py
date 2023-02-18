import pygame
import random as rd

# initialise pygame
pygame.init()

# screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
logo = pygame.image.load('space-game.png')
pygame.display.set_icon(logo)
font = pygame.font.SysFont('arial', 80)
font1 = pygame.font.SysFont('times', 40)
font2 = pygame.font.SysFont('times', 20)


# objects
class Player:
    def __init__(self, x, y, width, height, vel=3):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = vel
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.invul = False

    def draw(self, win, charImg):
        win.blit(charImg, (self.x, self.y))


class Enemy:
    def __init__(self, x, y, width, height, vel=1):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = vel
        self.vely = vel + 31
        self.hitbox = (self.x, self.y, self.x + self.width, self.y + self.height)
        self.gunLoop = rd.randint(0, 150)
        self.going = 'R'

    def draw(self, win, charImg):
        win.blit(charImg, (self.x, self.y))


class Laser:
    def __init__(self, x, y, going='down', width=2, height=10, vel=2):
        self.x = x
        self.y = y
        self.moving = going
        self.width = width
        self.height = height
        self.vel = vel

    def draw(self, win):
        if self.moving == 'up':
            pygame.draw.line(win, (0, 255, 0), (self.x, self.y), (self.x, self.y + self.height), self.width)
        else:
            pygame.draw.line(win, (255, 0, 0), (self.x, self.y), (self.x, self.y - self.height), self.width)


# values
playerX = 400 - 32
playerY = 500
playerWidth = 64
playerHeight = 64
PlayerImg = pygame.image.load('player.png')
PlayerInv = pygame.image.load('playerinv.png')
enemyImg = pygame.image.load('enemy.png')
char = Player(playerX, playerY, 64, 64)
lasers = []
enemies = []
invulnerability = 0
shootLoop = 0
deaths = 0
menu = 1
for o in range(5):
    enemies.append(Enemy(20 + o * 160, 20, 64, 64))
    enemies.append(Enemy(20 + o * 160, 90, 64, 64))


running = True
# game loop
while running:
    screen.fill((0, 0, 0))
    if menu == 1:
        text_a = font.render("Space Invaders", 2, (0, 0, 200))
        text_b = font1.render('Start Game', 1, (255, 255, 255))
        text_c = font1.render('Controls', 1, (255, 255, 255))
        text_d = font1.render('Quit Game', 1, (255, 255, 255))
        screen.blit(text_a, (190, 150))
        screen.blit(text_b, (300, 300))
        pygame.draw.rect(screen, (255, 255, 255), (290, 290, 200, 70), width=2)
        screen.blit(text_c, (320, 400))
        pygame.draw.rect(screen, (255, 255, 255), (290, 390, 200, 70), width=2)
        screen.blit(text_d, (300, 500))
        pygame.draw.rect(screen, (255, 255, 255), (290, 490, 200, 70), width=2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    button = pygame.mouse.get_pos()
                    if 290 <= button[0] <= 490:
                        if 290 <= button[1] <= 360:
                            menu = 0
                        if 390 <= button[1] <= 460:
                            menu = 2
                        if 490 <= button[1] <= 560:
                            running = False

        pygame.display.update()
    elif menu == 2:
        text_e = font.render("Controls", 2, (255, 255, 255))
        text_f = font1.render('Move using WASD or arrow keys.', 1, (255, 255, 255))
        text_g = font2.render('Press E to fire lasers. When you are invulnerable to damage your spaceship changes', 1,
                              (255, 255, 255))
        text_h = font1.render('Laser shooters may fail if there are too', 1, (200, 0, 0))
        text_k = font1.render('many lasers near you', 1, (200, 0, 0))
        text_i = font1.render('But this also applies to enemies', 1, (0, 200, 0))
        text_j = font1.render('Back to Main Menu', 1, (255, 255, 255))
        screen.blit(text_e, (300, 50))
        screen.blit(text_f, (100, 150))
        screen.blit(text_g, (100, 230))
        screen.blit(text_h, (100, 310))
        screen.blit(text_k, (100, 360))
        screen.blit(text_i, (100, 440))
        screen.blit(text_j, (250, 520))
        pygame.draw.rect(screen, (255, 255, 255), (240, 510, 340, 70), width=2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    button = pygame.mouse.get_pos()
                    if 240 <= button[0] <= 580:
                        if 510 <= button[1] <= 580:
                            menu = 1
        pygame.display.update()
    elif menu == 0:
        if len(enemies) < 1:
            text3 = font.render('You Win!', 1, (0, 200, 0))
            text4 = font1.render('Press R to restart', 1, (255, 255, 255))
            text5 = font1.render('Press E to go back to main menu', 1, (255, 255, 255))
            text6 = font1.render('Deaths: ' + str(deaths), 1, (255, 255, 255))
            screen.blit(text3, (270, 200))
            screen.blit(text4, (260, 280))
            screen.blit(text5, (180, 320))
            screen.blit(text6, (300, 360))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        playerX = 400 - 32
                        playerY = 500
                        playerWidth = 64
                        playerHeight = 64
                        char = Player(playerX, playerY, 64, 64)
                        lasers = []
                        enemies = []
                        invulnerability = 0
                        shootLoop = 0
                        deaths = 0
                        for o in range(5):
                            enemies.append(Enemy(20 + o * 160, 20, 64, 64))
                            enemies.append(Enemy(20 + o * 160, 90, 64, 64))
                    elif event.key == pygame.K_e:
                        menu = 1
                        playerX = 400 - 32
                        playerY = 500
                        playerWidth = 64
                        playerHeight = 64
                        char = Player(playerX, playerY, 64, 64)
                        lasers = []
                        enemies = []
                        invulnerability = 0
                        shootLoop = 0
                        deaths = 0
                        for o in range(5):
                            enemies.append(Enemy(20 + o * 160, 20, 64, 64))
                            enemies.append(Enemy(20 + o * 160, 90, 64, 64))
            pygame.display.update()
        else:
            if deaths > 2:
                text = font.render('Game Over!', 1, (200, 0, 0))
                text1 = font1.render('Press R to restart', 1, (255, 255, 255))
                text2 = font1.render('Press E to go back to main menu', 1, (255, 255, 255))
                screen.blit(text, (250, 200))
                screen.blit(text1, (260, 280))
                screen.blit(text2, (180, 320))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            playerX = 400 - 32
                            playerY = 500
                            playerWidth = 64
                            playerHeight = 64
                            char = Player(playerX, playerY, 64, 64)
                            lasers = []
                            enemies = []
                            invulnerability = 0
                            shootLoop = 0
                            deaths = 0
                            for o in range(5):
                                enemies.append(Enemy(20 + o * 160, 20, 64, 64))
                                enemies.append(Enemy(20 + o * 160, 90, 64, 64))
                        elif event.key == pygame.K_e:
                            menu = 1
                            playerX = 400 - 32
                            playerY = 500
                            playerWidth = 64
                            playerHeight = 64
                            char = Player(playerX, playerY, 64, 64)
                            lasers = []
                            enemies = []
                            invulnerability = 0
                            shootLoop = 0
                            deaths = 0
                            for o in range(5):
                                enemies.append(Enemy(20 + o * 160, 20, 64, 64))
                                enemies.append(Enemy(20 + o * 160, 90, 64, 64))
                pygame.display.update()
            else:
                pygame.time.delay(5)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    if char.x < 800 - char.width - char.vel:
                        char.x += char.vel
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    if char.x > char.vel:
                        char.x -= char.vel
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    if char.y < 600 - char.height - char.vel:
                        char.y += char.vel
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    if char.y > char.vel:
                        char.y -= char.vel
                if shootLoop > 20:
                    if keys[pygame.K_e]:
                        if len(lasers) <= 20:
                            lasers.append(Laser(char.x + 7, char.y + 36, 'up'))
                            lasers.append(Laser(char.x + 56, char.y + 36, 'up'))
                    shootLoop = 0
                else:
                    shootLoop += 1
                for e in enemies:
                    e.draw(screen, enemyImg)
                    if e.vel < e.x < 800 - e.width - e.vel:
                        if e.going == 'R':
                            e.x += e.vel
                        else:
                            e.x -= e.vel
                    else:
                        e.y += e.vely
                        if e.going == 'R':
                            e.going = 'L'
                            e.x -= e.vel
                        else:
                            e.going = 'R'
                            e.x += e.vel
                    if not char.invul:
                        if char.x <= e.x <= char.x + char.width or char.x <= e.x + e.width <= char.x + char.width:
                            if char.y <= e.y <= char.y + char.width or char.y <= e.y + e.width <= char.y + char.width:
                                deaths += 1
                                char.invul = True
                    if e.gunLoop > 200:
                        if len(lasers) <= 20:
                            e.gunLoop = rd.randint(0, 150)
                            lasers.append(Laser(e.x + 32, e.y + 64, vel=1))
                    else:
                        e.gunLoop += 1
                if char.invul:
                    if invulnerability > 200:
                        char.invul = False
                        invulnerability = 0
                    else:
                        invulnerability += 1
                for i in lasers:
                    if i.vel < i.y < 604 and i.moving == 'up':
                        i.draw(screen)
                        i.y -= i.vel
                    elif i.y < 600 and i.moving == 'down':
                        i.draw(screen)
                        i.y += i.vel
                    else:
                        lasers.pop(lasers.index(i))
                    if i.moving == 'up':
                        for e in enemies:
                            if e.x <= i.x <= e.x + e.width:
                                if e.y <= i.y <= e.y + e.width:
                                    enemies.pop(enemies.index(e))
                                    lasers.pop(lasers.index(i))
                    elif i.moving == 'down':
                        if not char.invul:
                            if char.x <= i.x <= char.x + char.width:
                                if char.y <= i.y <= char.y + char.width:
                                    deaths += 1
                                    char.invul = True
                                    lasers.pop(lasers.index(i))
                if char.invul:
                    char.draw(screen, PlayerInv)
                else:
                    char.draw(screen, PlayerImg)
                pygame.display.update()

pygame.quit()
