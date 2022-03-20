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


def drawText(text, textColor, sizeFont, typeText, x, y):
    global screen
    font = pygame.font.SysFont(typeText, sizeFont)
    img = font.render(text, True, textColor)
    screen.blit(img, (x, y))


def colorScreen(R, G, B):
    global screen
    background = (R, G, B)
    screen.fill(background)


def drawCircle(colorCircle, colorXY, Rad):
    global screen
    pygame.draw.circle(screen, colorCircle, colorXY, Rad)


def collisionRect(X1, Y1, W1, H1, X2, Y2, W2, H2):
    rect1 = pygame.Rect(X1, Y1, W1, H1)
    rect2 = pygame.Rect(X2, Y2, W2, H2)
    return rect1.colliderect(rect2)


def cycle(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


def quit():
    pygame.quit()
