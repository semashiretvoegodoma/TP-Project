import os

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
        self.current_level = ""

    def startLevel(self, level):
        self.state = GameplayScene.STATE_PLAY
        self.play.loadLevel(level)
        self.play.buildLevel()
        self.current_level = level

    def next_level(self):
        files = os.listdir("Levels")
        i = files.index(self.current_level)
        next_lvl = files[i+1]
        if i+1 < len(files):
            self.startLevel(next_lvl)
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
