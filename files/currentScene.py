from menuScene import MenuScene
from levelsScene import LevelsScene
from gameplayScene import GameplayScene
from finalScene import FinalWinScene
from scene import Scene


class CurrentScene(Scene):
    SCENE_MENU = 0
    SCENE_LEVELS = 1
    SCENE_GAMEPLAY = 2
    SCENE_FINALWIN = 3

    def __init__(self):
        self.state = CurrentScene.SCENE_MENU
        self.menuScene = MenuScene(self)
        self.gameplayScene = GameplayScene()
        self.levelsScene = LevelsScene(self, self.gameplayScene)
        self.finalWinScene = FinalWinScene()
        self.scene = {
            CurrentScene.SCENE_MENU: self.menuScene,
            CurrentScene.SCENE_LEVELS: self.levelsScene,
            CurrentScene.SCENE_GAMEPLAY: self.gameplayScene,
            CurrentScene.SCENE_FINALWIN: self.finalWinScene
        }

    def draw(self):
        self.scene[self.state].draw()

    def update(self):
        self.scene[self.state].update()
