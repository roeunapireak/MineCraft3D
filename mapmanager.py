# Loads maps
from direct.showbase.ShowBase import ShowBase
import pickle
class mapmanager():
    def __init__(self, map_model='block.egg', map_texture='block.png'):
        self.model = map_model

        self.texture = map_texture

        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ]

        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode ( "Land" )

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))

        self.block.setPos(position)

        # we choose one color from the list
        self.color = self.getColor( int(position[2]) )

        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
    
    def clear(self):
        self.land.removeNode()
        self.startNew()
    
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0 
            for line in file:
                x = 0 
                line = line.split(' ')
                for z in line:
                    for z_range in range(int(z) + 1):
                        block = self.addBlock( (x, y, z_range) )
                    x += 1
                y += 1

        return x,y

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    
    def findHighestEmpty(self, pos):
        x,y,z =pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z = z + 1
        return (x, y, z)

    def buildBlock(self, position):
        x, y, z = position
        new = self.findHighestEmpty(position)
        if new[2] <= z + 1:
            self.addBlock(new)
    
    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z - 1
        for block in self.findBlocks(pos):
            block.removeNode()

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def saveMap(self):
        """saves all blocks, including structures, to a binary file"""

        """returns a NodePath collection for all existing blocks on the world map"""
        blocks = self.land.getChildren()
        # open a binary file for recording
        with open('my_map.dat', 'wb') as fout:

            # save the number of blocks at the beginning of the file
            pickle.dump(len(blocks), fout)

            # go around all the blocks
            for block in blocks:
                # save the position
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)

    def loadMap(self):
        # delete all the blocks
        self.clear()

        # open a binary file for reading
        with open('my_map.dat', 'rb') as fin:
            
            # read the number of blocks
            length = pickle.load(fin)

            for i in range(length):
                # read the position
                pos = pickle.load(fin)

                # create a new block
                self.addBlock(pos)