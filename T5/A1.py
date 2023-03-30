import cv2 as cv

imagen = cv.imread('perrosonriendo.jpg', cv.IMREAD_GRAYSCALE)
imagen = cv.resize(imagen,(600,500))

imagen_canny = cv.Canny(imagen, 100, 200)

contornos, hierarchy = cv.findContours(imagen_canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

imagen = cv.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

cv.imshow('Imagen con contornos', imagen)
cv.waitKey()
cv.destroyAllWindows()
