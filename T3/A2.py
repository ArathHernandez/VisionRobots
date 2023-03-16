import cv2
import matplotlib.pyplot as plt

img_bn = cv2.imread('Numeros_Binarizacion.jpg', cv2.IMREAD_GRAYSCALE)

img_filtrada = cv2.GaussianBlur(img_bn, (5, 5), 0)

cv2.imshow('Imagen filtrada', img_filtrada)

hist = cv2.calcHist([img_filtrada], [0], None, [256], [0, 256])

plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
