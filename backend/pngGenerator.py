'''
Andrew Carlson (@andrewc272)
2D Graphics
11.26.24

When this script is finished it should:
    Input:  Any 6 png images
            Demensions of a box
    Output: 2 png images
                - the cover of the box
                - the respective backside with instructions on folding
'''

from PIL import Image


front = Image.open("Images/front.png")
back = Image.open("Images/back.png")
right = Image.open("Images/right.png")
left = Image.open("Images/left.png")
up = Image.open("Images/up.png")
down = Image.open("Images/down.png")

height = -1
width = -1
depth = -1


def getDimensions():
    pass


def main():
    getDimensions()
    makeCanvas()
    fillCanvas()
    showCanvas()

if __name__ == '__main__':
    main()
