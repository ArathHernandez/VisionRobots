import cv2 as cv
import numpy as np

imagen = cv.imread('actividad.jpg')
shape = imagen.shape
gray = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
blue,green,red = cv.split(imagen)

zeros = np.zeros(blue.shape, np.uint8)

blueBGR = cv.merge([blue,zeros,zeros])
greenBGR = cv.merge([zeros,green,zeros])
redBGR = cv.merge([zeros,zeros,red])

print(shape)
print(imagen)
print(gray)
print(blueBGR)
print(greenBGR)
print(redBGR)

cv.imshow('Original image',imagen)
cv.imshow('Gray image', gray)
cv.imshow('Blue Channel', blueBGR)
cv.imshow('Green Channel', greenBGR)
cv.imshow('Red Channel', redBGR)
cv.waitKey(0)
cv.destroyAllWindows()
