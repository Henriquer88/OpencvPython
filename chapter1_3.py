import cv2

img = cv2.imread("Resources/mulher.png")


print(img.shape)   # Mostra o tamanho da foto #

imgResize = cv2.resize(img,(1000,500))  # Alterando a resolução da imagem #
print(imgResize.shape)

imgCropped =img[0:300,200:800]

cv2.imshow("Image", img)
#cv2.imshow("Image Resolution", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)
