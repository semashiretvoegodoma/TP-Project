import time
import pygame

mouse_down = False
mouse_just_got_down = False
delta_time = 0.0
last_frame_time = time.time()
sounds = dict()
screen = None

def createScreen(width, height):
    pygame.init()
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Arkanoid3000")
    pygame.font.init()
    # image = pygame.image.load(path)
    # pygame.display.set_icon(image)


def drawRect(rectColor, rectXYWH):
    global screen
    pygame.draw.rect(screen, rectColor, rectXYWH)


def drawText(text, text_color, font_size, text_type, x, y):
    global screen
    font = pygame.font.SysFont(text_type, font_size)
    img = font.render(text, True, text_color)
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
    global mouse_just_got_down
    mouse_just_got_down = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running[0] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_just_got_down = True
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_just_got_down = False
            mouse_down = False

    pygame.display.update()


def isMousePressed():
    return mouse_down


def mouse_pos():
    return pygame.mouse.get_pos()


def add_sound(name: str):
    if name not in sounds.keys():
        try:
            sounds[name] = pygame.mixer.Sound("Sounds/" + name + ".wav")
        except FileNotFoundError:
            print("ERROR: can't find sound " + name + ".wav in Sounds folder!")


def play_sound(name: str):
    if name in sounds.keys():
        sounds[name].play()


def quit():
    pygame.quit()
