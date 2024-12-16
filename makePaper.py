from backend import box as box
from backend import imageEngine
from PIL import Image

def main():
    # make a box
    boxDimensions = (6500, 3500, 1062)
    madeBox = box.Box(boxDimensions)

    # set images
    frontImage = Image.open("Images/front.png")
    backImage = Image.open("Images/back.png")
    leftImage = Image.open("Images/left.png")
    rightImage = Image.open("Images/right.png")
    upImage = Image.open("Images/up.png")
    downImage = Image.open("Images/down.png")

    # draw an image on each side of the box
    frontImage = imageEngine.drawCanvas(madeBox.front, frontImage)
    madeBox.front.setImage(frontImage)

    backImage = imageEngine.drawCanvas(madeBox.back, backImage)
    madeBox.back.setImage(backImage)

    leftImage = imageEngine.drawCanvas(madeBox.left, leftImage)
    madeBox.left.setImage(leftImage)

    rightImage = imageEngine.drawCanvas(madeBox.right, rightImage)
    madeBox.right.setImage(rightImage)

    upImage = imageEngine.drawCanvas(madeBox.up, upImage)
    madeBox.up.setImage(upImage)

    downImage = imageEngine.drawCanvas(madeBox.down, downImage)
    madeBox.down.setImage(downImage)
    
    # save box for debugging
    print(madeBox)

    # make canvas for wrapping paper 
    canvasWidth = madeBox.width*2 + madeBox.depth*2
    canvasHeight = madeBox.height + madeBox.depth*2
    paper = Image.new('RGB', (canvasWidth, canvasHeight))
    paperData = paper.load()

    # UN
    canvas_x, canvas_y = (0, 0)
    image = madeBox.up.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # UW
    canvas_x, canvas_y = (madeBox.width, 0)
    image = madeBox.up.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # US
    canvas_x, canvas_y = (madeBox.width + madeBox.depth, 0)
    image = madeBox.up.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # UE
    canvas_x, canvas_y = (madeBox.width*2 + madeBox.depth, 0)
    image = madeBox.up.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # Back
    canvas_x, canvas_y = (0, madeBox.depth)
    image = madeBox.back.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # Left
    canvas_x, canvas_y = (madeBox.width, madeBox.depth)
    image = madeBox.left.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # front
    canvas_x, canvas_y = (madeBox.width + madeBox.depth, madeBox.depth)
    image = madeBox.front.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # Right
    canvas_x, canvas_y = (madeBox.width*2 + madeBox.depth, madeBox.depth)
    image = madeBox.right.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # DS
    canvas_x, canvas_y = (0, madeBox.depth + madeBox.height)
    image = madeBox.down.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # UW
    canvas_x, canvas_y = (madeBox.width, madeBox.depth + madeBox.height)
    image = madeBox.down.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # DN
    canvas_x, canvas_y = (madeBox.width + madeBox.depth, madeBox.depth + madeBox.height)
    image = madeBox.down.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    # DE
    canvas_x, canvas_y = (madeBox.width*2 + madeBox.depth, madeBox.depth + madeBox.height)
    image = madeBox.down.getCanvas()
    image = image.convert('RGB')
    imageData = image.load()
    for image_y in range(image.height):
        for image_x in range(image.width):
            x = canvas_x+image_x
            y = canvas_y+image_y
            if y < canvasHeight and x < canvasWidth:
                paperData[x,y] = imageData[image_x, image_y]

    paper.save("wrappingPaper.png")




if __name__ == '__main__':
    main()
