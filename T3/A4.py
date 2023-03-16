import cv2

# Cargamos la imagen en color
img_color = cv2.imread('Numeros_Borrozos-1.jpg', cv2.IMREAD_COLOR)

# Mostramos la imagen original
cv2.imshow('Imagen original', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertimos la imagen a escala de grises
img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Aplicamos el filtro de mediana
img_mediana = cv2.medianBlur(img_gris, 5)

# Aplicamos el filtro gaussiano
img_gaussiano = cv2.GaussianBlur(img_gris, (5, 5), 0)

# Aplicamos el filtro bilateral
img_bilateral = cv2.bilateralFilter(img_gris, 9, 75, 75)

# Mostramos las imágenes filtradas
cv2.imshow('Imagen filtrada con mediana', img_mediana)
cv2.waitKey(0)
cv2.imshow('Imagen filtrada con gaussiano', img_gaussiano)
cv2.waitKey(0)
cv2.imshow('Imagen filtrada con bilateral', img_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
