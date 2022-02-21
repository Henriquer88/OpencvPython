import cv2
import numpy as np

# Captura de Imagem #

# print("Package Imported")

# img = cv2.imread("Resources/placa.PNG")

# cv2.imshow("Output",img)

# cv2.waitKey(0)

#----------------------------------------------------------------------------------------------------------------------#

# Captura de Vídeo  #

# cap = cv2.VideoCapture("Resources/mons.mp4")

 # while True:
#   success,img = cap.read()
 #   cv2.imshow("Video",img)
  #  if cv2.waitKey(20) & 0xFF ==ord('q'):   # Quando o caracter 'q' é pressionado o vídeo é fechado #
   #     break
#----------------------------------------------------------------------------------------------------------------------#

# Captura de WebCam  #

#cap = cv2.VideoCapture(2)
#cap.set(3,640)
#cap.set(4,480)

#while True:
  #  success, img = cap.read()
  #  cv2.imshow("Video", img)
  #  if cv2.waitKey(1) & 0xFF ==ord('q'):
  #    break

# Alterando a cor da Imagem   #
kernel = np.ones((10,10),np.uint8)  # Para fazer a dilatação imagem é necessário usar uma matrix de Kernel -- 0-255#
img =cv2.imread("Resources/mulher.png")

imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Deixa imagem Gray #
imBlur = cv2.GaussianBlur(imGray,(7,7),1)     # Aplica um filtro Gaussiano  #
imgCanny = cv2.Canny(img,150,200)              # Aplica um " Negativo na foto  #
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

#cv2.imshow("Gray Image",imGray)
#cv2.imshow("Blur Image",imBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)