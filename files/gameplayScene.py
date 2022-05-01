import scene
from GameplayPlayState import GameplayPlayState
from GameplayPauseState import GameplayPauseState
from GameplayWinState import GameplayWinState
from GameplayLoseState import GameplayLoseState
import json


class GameplayScene(scene.Scene):
    STATE_PLAY = 0
    STATE_PAUSE = 1
    STATE_WIN = 2
    STATE_LOSE = 3

    def __init__(self, current_scene):
        self.current_scene = current_scene
        self.state = GameplayScene.STATE_PLAY
        self.play = GameplayPlayState(self)
        self.pause = GameplayPauseState(self)
        self.win = GameplayWinState(self)
        self.lose = GameplayLoseState(self)
        self.gameplaySceneState = {
            self.STATE_PLAY: self.play,
            self.STATE_PAUSE: self.pause,
            self.STATE_WIN: self.win,
            self.STATE_LOSE: self.lose
        }
        self.current_level = -1
        f = open("Levels/levels_info")
        dec = json.JSONDecoder()
        self.levels = int(dec.decode(s=f.read())["levels_amount"])
        f.close()

    def startLevel(self, level):
        self.state = GameplayScene.STATE_PLAY
        self.play.loadLevel(level)
        self.play.buildLevel()
        self.current_level = level

    def next_level(self):
        if self.current_level + 1 <= self.levels:
            self.startLevel(self.current_level + 1)
        else:
            self.to_final_win()

    def to_win(self):
        self.state = self.STATE_WIN

    def to_final_win(self):
        self.current_scene.state = self.current_scene.SCENE_FINALWIN

    def to_lose(self):
        self.state = self.STATE_LOSE

    def retry(self):
        self.state = self.STATE_PLAY
        self.play.buildLevel()

    def to_pause(self):
        if self.state == self.STATE_PLAY:
            self.state = self.STATE_PAUSE

    def to_levels(self):
        self.current_scene.state = self.current_scene.SCENE_LEVELS

    def resume(self):
        if self.state == self.STATE_PAUSE:
            self.state = self.STATE_PLAY

    def draw(self):
        self.gameplaySceneState[self.state].draw()

    def update(self):
        self.gameplaySceneState[self.state].update()
