import turtle as t
from tkinter import *
from tkinter import filedialog
import random as r
from PIL import Image, ImageTk
import colorgram

#Main User Interface

root = Tk()
root.title('Hello Artist')
root.geometry("1000x1000")


#User will locate Img they and and create a Pillow Object from it to use in ColorGram.py

def locateImg():
    imgFinder = filedialog.askopenfilename(title = "select Image File", fileTypes = (('JPG file', "*.jpg"), ("PNG file", '.*.png'))) #initialdir = os.get pwd? )



#Image color extraction: I commented it out to save memory on our computers.
# User would input the number of colors they want from the image:
        #Ex. They pick 20.


# extractedColors = colorgram.extract('user.jpg', 20)
# colorList = []  #can uncomment and mess around with it.
# for color in extractedColors:
#     newColor = (color.rgb.r, color.rgb.g color.rgb.b)
#     colorList.append(newColor)
#
# print(colorList)


t.colormode(255)

#Sample color list made from above.
colorList = [(247, 242, 234), (237, 242, 248), (249, 240, 244), (238, 248, 244), (137, 167, 198), (197, 138, 149), (211, 152, 114), (26, 37, 57), (53, 105, 145), (144, 179, 162), (156, 66, 53), (232, 213, 98), (138, 67, 76), (158, 25, 33), (29, 53, 47), (231, 164, 171), (50, 38, 44), (53, 109, 89), (196, 94, 104), (207, 85, 72), (155, 29, 24), (48, 41, 37), (18, 94, 69), (234, 170, 160), (174, 189, 215), (109, 123, 160), (25, 60, 112), (172, 203, 189), (43, 152, 198), (158, 202, 220), (250,111,231)]

#turtle program to run colors

screen = t.Screen()
screen.title("Color Palette Generator")
generator = t.Turtle()
generator.shape("arrow")
generator.speed("fastest")
generator.penup()
generator.setheading(135)
generator.forward(375)
generator.setheading(0)

numOfColors = len(colorList)

for dot in range(1, numOfColors):
    color = colorList[dot - 1]
    generator.dot(50, color)
    generator.forward(50)
    if dot % 10 == 0:
        generator.setheading(270)
        generator.forward(50)
        generator.setheading(180)
        generator.forward(500)
        generator.setheading(0)


#Option to save the image

screen.exitonclick()
