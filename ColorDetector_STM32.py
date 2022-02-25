# --------------------------------------------Bibliotecas Usadas--------------------------------------------------------#
import cv2
import serial
import time

# ----------------------------------------------------------------------------------------------------------------------#


# --------------------------------------------Habilita Serial-----------------------------------------------------------#

ser = serial.Serial('COM20', 115200, bytesize=8, timeout=1)  # Configurando e abrindo a port


# print(ser.name)

# ----------------------------------------------------------------------------------------------------------------------#


# --------------------------------------------Função Contador-----------------------------------------------------------#

def contador():
    for i in range(0, 5):
        # print('Número {}\n'.format((i)))

        # print(time.ctime())

        time.sleep(0.5)


# ----------------------------------------------------------------------------------------------------------------------#


# -----------------------------------------Teste de Cores de Fundo------------------------------------------------------#

# img = cv2.imread("Resources/blue.jpg")
# img = cv2.imread("Resources/red.jpg")
# print(img)  # Imprime Matriz de Pixels da imagem
# cv2.imshow("img",img)
# cv2.waitKey(0)

# ----------------------------------------------------------------------------------------------------------------------#


# -------------------------------------------Centro da Imagem ---------------------------------------------------------#
cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cy, cx]

    hue_value = pixel_center[0]

#----------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------Cores para ser identidificadas-----------------------------------------#

   # color = "Undefined"
    # hue_value = 0

    if hue_value < 5:

        color = "RED"
        ser.write(b'0\n')


    elif hue_value>100 and hue_value<127:

        color = "BLUE"
        ser.write(b'1\n')

    elif hue_value <150:

        color = "Undefined"
        ser.write(b'U')

# ---------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#



    print(pixel_center)

    pixel_center_bgr = frame[cy, cx]

    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.putText(frame, color, (10, 70), 0, 1.5, (b, g, r), 2)

    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == 27:  # Tecla 27 do Teclado

        break

cap.release()
cv2.destroyAllWindows()



