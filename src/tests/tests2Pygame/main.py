
import pygame

WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 1280, 720
### Créé la fenêtre
WIN = pygame.display.set_mode(WIN_SIZE)

# Donne un nom à la fenêtre
pygame.display.set_caption("un jeu")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

FPS = 60

run = True

def updateWindow(event):
    if event.type == pygame.QUIT:
        global run
        run = False

def drawWindow(window):
    window.fill(BLUE)



def update():
    for event in pygame.event.get():
        updateWindow(event)
        pass



def draw():
    drawWindow(WIN)
    #pygame.display.flip()
    pygame.display.update()


def main():
    global run
    clock = pygame.time.Clock()

    while run:
        update()
        draw()

    clock.tick(FPS)

if __name__ == "__main__":
    main()
