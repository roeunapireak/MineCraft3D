
key_switch_camera = 'space' # the camera is bound to the hero or not
key_switch_mode = 'z' # can get past obstacles or not


key_forward = 'w' # step forward (the direction the camera is pointing in)
key_back = 's' # turn back
key_left = 'a' # turn left (sideways from the camera)
key_right = 'd' # step right

key_up = 'e' # step up
key_down = 'q' # step down


key_turn_left = 'n' 
key_turn_right = 'm' 




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
        base.accept(key_switch_camera, self.changeView)

        base.accept(key_left, self.turn_left)
        base.accept(key_left + '-repeat', self.turn_left)

        base.accept(key_right, self.turn_right)
        base.accept(key_right + '-repeat', self.turn_right)

        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)

        base.accept(key_back, self.back)
        base.accept(key_back + '-repeat', self.back)

        base.accept(key_turn_left, self.left)
        base.accept(key_turn_left + '-repeat', self.left)

        base.accept(key_turn_right, self.right)
        base.accept(key_turn_right + '-repeat', self.right)

        base.accept(key_up, self.up)
        base.accept(key_up + '-repeat', self.up)

        base.accept(key_down, self.down)
        base.accept(key_down + '-repeat', self.down)

        base.accept(key_switch_mode, self.changeMode)



    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)


    def forward(self):
        angle =(self.hero.getH()) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)


    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    

    def look_at(self, angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy

        return x_to, y_to, z_from
    
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def check_dir(self,angle):
        if angle >= 0 and angle <= 20:
           return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)
        

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)


    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True