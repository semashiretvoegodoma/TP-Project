import pygame


def createScreen(width, height):
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Arkanoid3000")
    # image = pygame.image.load(path)
    # pygame.display.set_icon(image)


def drawRect(rectColor, rectXYWH):
    global screen
    pygame.draw.rect(screen, rectColor, rectXYWH)
    pygame.display.update()  # вот это под сомнениями


def drawText(text, font, textColor, x, y):
    global screen
    img = font.render(text, True, textColor)
    screen.blit(img, (x, y))


def colorScreen(R, G, B):
    global screen
    background = (R, G, B)
    screen.fill(background)


def drawCircle(colorCircle, colorXY, Rad):
    global screen
    pygame.draw.circle(screen, colorCircle, colorXY, Rad)
