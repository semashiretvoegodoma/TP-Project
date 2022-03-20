import wrapper
from currentScene import CurrentScene

#отвечает за экран
screen_width = 1300
screen_height = 700
wrapper.createScreen((screen_width, screen_height))

currentScene = CurrentScene()

running = True

while running:

    currentScene.update()
    currentScene.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
