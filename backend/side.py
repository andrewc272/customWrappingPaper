from backend import imageEngine

class Side:
    def __init__(self, sideDimensions):
        self.height, self.width = sideDimensions
        self.canvas = imageEngine.makeCanvas(sideDimensions)

    def setImage(self, Image):
        self.canvas = imageEngine.drawCanvas(self, Image)

    def getCanvas(self):
        return self.canvas

