import cv2
import serial

ser = serial.Serial('COM3', 9600)
# 0 es la camara de la laptop, 1 es la camara USB  (no se porque a veces cambia el orden)
cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
  ret,frame = cap.read()
  
  if ret:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
      ser.write(str('h').encode())
    else:
      ser.write(str('n').encode())

    for (x,y,w,h) in faces:
      cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

    #la siguiente línea debe estar alineada con for, si se le pone sangría da error que no abre la ventana de camara al ejecutar el programa. 
    #hasta que detecte un rostro abre el cuadro, y si se pone la mano frente a la camara, se congela la imagen. 

    cv2.imshow('frame',frame)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
ser.close()
cap.release()
cv2.destroyAllWindows()

