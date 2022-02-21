import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    red_frame = cv2.GaussianBlur(frame,(5,5),0)
    hsv_frame = cv2.cvtColor(red_frame, cv2.COLOR_BGR2HSV)


    # BLUE Color
    low_blue = np.array([38,86,0])
    high_blue = np.array([121,255,255])
    red_mask = cv2.inRange(hsv_frame,low_blue,high_blue)                    # Identifica  apenas a cor BLUE
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area =  cv2.contourArea(contour)
      #  print(area)

        if area<78837:
            cv2.drawContours(frame,contour,-1,(0,255,0),3)
            print('Quadrado')

   # cv2.drawContours(frame, contours, -1, (0,255,0) , 3)

   # print(contours)

    cv2.imshow("Frame",frame)
    cv2.imshow("",red_mask)


#----------------------------------------------------------------------------------------------------------------------#


    key =cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()