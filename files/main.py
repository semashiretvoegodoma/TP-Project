import pygame
from currentScene import CurrentScene


currentScene = CurrentScene()

# это отвечает за выход из игры нажатием на крестик
# также за обновление экрана
running = True
while running:
    currentScene.update()
    currentScene.draw()

    cycle(running)
quit()
