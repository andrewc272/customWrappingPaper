from PIL import Image

def makeCanvas(canvasDimensions):
    height, width = canvasDimensions
    blankCanvas = Image.new('RGB', (width, height), 'white')
    return blankCanvas

def drawCanvas(side, image):
    
    canvas =  Image.new('RGB', (side.width, side.height))
    canvasData = canvas.load()
    image = image.convert('RGB')
    imageData = image.load()

    xAmount = image.width/canvas.width
    yAmount = image.height/canvas.height

    for y in range(canvas.height):
        for x in range(canvas.width):
            canvasData[x,y]  = imageData[int(x*xAmount), int(y*yAmount)]

    return canvas

def stretch(img):
    img = img.resize((img.width*2, img.height))
    img.show()

