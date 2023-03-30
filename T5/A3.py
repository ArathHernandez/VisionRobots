import cv2 as cv

imagen = cv.imread('manzana.jpg', 0)

imagen_canny = cv.Canny(imagen, 100, 150)

contornos, hierarchy = cv.findContours(imagen_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

max_area = 0
contorno_principal = None
for contorno in contornos:
    area = cv.contourArea(contorno)
    if area > max_area:
        max_area = area
        contorno_principal = contorno

imagen_contorno = cv.drawContours(imagen.copy(), [contorno_principal], 0, (0, 255, 0), 3)
imagen_todos = cv.drawContours(imagen.copy(), contornos, -1, (0, 255, 0), 3)

cv.imshow('Imagen con contorno principal', imagen_contorno)
cv.imshow('Imagen con todos los contornos', imagen_todos)
cv.waitKey()
cv.destroyAllWindows()
