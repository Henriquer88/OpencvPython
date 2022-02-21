# Face Detection #

import cv2
faceCascade = cv2.CascadeClassifier("Resources"/)
img = cv2.imread('Resources/mulher.png')

img_resolution = cv2.resize(img,(500,500))

cv2.imshow("Result", img_resolution)
cv2.waitKey(0)