import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread('sudoku.jpg', cv2.IMREAD_GRAYSCALE)
imagen = cv2.resize(imagen, (700, 700))

imagen_gauss = cv2.GaussianBlur(imagen, (5, 5), 0)

ret, imagen_bn_bin = cv2.threshold(imagen, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, imagen_gauss_bin = cv2.threshold(imagen_gauss, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Imagen binarizada antes de gauss', imagen_bn_bin)
cv2.imshow('Imagen binarizada despues de gauss', imagen_gauss_bin)

hist = cv2.calcHist([imagen_gauss_bin], [0], None, [256], [0, 256])
hist_antes = cv2.calcHist([imagen_bn_bin], [0], None, [256], [0, 256])

plt.plot(hist)
plt.plot(hist_antes)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
