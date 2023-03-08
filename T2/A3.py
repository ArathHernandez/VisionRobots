import cv2 as cv

imagen = cv.imread('T2A6.png')

neg = abs(255-imagen)

cv.imshow("Imagen original", imagen)
cv.imshow("Imagen negativa", neg)
cv.waitKey()
