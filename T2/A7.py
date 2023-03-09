import cv2 as cv

imagen = cv.imread("T2A7.jpg")
hsv = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)

h,s,v = cv.split(hsv)

cv.imshow("H", h)
cv.imshow("S", s)
cv.imshow("V", v)
cv.waitKey()
