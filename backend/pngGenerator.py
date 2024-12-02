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
from backend import canvas

# RGB colors
RGB_white = (255, 255, 255)

# images
image_front = Image.open("Images/front.png")
image_back = Image.open("Images/back.png")
image_right = Image.open("Images/right.png")
image_left = Image.open("Images/left.png")
image_up = Image.open("Images/up.png")
image_down = Image.open("Images/down.png")

canvas = Image.new('RGB', (0,0), RGB_white)
canvas_grid = []

# box
box_dimensions = (-1, -1, -1) # height, width, depth

def main():
    getDimensions()
    makeCanvas()
    fillCanvas(0, 0)
    showCanvas()

def getDimensions():
    for i in range(0,3):
        box_dimensions[i] = (float)input(f'What is dimension i: ')
    box_dimensions.sort(reverse=True)

def makeCanvas():
    box_height, box_width, box_depth = box_dimensions
    canvas_height = ( box_depth * 1.5 ) + box_height
    canvas_width = ( 2 * box_width ) + ( 2 * box_depth )
    canvas = Image.new('RGB', (canvas_width, canvas_height), RGB_white)


def fillCanvas(x, y):
    if isGrid(x, y):

def isGrid(x, y):
    box_height, box_width, box_depth = box_dimensions



if __name__ == '__main__':
    main()
