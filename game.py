# Starts up the game
from direct.showbase.ShowBase import ShowBase
from mapmanager import mapmanager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = mapmanager() #create a map
        self.land.loadLand("land2.txt")
        self.hero = Hero(pos=(x//2, y//2, 2), land=self.land)
        base.camLens.setFov(90)

game = Game()
game.run()