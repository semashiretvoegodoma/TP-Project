import pygame
import current_scene
aboba
#отвечает за экран
screen_width = 1300
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

#отвечает за название экрана
pygame.display.set_caption("Arkanoid3000")

#отвечает за иконку, она находится слева сверху
image = pygame.image.load("Arkanoid.png")
pygame.display.set_icon(image)

# цвет текста
text_color = (0, 0, 0)

...


# это отвечает за выход из игры нажатием на крестик
# также за обновление экрана
T = True
while T:

    current_scene()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            T = False

    pygame.display.update()

pygame.quit()
