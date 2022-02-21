
import cv2
import numpy as np

img= cv2.imread('Resources/paisagem.jpg')

imgHor =np.hstack((img,img)) # Duplica a imgaem na Horizontal

imgVert = np.vstack((img,img)) # Duplica a imgaem na Vertical


cv2.imshow("Horizontal",imgHor)

cv2.imshow("Vertical",imgVert)

cv2.waitKey(0)