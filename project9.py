"""
Student:  Robin G. Blaine
Date:     October 26, 2017
Class:   _Python Programming

Assignment (Module 2, Chapter 7, Project 9): pg 290
Develop 3 algorithms (lighten, darken, colorFilter) for lightening,
darkening, and color filtering an image. (Note that colorFilter should do
most of the work.)

Pseudocode:

"""
from images import Image

def colorFilter(i, colorShift):
    for y in range(i.getHeight()):
        for x in range(i.getWidth()):
            (r, g, b) = i.getPixel(x, y)
            r += colorShift[0]
            if r > 255:
                r = 255
            elif r < 0:
                r = 0
            g += colorShift[1]
            if g > 255:
                g = 255
            elif g < 0:
                g = 0
            b += colorShift[2]
            if b > 255:
                b = 255
            elif b < 0:
                b = 0
            i.setPixel(x, y, (r, g, b))

def lighten(i, degree):
    colorFilter(i, (degree, degree, degree))

def darken(i, degree):
    colorFilter(i, (-degree, -degree, -degree))

def main():
    image1 = Image("gif1.gif")
    image2 = Image("gif2.gif")
    image3 = Image("gif3.gif")
    cont = ""
    cont = input("Press ENTER to display image1...")
    image1.draw()
    cont = input("Press ENTER to lighten image1...")
    lighten(image1, 50)
    cont = input("Press ENTER to display image2...")
    image2.draw()
    cont = input("Press ENTER to darken image2...")
    darken(image2, 50)
    cont = input("Press ENTER to display image3...")
    image3.draw()
    cont = input("Press ENTER to red-shift image3...")
    colorFilter(image3, (255, 0, 0))

main()
