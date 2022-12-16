
import sys, pygame

size = width, height = 320, 480
speed = [1, 1]
black = 0, 0, 0

# 
screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    # noir au fond
    screen.fill(black)

    # affiche la balle
    screen.blit(ball, ballrect)

    # met a jour l'écran
    pygame.display.flip()



