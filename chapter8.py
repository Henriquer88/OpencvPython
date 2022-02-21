import cv2
import numpy as np

def getContours(img):

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:

        area = cv2.contourArea(cnt)
        print(area)                           # Imprimi o valor da área(pixels) correspondente
        #cv2.drawContours(imgContours,cnt,-1,(255,0,0),3) # Faz o contorno da forma da imagem
        if area>500:
            cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        #print(approx)    # Imprimi as coordenadas das imagens

            print(len(approx))
            objtcor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)    #Cria um retângulo no objeto detectado
            #cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,255,0),2)

            if objtcor == 3: objectType = "Tri"
            elif objtcor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio<1.05: objectType = "Square"
                else: objectType="Retangle"
            else: objectType= "None"
            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContours,objectType,(x+(w//2)-10,(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)




path = 'Resources/formas.jpg'
img = cv2.imread(path)
imgContours  = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contours",imgContours)
cv2.waitKey(0)

