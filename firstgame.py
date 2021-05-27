import pygame
import random
import math
import time

#rozpocznij program
pygame.init()

#dodaj zegar gry
clock = pygame.time.Clock()

#stworz ekran gry
screen = pygame.display.set_mode((1000, 600))

#nazwa gry
pygame.display.set_caption("eliminate the crown")

#ikona gry
icon = pygame.image.load("obrazki/ikona.png")
pygame.display.set_icon(icon)

#gracz
playerimg = pygame.image.load("obrazki/virusman.png")
playerX = 460
playerY = 500
speedX = 0
speedY = 0

#przeciwnik
enemyimg = pygame.image.load("obrazki/mob.png")
enemyX = random.randint(0, 936)
enemyY = random.randint(50, 100)
enemyspeedX = random.choice([1, 2, -1, -2])

#kolizja ogień
fireimg = pygame.image.load("obrazki/fire.xcf")
fireX = 600
fireY = 500

#amunicja
ammoimg = pygame.image.load("obrazki/termometer.png")
ammoX = 0
ammoY = 0
ammospeedY = 7
ammoState = "ready" # ready / throw

score = 0

def fire(x, y):
    screen.blit(fireimg, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def throw_ammo(x, y):
    global ammoState
    ammoState = "throw"
    screen.blit(ammoimg, (x + 16, y + 10))



def is_collision(enemyX, enemyY, ammoX, ammoY):
    distance = math.sqrt((math.pow(enemyX-ammoX,2) + math.pow(enemyY-ammoY,2)))
    if distance < 25:
        return True
    else:
        return False


def gen_enemy():
    global enemyX, enemyY, enemyspeedX
    enemyX = random.randint(1, 935)
    enemyY = 0
    enemyspeedX = random.choice([1, 2, -1, -2])

running = True

while running:

    #tło ekranu gry
    screen.fill((255,200,163))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #poprawiony ruch z klawiatury
    keys = pygame.key.get_pressed()
    speedX = 0
    speedY = 0

    if keys[pygame.K_LEFT]:
        speedX = -3
    elif keys[pygame.K_RIGHT]:
        speedX = 3

    if keys[pygame.K_UP]:
        speedY = -3
    elif keys[pygame.K_DOWN]:
        speedY = 3

    if keys[pygame.K_SPACE]:
        ammoY = playerY
        ammoX = playerX
        throw_ammo(ammoX, ammoY)

    playerX += speedX
    playerY += speedY

    enemyX += enemyspeedX

    #ogranicz obszar gry
#player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 936:
        playerX = 936

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
         playerY = 536
#enemy
    if enemyX <= 0:
        enemyspeedX *= -1
    elif enemyX >= 936:
        enemyspeedX *= -1

    player(playerX, playerY)
    enemy(enemyX, enemyY)


#strzal

    if ammoY <= -32:
        ammoY = -50
        ammoState = "ready"

    if ammoState == "throw":
        throw_ammo(ammoX, ammoY)
        ammoY -= ammospeedY



#kolizja ?
    collision = is_collision(enemyX, enemyY, ammoX, ammoY)

    if collision:
        fire(enemyX, enemyY)
        ammoState = "ready"
        enemyY = -50
        gen_enemy()
        score += 1


    pygame.display.update()
    clock.tick(60)
