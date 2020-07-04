import pygame
import random
import math




#initialize the game
pygame.init()
#creating the scree
screen = pygame.display.set_mode((800, 600))
#background
background = pygame.image.load('stars_milky_way_space_116893_800x600.jpg')
#caption and icon
pygame.display.set_caption("Space Invadors by bhawuk")
#Player
Playerimg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0
#enemy
Enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    Enemy_img.append(pygame.image.load('002-space-invaders.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
#bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#score
score_value=0
font= pygame.font.Font('freesansbold.ttf',32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
textX=10
textY=10
def show_score(x,y):
    score=font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(280,250))

def player(x, y):
    screen.blit(Playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(Enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def is_collition(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
#main loop
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    for i in range(no_of_enemies):
        # Game Over
        if enemyY[i] > 430:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX[i] = -4
            enemyY[i] += enemyY_change[i]
        collision = is_collition(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    collision = is_collition(enemyX[i], enemyY[i], bulletX, bulletY)

    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()

