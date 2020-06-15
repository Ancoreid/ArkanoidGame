import pygame
import random
import os

# Inicialize the pygame
pygame.init()

# Get the center position of the windows video
(width, height) = (900, 600)
pos_x = width / 2 - width / 2
pos_y = height - height
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

# Title and Icon
pygame.display.set_caption("Pong Game")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

# Player
playerX = 387
playerY = 550
playerSpeed = 0
player = pygame.Rect(playerX, playerY, 125, 18)

# Ball
direction = random.choice((1,-1))
ballSpeedX = 5 * direction
ballSpeedY = 5 * direction
ball = pygame.Rect(400, 380, 25, 25)

# COLOR
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
DARK_GREEN = (0,150,0)
BLUE = (0,0,255)
DARK_YELLOW = (255,204,0)
colors = [RED, DARK_GREEN, BLUE, DARK_YELLOW]

# Blocks
blockList = []
colorList = []

def createBlocks():
    y = 0
    count = 0
    for i in range(70):
        color = random.choice(colors)
        block = pygame.Rect(85*count + count*4, 30*y + y*4, 85, 30)
        blockList.append(block)
        colorList.append(color)
        count += 1
        if count == 10:
            y += 1
            count = 0

createBlocks()

def blockDesign():
    for i in range(70):
        pygame.draw.rect(screen, colorList[i], blockList[i])

# Loss or Win
lossImg = pygame.image.load('loss.png')
winImg = pygame.image.load('victory.png')

def loss():
    screen.blit(lossImg, (322, 172))

# Clear the screen
def clear():
    for i in range(70):
        blockList[i].x = 1000
    player.x = 1000
    ball.x = 1000

# Game Loop
running = True
while running:
    # Background color - RGB
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player and Ball Collision
    if ball.colliderect(player):
        ballSpeedY *= -1

    #Player Movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
             player.x -= 7
        elif event.key == pygame.K_RIGHT:
            player.x += 7
    # Player border limits
    if player.x <= 0:
        player.x = 0
    elif player.x >= 775:
        player.x = 775

    # Ball Movement
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Ball border limits
    if ball.top <= 0:
        ballSpeedY *= -1
    if ball.left <= 0 or ball.right >= width:
        ballSpeedX *= -1
    if ball.bottom >= height:
        clear()
        screen.fill((255, 255, 255))
        loss()

    # Remove a broken block
    for i in range(len(blockList)):
        if ball.colliderect(blockList[i]):
            blockList[i].x = 1000
            ballSpeedY *= -1
            break

    # Function Activation
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.ellipse(screen, WHITE, ball)
    blockDesign()
    pygame.display.update()

    pygame.time.Clock().tick(50)
