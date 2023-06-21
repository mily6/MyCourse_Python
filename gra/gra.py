import math
import time
import pygame
import random
import math

#rozpocznij program
pygame.init()

dirtyRects=[]
score=0
#dodaj zegar gry
clock=pygame.time.Clock()

#stworz ekran gry
screen = pygame.display.set_mode((800,600)) #szerokosc, wysokosc
screen.fill((20,150,101)) # Red Green Blue 0 ---> 255

# nazwa gry
pygame.display.set_caption("Zabij Bastiana")

icon = pygame.image.load("assets/knight(1).png")
pygame.display.set_icon(icon)

# gracz
playerImg = pygame.image.load("assets/monster.png").convert_alpha()
playerX = 368 #calosc ekranu (800)/2 - szerokosc obrazka(64)/2
playerY = 400
speedX = 0
speedY = 0
playerSpeedChange = 7

# przeciwnik1
enemyImg = pygame.image.load("assets/zombie.png").convert_alpha()
enemyX = random.randint(1,735) #calosc ekranu (800)/2 - szerokosc obrazka(64)/2
enemyY = 0

enemyspeedX = random.choice([4,5,6,-4,-5,-6])
#enemyspeedY = 0

# przeciwnik2
enemyImg2 = pygame.image.load("assets/zombie.png").convert_alpha()
enemyX2 = random.randint(1,735) #calosc ekranu (800)/2 - szerokosc obrazka(64)/2
enemyY2 = 0
enemyspeedX2 = random.choice([4,5,6,-4,-5,-6])

# przeciwnik3
enemyImg3 = pygame.image.load("assets/zombie.png").convert_alpha()
enemyX3 = random.randint(1,735) #calosc ekranu (800)/2 - szerokosc obrazka(64)/2
enemyY3 = 0
enemyspeedX3 = random.choice([4,5,6,-4,-5,-6])


# strzal
spearImg = pygame.image.load("assets/spear.png").convert_alpha()
spearX = 0
spearY = 0
spearspeedY = 10
spearState = "ready" # ready / throw




def player(x,y):
    r=screen.blit(playerImg, (x, y))
    global dirtyRects
    dirtyRects.append(r)
    #screen.blit(playerImg, (x, y))

def enemy(x, y):
    r=screen.blit(enemyImg, (x, y))
    global dirtyRects
    dirtyRects.append(r)
    #screen.blit(enemyImg, (x, y))

def enemy2(x, y):
    r = screen.blit(enemyImg2, (x, y))
    global dirtyRects
    dirtyRects.append(r)
    # screen.blit(enemyImg, (x, y))

def enemy3(x, y):
    r = screen.blit(enemyImg3, (x, y))
    global dirtyRects
    dirtyRects.append(r)
    # screen.blit(enemyImg, (x, y))



def throw_spear(x,y):
    global spearState
    spearState = "throw"
    r=screen.blit(spearImg, (x+16,y+10))
    global dirtyRects
    dirtyRects.append(r)
    #screen.blit(spearImg, (x+16, y+10))

def isCollision(enemyX, enemyY, spearX, spearY):
    distance = math.sqrt((math.pow(enemyX-spearX,2)+math.pow(enemyY-spearY,2)))
    if distance < 25:
        return True
    else:
        return False

def isCollision2(enemyX2, enemyY2, spearX, spearY):
    distance2 = math.sqrt((math.pow(enemyX2-spearX,2)+math.pow(enemyY2-spearY,2)))
    if distance2 < 25:
        return True
    else:
        return False

def isCollision3(enemyX3, enemyY3, spearX, spearY):
    distance3 = math.sqrt((math.pow(enemyX3-spearX,2)+math.pow(enemyY3-spearY,2)))
    if distance3 < 25:
        return True
    else:
        return False

def genEnemy():
    global enemyX,enemyY,enemyspeedX
    enemyX = random.randint(1, 735)
    enemyY = 0
    enemyspeedX = random.choice([-6,-5,-4,4,5,6])

def genEnemy2():
    global enemyX2,enemyY2,enemyspeedX2
    enemyX2 = random.randint(1, 735)
    enemyY2 = 0
    enemyspeedX2 = random.choice([-6,-5,-4,4,5,6])

def genEnemy3():
    global enemyX3,enemyY3,enemyspeedX3
    enemyX3 = random.randint(1, 735)
    enemyY3 = 0
    enemyspeedX3 = random.choice([-6,-5,-4,4,5,6])


running = True

while running == True:
    screen.fill((20,150,101)) # Red Green Blue 0 ---> 255
    enemy(enemyX, enemyY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Udalo Ci sie trafic w bastiana", score, "razy")
            score=0
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if spearState == "ready":
                    spearY = playerY
                    spearX = playerX
                    throw_spear(spearX, spearY)
    #poprawiony ruch z klawiatury
    keys = pygame.key.get_pressed()
    speedX=0
    speedY=0
    if keys[pygame.K_LEFT]:
        speedX = -playerSpeedChange
    elif keys[pygame.K_RIGHT]:
        speedX = playerSpeedChange

    if keys[pygame.K_UP]:
        speedY = -playerSpeedChange
    elif keys[pygame.K_DOWN]:
        speedY = playerSpeedChange

    playerX += speedX
    playerY += speedY

    #ogranicz obszar gry gracz
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # ogranicz obszar gry przeciwnika1
    if enemyX <= 0:
        enemyspeedX *= -1
        enemyY += 32
    elif enemyX >= 736:
        enemyspeedX *= -1
        enemyY += 32
    enemyX += enemyspeedX

    # ogranicz obszar gry przeciwnika2
    if enemyX2 <= 0:
        enemyspeedX2 *= -1
        enemyY2 += 32
    elif enemyX2 >= 736:
        enemyspeedX2 *= -1
        enemyY2 += 32
    enemyX2 += enemyspeedX2

    # ogranicz obszar gry przeciwnika3
    if enemyX3 <= 0:
        enemyspeedX3 *= -1
        enemyY3 += 32
    elif enemyX3 >= 736:
        enemyspeedX3 *= -1
        enemyY3 += 32
    enemyX3 += enemyspeedX3

    if spearY <= -16:
        spearY = -50
        spearState = "ready"



    #strzal
    if spearState == "throw":
        throw_spear(spearX, spearY)
        spearY -= spearspeedY

    # Koniec gry
    distanceEnemy = math.sqrt((math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2)))
    distanceEnemy2 = math.sqrt((math.pow(enemyX2 - playerX, 2) + math.pow(enemyY2 - playerY, 2)))
    distanceEnemy3 = math.sqrt((math.pow(enemyX3 - playerX, 2) + math.pow(enemyY3 - playerY, 2)))

    if distanceEnemy < 50 or enemyY > 528:
        running = False
        #pygame.quit()
        print("Przegrales !")
        print("Udalo Ci sie trafic w bastiana", score, "razy!")
    elif distanceEnemy2 < 50 or enemyY2 > 528:
        running = False
        #pygame.quit()
        print("Przegrales !")
        print("Udalo Ci sie trafic w bastiana", score, "razy!")
    elif distanceEnemy3 < 50 or enemyY3 > 528:
        running = False
        #pygame.quit()
        print("Przegrales !")
        print("Udalo Ci sie trafic w bastiana", score, "razy!")

    # kolizja?
    collision = isCollision(enemyX, enemyY, spearX, spearY)
    collision2 = isCollision2(enemyX2, enemyY2, spearX, spearY)
    collision3 = isCollision3(enemyX3, enemyY3, spearX, spearY)
    if collision and spearState == "throw":
        spearState = "ready"
        spearY = -50
        score += 1
        genEnemy()
    elif collision2 and spearState == "throw":
        spearState = "ready"
        spearY = -50
        score += 1
        genEnemy2()
    elif collision3 and spearState == "throw":
        spearState = "ready"
        spearY = -50
        score += 1
        genEnemy3()


    #enemy(enemyX, enemyY)
    if score >= 5:
        enemy2(enemyX2, enemyY2)
        if score >=10:
            enemy3(enemyX3, enemyY3)
    player(playerX, playerY)

    pygame.display.update()
    clock.tick(60)

