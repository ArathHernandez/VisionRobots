import cv2 as cv

imagen = cv.imread("T2A7.jpg")
rgb = cv.cvtColor(imagen, cv.COLOR_BGR2RGB)
hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)

cv.imshow("Imagen en RGB", rgb)
cv.imshow("Imagen en HSV", hsv)
cv.waitKey()
