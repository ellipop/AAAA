# Importar la biblioteca OpenCV
import cv2

# Definir un objeto de captura de video
vid = cv2.VideoCapture('frens.avi')

while(True):
   
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()


    # Mostrar el cuadro resultante 
    cv2.imshow("camera", frame)

    if cv2.waitKey(25) == 32:
        break
  

vid.release()

cv2.destroyAllWindows()