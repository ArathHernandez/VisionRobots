import cv2
import numpy as np
from scipy import ndimage

imagen = cv2.imread('Hipo.jpg', cv2.IMREAD_GRAYSCALE)
imagen = cv2.resize(imagen, (700, 700))

kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

imagen_convolve = ndimage.convolve(imagen, kernel)
magnitud = np.abs(imagen_convolve)
escalada = magnitud * 255.0 / np.max(magnitud)
sobel_x = np.uint8(escalada)

cv2.imshow('Sobel en X', sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
