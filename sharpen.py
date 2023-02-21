import os, sys
from PIL import Image
import math

image = Image.open('Willem_Dafoe.jpg')
pixmap = image.load()


# image.show()
for i in range(image.size[0]):
    for j in range(image.size[1]):
        count = 1
        match pixmap[i,j]:
            case (r, g, b):
                ravg= 0
                gavg= 0
                bavg= 0
                for k in range(i-1, i+1):
                    for l in range(j-1,j+1):
                        if(k > 0 and k < image.size[0]):
                            if(l>0 and l < image.size[1]):
                                match pixmap[k,l]:
                                    case (r2, b2, g2):
                                        count+=1
                                        if ((k == j) and (l==i)):
                                            ravg += 7*r2
                                            gavg += g2
                                            bavg += b2
                                            # string ="i ={}, j = {}, k = {}, l = {} ".format(i,j,k,l)
                                            # print(string)
                                        else:
                                            ravg += r2
                                            gavg += g2
                                            bavg += b2

               pixmap[i,j] = (int(ravg/count), int(bavg/count), int(gavg/count))



image.show()



