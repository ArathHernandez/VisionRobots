import cv2
import numpy as np
from scipy import ndimage

# Cargar la imagen
img = cv2.imread('pasaporte.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (700, 700))

# Definir el kernel de Sobel en dirección X
kernel = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

# Realizar la convolución utilizando la función filter2D de OpenCV
dst = cv2.filter2D(img, -1, kernel)

# Calcular la magnitud de la derivada
dst = np.abs(dst)

# Escalar los valores al rango [0, 255]
dst = (dst * 255 / np.max(dst)).astype(np.uint8)

# Mostrar la imagen resultante
cv2.imshow('Derivada de Sobel en direccion X', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
