import cv2
import time
cap = cv2.VideoCapture(0)
cap.set(5, 30)

framecount = 0
prevMillis = 0

print(cap.get(5))

def fpsCount():
    global prevMillis
    global framecount
    millis = int(round(time.time() * 1000))
    framecount += 1
    if millis - prevMillis > 1000:
        print(framecount)
        prevMillis = millis
        framecount = 0

while True:
    __, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #blur = cv2.blur(frame, (5, 5))
    #ret, thresh = cv2.threshold(blur, 170, 255, 0)
    cv2.imshow("Image", frame)


    fpsCount()
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break



cap.release()
cv2.destroyAllWindows()