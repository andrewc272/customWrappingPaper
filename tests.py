from PIL import Image
from backend import side
from backend import imageEngine

testImage = Image.open("Images/test.jpg")

def TEST_side():
    squareSide = side.Side((1000, 1000))
    squareSide.getCanvas().show()
    
    tallSide = side.Side((2000, 500))
    tallSide.getCanvas().show()
    
    fatSide = side.Side((500, 2000))
    fatSide.getCanvas().show()


def TEST_drawCanvas():
    squareSide = side.Side((1000, 1000))
    tallSide = side.Side((2000, 500))
    fatSide = side.Side((500, 2000))

    testImage.show()

    # test just getting the same image
    imageSide = side.Side((testImage.height, testImage.width))
    sameImage = imageEngine.drawCanvas(imageSide, testImage)
    sameImage.show()

    squareImage = imageEngine.drawCanvas(squareSide, testImage)
    squareImage.show()

    tallImage = imageEngine.drawCanvas(tallSide, testImage)
    tallImage.show()

    fatImage = imageEngine.drawCanvas(fatSide, testImage)
    fatImage.show()

def runTests():
    #TEST_side()
    TEST_drawCanvas()


if __name__ == '__main__':
    runTests()
