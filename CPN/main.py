import turtle as t
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import colorgram
import os, sys

#Global Vars
directory = ""

#Methods

# locateImg() method:
# locates image and returns image location
def locateImg():
    imgFinder = filedialog.askopenfilename(title="Select Image File", filetypes=[('Image File', ("*.jpg", "*.png"))])  # initialdir = os.get pwd? ) # fixed filetypes
    if imgFinder is not None:
        global directory
        directory = os.path.split(imgFinder)[0] + "/" + os.path.split(imgFinder)[1]
        # print(directory)
        # img = Image.open(imgFinder)
        # img = ImageTk.PhotoImage(img)


# extractedColors = colorgram.extract('test.png', 20)
# colorList = []  # can uncomment and mess around with it.
# for color in extractedColors:
#     newColor = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colorList.append(newColor)

# print(colorList)
def generateColors(colorList):
    generator.setheading(135)
    generator.forward(375)
    generator.setheading(0)
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

def saveImage():
    #UPDATE: We might have to save from the Tkinter instead of the turtle screen.
    # canvas saving features. Currently saves as a .eps file (which can be opened with Preview as a PDF) but working on
    # converting the .eps file to a universal .png or .jpg file
    # Requires installing ghostscript (using 'pip install' gave me errors, so i used homebrew to install the package)
    screenCapture = generator.getscreen()  # hs = captures the screen of the 'generator', to be used later for exporting the pallet
    screenCapture.getcanvas().postscript(file="out.eps")  # hs = exports the screenCapture as a eps file (typescript)
    outputFile = "output_result.png"  # hs = name of output file of final .png output file
    Image.open("out.eps").convert('RGBA').save(outputFile,lossless=True)  # hs = converts eps file to RGBA(.png) color profile and saves as .png
    # deletes the .eps file HOWEVER .eps seems to be higher quality than the .png (up to you if you want to keep
    # the .eps file)
    # os.remove("out.eps")  # hs = removes 'out.eps' from system

    # Option to save the image

root = Tk()
root.title("Color Palette Generator")
root.geometry("800x600")
root.config(bg = "maroon")
canvas = Canvas(master=root, width=600, height = 500)
canvas.grid(row=0, padx=30, pady=20, columnspan= 6)
t.colormode(255)
generator = t.RawTurtle(canvas)

#Buttons:

#ImgLocator
style = ttk.Style()
style.configure('TButton', padding=6, relief="flat", foreground="black", font='georgia 13 bold')
imageLocation = ttk.Button(root, text="Import Image", style='TButton', command = locateImg)
savePalette = ttk.Button(root, text="Save Palette")
imageLocation.grid(row=1, column=1)
savePalette.grid(row=1, column=2)
generator.shape("circle")
generator.hideturtle()
generator.speed("fastest")
generator.penup()
generator.setheading(135)






# Sample color list made from above.
colorList = [(247, 242, 234), (237, 242, 248), (249, 240, 244), (238, 248, 244), (137, 167, 198), (197, 138, 149),
             (211, 152, 114), (26, 37, 57), (53, 105, 145), (144, 179, 162), (156, 66, 53), (232, 213, 98),
             (138, 67, 76), (158, 25, 33), (29, 53, 47), (231, 164, 171), (50, 38, 44), (53, 109, 89), (196, 94, 104),
             (207, 85, 72), (155, 29, 24), (48, 41, 37), (18, 94, 69), (234, 170, 160), (174, 189, 215),
             (109, 123, 160), (25, 60, 112), (172, 203, 189), (43, 152, 198), (158, 202, 220), (250, 111, 231)]

# turtle program to run colors


numOfColors = len(colorList)
generator.forward(375)
generator.setheading(0)

# for dot in range(1, numOfColors):
#     color = colorList[dot - 1]
#     generator.dot(50, color)
#     generator.forward(50)
#     if dot % 10 == 0:
#         generator.setheading(270)
#         generator.forward(50)
#         generator.setheading(180)
#         generator.forward(500)
#         generator.setheading(0)


root.mainloop()
print(directory) #test to verify correct image location