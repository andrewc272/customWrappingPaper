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
images = []

canvas_height = 0
canvas_width = 0
canvas = Image.new('RGB', (canvas_width, canvas_height), RGB_white)
canvas_grid = []

# box
box_dimensions = (-1, -1, -1) # height, width, depth

def main():
    getDimensions()
    makeCanvas()
    fillCanvas()
    showCanvas()

def getDimensions():
    for i in range(0,3):
        box_dimensions[i] = (float)input(f'What is dimension {i} in inches: ') * 1000
    box_dimensions.sort(reverse=True)

def makeCanvas():
    box_height, box_width, box_depth = box_dimensions
    canvas_height = ( box_depth * 1.5 ) + box_height
    canvas_width = ( 2 * box_width ) + ( 2 * box_depth )
    canvas = Image.new('RGB', (canvas_width, canvas_height), RGB_white)
    canvas_grid = ([box_width, box_width+box_depth, 2*box_width+box_depth, canvas_width],
                   [box_depth*0.75, box_depth*0.75+box_height, canvas_height])


def fillCanvas():
    makeImages()
    drawImages()


def makeImages():
    horizontal_lines, vertical_lines = canvas_grid
    image_number = 0
    for hoizontal_line in horizontal_lines:
        for vertical_line in vertical_lines:
             image = whichImage(image_number)
             image = stretchImage(image, (horizontal_line, vertical_line))


def whichImage(image_num):
    if image_num < 4: return image_up
    elif image_num == 4: return image_front
    elif image_num == 5: return image_left
    elif image_num == 6: return image_back
    elif image_num == 7: return image_right
    elif image_num >= 8: return image_down

def stretchImage(og_img, stretchPos):
    width, height = stretchPos
    
    '''
There are a few different ways of doing this and I want to find the one that will be simplest and fastest
    - you can make 13 different images and then draw them on to the canvas in order
        - up 1, up 2, up 3, up 4
        - front
        - left
        - back
        - right
        - down 1, down 2, down 3, down 4
        - grid

    - Another option is to make the grid and then fill in each square of the grid given an image
        - this would have to in real time map the image to the squares rather than drawing 
            a pre-existing image.
    '''



if __name__ == '__main__':
    main()
