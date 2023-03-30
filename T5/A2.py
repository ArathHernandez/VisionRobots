import cv2 as cv

imagen = cv.imread('perrosonriendo.jpg', cv.IMREAD_GRAYSCALE)
imagen = cv.resize(imagen,(600,500))

imagen_canny = cv.Canny(imagen, 100, 150)

contornos, hierarchy = cv.findContours(imagen_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

print("Número de contornos encontrados: ", len(contornos))
for i, c in enumerate(contornos):
    print("Contorno ", i, ": ", c)
