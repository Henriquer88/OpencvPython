# Algumas funções do opencv

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)         # Imagem de fundo
#print(img)                                   # Shape - Mostra o tamanho da imagem

#img[:]=255,0,0   # Cor Azul

#img[10:300,200:300]=255,0,0  # Dimenciona o tamanho da imagem com cor

#cv2.line(img,(0,0),(300,300),(0,255,0),3)   # Criação de linha --obs o número é a espessura da linha

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # Cria-se uma linha vertica lingando os extremos

cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)               # Cria - se um retângulo

cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)     # Cria - se um retângulo  preenchido

cv2.circle(img,(400,50),30,(255,255,0),3)                   # Cria - se um Circulo

cv2.putText(img,"HENRIQUE",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)  # Texto na Imagem

cv2.imshow("Image", img)


cv2.waitKey(0)