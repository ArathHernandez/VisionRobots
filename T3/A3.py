import cv2
import matplotlib.pyplot as plt

# Cargamos la imagen en blanco y negro
img_bn = cv2.imread('Numeros_Binarizacion.jpg', cv2.IMREAD_GRAYSCALE)

# Mostramos la imagen
cv2.imshow('Imagen en blanco y negro', img_bn)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicamos el filtro gaussiano
img_filtrada = cv2.GaussianBlur(img_bn, (5, 5), 0)

# Mostramos la imagen filtrada
cv2.imshow('Imagen filtrada', img_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Binarización de la imagen sin filtro
ret, img_bn_bin = cv2.threshold(img_bn, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Mostramos la imagen binarizada
cv2.imshow('Imagen binarizada sin filtro', img_bn_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Binarización de la imagen con filtro
ret, img_filtrada_bin = cv2.threshold(img_filtrada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Mostramos la imagen binarizada
cv2.imshow('Imagen binarizada con filtro', img_filtrada_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculamos el histograma de la imagen filtrada binarizada
hist = cv2.calcHist([img_filtrada_bin], [0], None, [256], [0, 256])

# Mostramos el histograma
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
