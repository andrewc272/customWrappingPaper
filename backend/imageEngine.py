from PIL import Image

def makeCanvas(canvasDimensions):
    height, width = canvasDimensions
    blankCanvas = Image.new('RGB', (width, height), 'white')
    return blankCanvas

def drawCanvas(side, Image):
    height, width = (side.height, side.width)
    return makeCanvas((height, width))

