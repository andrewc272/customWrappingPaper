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


# images
image_front = Image.open("Images/front.png")
image_back = Image.open("Images/back.png")
image_right = Image.open("Images/right.png")
    horizontal_lines, vertical_lines = canvas_grid
    image_number = 0
    for x in range(1, len(horizontal_lines)):
        topGridLine = horizontal_lines[x-1]
        bottomGridLine = horizontal_lines[x-1]
        height = bottomGridLine - topGridLine

        for y in range(1, len(vertical_lines)):
            leftGridLine = vertical_lines[y-1]
            rightGridLine = vertical_lines[y]
            width = rightGridLine - leftGridLine

            image = whichImage(image_number)
            image_number++

            image = stretchImage(image, (width, height))
image_left = Image.open("Images/left.png")
image_up = Image.open("Images/up.png")
image_down = Image.open("Images/down.png")
images = []

canvas_height = 0
canvas_width = 0
canvas = Image.new('RGB', (canvas_width, canvas_height))
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
    canvas = Image.new('RGB', (canvas_width, canvas_height))
    canvas_grid = ([0, box_width, box_width+box_depth, 2*box_width+box_depth, canvas_width],
                   [0, box_depth*0.75, box_depth*0.75+box_height, canvas_height])


def fillCanvas():
    makeImages()
    drawImages()

def makeImages():
    horizontal_lines, vertical_lines = canvas_grid
    for x in range(1, len(horizontal_lines)):
        height = horizontal_lines[x] - horizontal_lines[x-1]
        for y in range(1, len(vertical_lines)):
            width = vertical_lines[y] - vertocal_lines[y-1]
            image = whichImage(len(images))
            images.append(stretchImage(image, (width, height)))

def whichImage(image_num):
    if image_num < 4: return image_up
    elif image_num == 4: return image_front
    elif image_num == 5: return image_left
    elif image_num == 6: return image_back
    elif image_num == 7: return image_right
    elif image_num >= 8: return image_down

def stretchImage(og_img, stretchPos):
    og_data = og_img.load()
    width, height = stretchPos
    
    adj_img = Image.new('RGB', (width, height))
    adj_data = adj_img.load()

    horizontalStretch = adj_img.width / og_img.width
    verticalStretch = adj_img.height / og_img.width
    
    for y in range(adj_img.heigh):
        for x in range(adj_img.width):
            pixel = og_data[int(x/horizontalStretch), int(y/verticalStretch)]
            adj_data[x,y] = pixel

    return adj_image

def drawImages():
    horizontal_lines, vertical_lines = canvas_grid
    image_number = 0
    for x in range(1, len(horizontal_lines)):
        topGridLine = horizontal_lines[x-1]
        bottomGridLine = horizontal_lines[x-1]

        for y in range(1, len(vertical_lines)):
            leftGridLine = vertical_lines[y-1]
            rightGridLine = vertical_lines[y]

            
            image_number++

            image = stretchImage(image, (width, height))

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
