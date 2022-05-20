import SolidBrickRenderer
import BreakingBrickRenderer
import BrokenBrickRenderer


class BrickRenderer:
    def __init__(self, brick):
        self.brick = brick
        self.SOLID = 0
        self.BREAKING = 1
        self.BROKEN = 2
        self.solidRenderer = SolidBrickRenderer.SolidBrickRenderer(self)
        self.breakingRenderer = BreakingBrickRenderer.BreakingBrickRenderer(self)
        self.brokenRenderer = BrokenBrickRenderer.BrokenBrickRenderer()
        self.state = self.SOLID
        self.renderers = {
            self.SOLID: self.solidRenderer,
            self.BREAKING: self.breakingRenderer,
            self.BROKEN: self.brokenRenderer
        }

    def to_broken(self):
        self.state = self.BROKEN

    def to_breaking(self):
        self.state = self.BREAKING

    def draw(self):
        self.renderers[self.state].draw()

    def update(self):
        self.renderers[self.state].update()
