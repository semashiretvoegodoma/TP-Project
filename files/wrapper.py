import pygame

# это отвечает за инициализацию pygame
pygame.init()

#отвечает за экран
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

brick_color = (50, 50, 50)
brick_xy_wh = (100, 100, 30, 10)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


def background_screen(R, G, B):
    background = (R, G, B)
    screen.fill(background)


def brick(screen, brick_color, brick_xy_wh):
    def draw_rectangle():
        pygame.draw.rect(screen, brick_color, brick_xy_wh)

brick(screen, brick_color, brick_xy_wh)

T = True
while T:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            T = False

    pygame.display.update()

pygame.quit()

def slider():
    ///...

def ball():
    ...
