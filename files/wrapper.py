import time
import pygame

mouse_down = False
delta_time = 0.0
last_frame_time = time.time()

def createScreen(width, height):
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Arkanoid3000")
    pygame.font.init()
    # image = pygame.image.load(path)
    # pygame.display.set_icon(image)


def drawRect(rectColor, rectXYWH):
    global screen
    pygame.draw.rect(screen, rectColor, rectXYWH)


def drawText(text, textColor, sizeFont, typeText, x, y):
    global screen
    font = pygame.font.SysFont(typeText, sizeFont)
    img = font.render(text, True, textColor)
    screen.blit(img, (x, y))


def colorScreen(R, G, B):
    global screen
    background = (R, G, B)
    screen.fill(background)


def drawCircle(colorCircle, pos, Rad):
    global screen
    pygame.draw.circle(screen, colorCircle, pos, Rad)


def collisionRect(X1, Y1, W1, H1, X2, Y2, W2, H2):
    rect1 = pygame.Rect(X1, Y1, W1, H1)
    rect2 = pygame.Rect(X2, Y2, W2, H2)
    return rect1.colliderect(rect2)


def rectContains(X1, Y1, W1, H1, X2, Y2, W2, H2):
    rect1 = pygame.Rect(X1, Y1, W1, H1)
    rect2 = pygame.Rect(X2, Y2, W2, H2)
    return rect1.contains(rect2)

def arrowLeft():
    key = pygame.key.get_pressed()
    return key[pygame.K_LEFT]


def arrowRight():
    key = pygame.key.get_pressed()
    return key[pygame.K_RIGHT]


def mouseInButton(X1, Y1, W1, H1):
    rect = pygame.Rect(X1, Y1, W1, H1)
    point = pygame.mouse.get_pos()
    return rect.collidepoint(point[0], point[1])


def dotInRect(X1, Y1, W1, H1, dotx, doty):
    if X1 + W1 <= dotx <= X1 and Y1 + H1 <= doty <= Y1:
        return 1
    return 0


def cycle(running):
    global delta_time
    global last_frame_time
    delta_time = time.time() - last_frame_time
    last_frame_time = time.time()
    global mouse_down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running[0] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

    pygame.display.update()


def isMousePressed():
    return mouse_down


def quit():
    pygame.quit()
