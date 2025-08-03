''' variables '''





class Hero():

    def __init__(self, pos, land):
        self.land = land
        self.mode = True # pass through everything mode
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)

        self.hero.reparentTo(render)


        self.cameraBind()

        self.accept_events()


    def cameraBind(self):
        
        base.disableMouse()

        base.camera.setH(180) # rotate the camera 180 degrees
        
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)

        self.cameraOn = True # to show if the camera is bound or not


    def cameraUp(self):

        pos = self.hero.getPos()
        
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3) 

        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    


    def accept_events(self):
        base.accept('space', self.changeView)


    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
