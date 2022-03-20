import pygame


def createScreen(width, height, path):
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Arkanoid3000")
    image = pygame.image.load(path)
    pygame.display.set_icon(image)


def drawRect(rectColor, rectXYWH):
    global screen
    pygame.draw.rect(screen, rectColor, rectXYWH)
    pygame.display.update()  # вот это под сомнениями


def drawText(text, textColor, sizeColor, typeText, x, y):
    global screen
    font = pygame.font.SysFont(typeText, sizeColor)
    img = font.render(text, True, textColor)
    screen.blit(img, (x, y))


def colorScreen(R, G, B):
    global screen
    background = (R, G, B)
    screen.fill(background)


def drawCircle(colorCircle, colorXY, Rad):
    global screen
    pygame.draw.circle(screen, colorCircle, colorXY, Rad)


def moveSlider(slider, speedSlider, width):
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and slider.left > 0:
        slider.left -= speedSlider
    if key[pygame.K_RIGHT] and slider.right < width:
        slider.right += speedSlider

def cycle(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

def quit():
    pygame.quit()

