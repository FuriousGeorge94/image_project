import os, sys
from PIL import Image
import math

image = Image.open('old.jpeg')
pixmap = image.load()


image.show()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        match pixmap[i,j]:
            case (r, g, b):
                ravg= r
                gavg= b
                bavg= g
                count = 1
                for k in range(i-1, i+1):
                    for l in range(j-1,j+1):
                        if(i > 0 and i < image.size[0]):
                            if(j>0 and j < image.size[1]):
                                match pixmap[k,l]:
                                    case (r2, g2, b2):
                                        count+=1
                                        ravg += r2
                                        gavg += g2
                                        bavg += b2
                    pixmap[i,j] = (int(ravg/count), int(bavg/count), int(gavg/count))



image.show()



