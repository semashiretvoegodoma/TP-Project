import wrapper
from currentScene import CurrentScene


def run():
    screen_width = 1300
    screen_height = 700
    wrapper.createScreen(screen_width, screen_height)

    currentScene = CurrentScene()

    running = True

    while running:

        currentScene.update()
        wrapper.colorScreen(255, 255, 255)
        currentScene.draw()

        temp = [running]
        wrapper.cycle(temp)
        running = temp[0]

    wrapper.quit()
