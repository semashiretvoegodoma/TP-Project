import pygame
from time import sleep

pygame.init()


size = (600,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tormoz")


font = pygame.font.SysFont('arial',32)
RED = (255,0,0)
text = "Welcome"

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def animate(text, delay):
    for i in text:
        draw_text(i, font, text_col, 0, 0)
        sleep(delay)

animate("Welcome to my house", 0.01)

while True:
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            quit()
