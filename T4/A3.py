import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    videoBN = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bajo_alto = cv2.Canny(videoBN, 50, 150)
    alto_bajo = cv2.Canny(videoBN, 200, 250)
    
    cv2.imshow('Bajo - Alto', bajo_alto)
    cv2.imshow('Alto - Bajo', alto_bajo)

    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

video.release()
cv2.destroyAllWindows()
