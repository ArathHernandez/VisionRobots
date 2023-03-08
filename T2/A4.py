import cv2 as cv

imagen = cv.imread('T2A6.png')

rot = cv.rotate(imagen, cv.ROTATE_90_CLOCKWISE)

cv.imshow("Imagen original", imagen)
cv.imshow("Imagen rotada", rot)
cv.waitKey()
