
import os, sys
from PIL import Image
import math

image = Image.open('old.jpeg')
pixmap = image.load()

ascii_arr =["\"", ".",":","-","=","+","*","#","%","@"]

f = open("test.txt", "w")

print(image.size[0])
print(image.size[1])

for i in range(image.size[1]):
    for j in range(image.size[0]):
        print(str(i) + " " +  str(j))
        match pixmap[j,i]:
            case (r, g, b):
                luminance = int((0.2126*r + 0.7162*b + 0.0722*g)/25)
                f.write(ascii_arr[luminance])
    f.write("\n")


# image.show()



