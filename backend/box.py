from backend import side
from PIL import Image

class Box:
    def __init__(self, boxDimensions):
        self.height, self.width, self.depth = boxDimensions
        self.front = side.Side((self.height, self.width))
        self.back = side.Side((self.height, self.width))
        self.left = side.Side((self.height, self.depth))
        self.right = side.Side((self.height, self.depth))
        self.up = side.Side((self.depth, self.width))
        self.down = side.Side((self.depth, self.width))

    def __str__(self):
        self.front.getCanvas().save("BOX/front.png")
        self.back.getCanvas().save("BOX/back.png")
        self.left.getCanvas().save("BOX/left.png")
        self.right.getCanvas().save("BOX/right.png")
        self.up.getCanvas().save("BOX/up.png")
        self.down.getCanvas().save("BOX/down.png")
        return "Box Saved"
