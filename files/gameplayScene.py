import scene
from GameplayPlayState import GameplayPlayState
from GameplayPauseState import GameplayPauseState
from GameplayWinState import GameplayWinState
from GameplayLoseState import GameplayLoseState


class GameplayScene(scene.Scene):
    STATE_PLAY = 0
    STATE_PAUSE = 1
    STATE_WIN = 2
    STATE_LOSE = 3

    def __init__(self):
        self.state = GameplayScene.STATE_PLAY
        self.play = GameplayPlayState()
        self.pause = GameplayPauseState()
        self.win = GameplayWinState()
        self.lose = GameplayPauseState()
        self.gameplaySceneState = {
            self.STATE_PLAY: self.play,
            self.STATE_PAUSE: self.pause,
            self.STATE_WIN: self.win,
            self.STATE_LOSE: self.lose
        }

    def startLevel(self, levelNum):
        self.state = GameplayScene.STATE_PLAY
        self.play.buildLevel()

    def draw(self):
        self.gameplaySceneState[self.state].draw()

    def update(self):
        self.gameplaySceneState[self.state].update()
