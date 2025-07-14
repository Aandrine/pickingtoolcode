import numpy as np
import cv2
import matplotlib.pyplot as plt

# To read image from disk, we use
# cv2.imread function, in below method,
path = "geeks14.png"

src = cv2.imread(path)

window = "image"

# image = cv2.rotate(src,cv2.ROTATE_90_CLOCKWISE)

# image2 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

(rows, cols) = src.shape[:2]

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
res = cv2.warpAffine(src,M,(cols,rows))

blurred = cv2.GaussianBlur(src,(5,5),0)


# edges = cv2.Canny(image2,100,200)

cv2.rectangle(blurred,(30,30),(300,200),(0,255,0),5)

cv2.imwrite("lagra.png",blurred)
cv2.imshow(window,res)

cv2.waitKey(0)
cv2.destroyAllWindows()